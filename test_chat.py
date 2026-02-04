from llm_parser import parse_user_query
from hr_logic import handle_intent

def test_query(user_input: str):
    print(f"\nUser query: {user_input}")

    # Step 1: LLM parses the input
    intent_data = parse_user_query(user_input)
    print("LLM output:", intent_data)

    # Step 2: HR logic handles it
    response = handle_intent(intent_data)
    print("System response:")
    print(response)

from main import chat

def start_terminal_chat():
    print("--- 🏢 HR Assistant Live Test ---")
    print("(Type 'quit' to exit)")
    
    while True:
        user_msg = input("\nYou: ")
        if user_msg.lower() in ["quit", "exit"]:
            break
            
        answer = chat(user_msg)
        print(f"Assistant: {answer}")

if __name__ == "__main__":
    start_terminal_chat()