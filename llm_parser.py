import requests
import json
from langsmith import traceable
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)


OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are an HR assistant. Extract information into JSON.

Possible intents:
- employee_details
- leave_balance
- interview_questions
- hr_general

Rules:
- Use employee_details ONLY if a specific employee is explicitly mentioned.
- Use leave_balance ONLY if the question is about leave days for a named employee.
- Use interview_questions if the user asks for interview or screening questions.
- Use hr_general for questions about HR concepts, roles, responsibilities, policies, or definitions.
- DO NOT assume an employee exists if no person is named.

Schema:
{
  "intent": string,
  "employee_name": string | null,
  "job_role": string | null
}

EXAMPLES:
User: "Tell me about Omar Habli"
{"intent": "employee_details", "employee_name": "Omar Habli", "job_role": null}

User: "Interview questions for Data Scientist"
{"intent": "interview_questions", "employee_name": null, "job_role": "Data Scientist"}

User: "Nagham's leave balance"
{"intent": "leave_balance", "employee_name": "Nagham Habli", "job_role": null}

User: "What are the responsibilities of an HR manager?"
{"intent": "hr_general", "employee_name": null, "job_role": null}

Return ONLY valid JSON. No text outside JSON.
"""

@traceable
def parse_user_query(user_query: str) -> dict:
    prompt = SYSTEM_PROMPT + "\nUser query: " + user_query

    raw_output = llm.invoke([
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": user_query}
]).content


    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {
            "intent": None,
            "employee_name": None,
            "job_role": None
        }
