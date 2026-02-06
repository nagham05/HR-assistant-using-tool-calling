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
- leave_balance: User asks about leave for a person.
- interview_questions: User needs help with hiring for a SPECIFIC job role (e.g., "Data Scientist").
- hr_general: General HR knowledge or definitions.

STRICT RULES:
1. If intent is 'interview_questions', 'employee_details', or 'leave_balance':
   - Set 'direct_response' to null.
   - You MUST identify the 'job_role' or 'employee_name'.
2. If intent is 'hr_general', provide a detailed Markdown response in 'direct_response'.
3. Return ONLY valid JSON. Do not include any conversational text, headers, or explanations.

JSON STRUCTURE:
{
  "intent": "string",
  "employee_name": "string or null",
  "job_role": "string or null",
  "direct_response": "string or null"
}
"""

@traceable
def parse_user_query(user_query: str) -> dict:
    raw_output = llm.invoke([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]).content

    try:
        # 1. Extract JSON block
        json_match = re.search(r'\{.*\}', raw_output, re.DOTALL)

        if not json_match:
            # No JSON at all → treat everything as HR general response
            return {
                "intent": "hr_general",
                "employee_name": None,
                "job_role": None,
                "direct_response": raw_output.strip()
            }

        json_text = json_match.group(0)
        data = json.loads(json_text)

        # 2. Capture text OUTSIDE the JSON
        remaining_text = raw_output.replace(json_text, "").strip()

        # 3. If HR general + empty direct_response → fill it
        if data.get("intent") == "hr_general" and not data.get("direct_response"):
            data["direct_response"] = remaining_text

        return data

    except Exception:
        # Emergency fallback
        return {
            "intent": "hr_general",
            "employee_name": None,
            "job_role": None,
            "direct_response": raw_output.strip()
        }
