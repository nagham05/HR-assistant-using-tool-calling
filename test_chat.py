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


if __name__ == "__main__":
    # Example queries
    test_query("Tell me about Omar Habli")
    test_query("How many leave days does Marwa Baba have?")
    test_query("Give me interview questions for Senior Software Engineer")
