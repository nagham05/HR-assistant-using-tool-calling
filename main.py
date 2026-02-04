from llm_parser import parse_user_query
from hr_logic import handle_intent

def chat(user_input: str):
    intent_data = parse_user_query(user_input)
    return handle_intent(intent_data)
