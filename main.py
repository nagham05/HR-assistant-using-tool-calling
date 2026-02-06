from dotenv import load_dotenv
load_dotenv()

from llm_parser import parse_user_query, llm
from hr_logic import handle_intent, get_employee_details

session_state = {"awaiting_id": False}

def chat(user_input: str):
    global session_state
    
    # 1. Handle clarification flow (Existing logic)
    if session_state["awaiting_id"] and user_input.strip().isdigit():
        session_state["awaiting_id"] = False 
        emp = get_employee_details(user_input.strip())
        
        if "error" in emp:
            return "ID not found. Please try again."
            
        return f"Details found!\nName: {emp['name']}\nDept: {emp['department']}\nRole: {emp['role']}"

    # 2. Parse the query
    intent_data = parse_user_query(user_input)
    
    # --- FIX STARTS HERE ---
    # Extract only the text if 'direct_response' exists
    if intent_data.get("direct_response"):
        session_state["awaiting_id"] = False
        return intent_data["direct_response"] # Return ONLY the string value
    # --- FIX ENDS HERE ---

    # 3. Handle specific HR logic (leave, details, etc.)
    response = handle_intent(intent_data)

    if "Please clarify" in response:
        session_state["awaiting_id"] = True
    else:
        session_state["awaiting_id"] = False
        
    return response