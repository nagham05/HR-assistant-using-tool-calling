from dotenv import load_dotenv
load_dotenv()

from llm_parser import parse_user_query
from hr_logic import handle_intent, get_employee_details
import re

session_state = {"awaiting_id": False}

def clean_direct_response(text: str) -> str:
    # Remove common LLM meta-explanations
    patterns = [
        r"Here is the extracted intent.*?\n",
        r"^What does HR do\?\s*",
    ]

    for p in patterns:
        text = re.sub(p, "", text, flags=re.IGNORECASE | re.DOTALL)

    return text.strip()


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
    
    # Extract only the text if 'direct_response' exists
    if intent_data.get("direct_response"):
        session_state["awaiting_id"] = False

        text = intent_data["direct_response"]

        # Remove LLM meta explanations completely
        # This pattern removes "Here is the extracted intent in JSON format:" 
        # and the entire JSON structure including triple quotes
        text = re.sub(
            r'Here is the extracted intent in JSON format:\s*\{[^}]*"direct_response":\s*"""',
            "",
            text,
            flags=re.DOTALL | re.IGNORECASE
        )
        
        # Also remove any trailing triple quotes and closing braces
        text = re.sub(r'"""\s*\}?\s*$', "", text, flags=re.DOTALL)

        return text.strip()

    # 3. Handle specific HR logic (leave, details, etc.)
    response = handle_intent(intent_data)

    if "Please clarify" in response:
        session_state["awaiting_id"] = True
    else:
        session_state["awaiting_id"] = False
        
    return response