from dotenv import load_dotenv
load_dotenv()

from llm_parser import parse_user_query, llm
from hr_logic import handle_intent, get_employee_details

# This variable stays alive as long as your terminal session is running
session_state = {"awaiting_id": False}

def chat(user_input: str):
    global session_state
    
    # STEP 1: If we are waiting for an ID, don't even call the LLM.
    # Just check if the user typed a number.
    if session_state["awaiting_id"] and user_input.strip().isdigit():
        session_state["awaiting_id"] = False # Reset state
        emp = get_employee_details(user_input.strip())
        
        if "error" in emp:
            return "ID not found. Please try again."
            
        return f"Details found!\nName: {emp['name']}\nDept: {emp['department']}\nRole: {emp['role']}"

    # STEP 2: Normal LLM Parsing
    intent_data = parse_user_query(user_input)
    response = handle_intent(intent_data)
    
    if response == "HR_GENERAL":
        return llm.invoke(user_input).content

    # STEP 3: If response asks for clarification, flip the 'memory' switch
    if "Please clarify" in response:
        session_state["awaiting_id"] = True
    else:
        session_state["awaiting_id"] = False
        
    return response