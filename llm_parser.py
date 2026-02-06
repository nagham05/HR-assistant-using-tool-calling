import requests
import re
import json
from langsmith import traceable
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)

SYSTEM_PROMPT = """
You are a professional HR Assistant. Extract the user's intent into JSON.

INTENTS:
- employee_details: User asks about a specific person.
- leave_balance: User asks about remaining vacation/leave for a person.
- interview_questions: User needs help with hiring or screening.
- hr_general: General HR knowledge, definitions, or policies.

RULES:
1. If intent is 'hr_general', write a detailed, professional Markdown response in 'direct_response'. 
2. Use **bolding** for headers and bullet points for lists.
3. Be thorough. Do not summarize.
4. If intent is NOT 'hr_general', 'direct_response' must be null.

JSON STRUCTURE:
{
  "intent": "string",
  "employee_name": "string or null",
  "job_role": "string or null",
  "direct_response": "string or null"
}
Return ONLY JSON.
"""

@traceable
def parse_user_query(user_query: str) -> dict:
    raw_output = llm.invoke([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]).content

    # 1. REMOVE CODE BLOCKS: Use regex to strip ```json and ``` 
    clean_output = re.sub(r'```json\s?|```', '', raw_output).strip()

    try:
        # 2. ATTEMPT TO PARSE: Convert the string to a Python dictionary
        data = json.loads(clean_output)
        return data
    except json.JSONDecodeError:
        # 3. EMERGENCY FALLBACK: If JSON is still broken, 
        # try to find the text between the "direct_response": "..." quotes
        match = re.search(r'"direct_response":\s*"(.*)"', clean_output, re.DOTALL)
        if match:
            return {
                "intent": "hr_general",
                "direct_response": match.group(1).replace('\\n', '\n').replace('\\"', '"')
            }
        
        # If all else fails, return the raw output so you can at least see the text
        return {
            "intent": "hr_general", 
            "direct_response": raw_output
        }