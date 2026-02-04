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
You are an HR assistant. Extract info into JSON. 
Intents: employee_details, leave_balance, interview_questions.

EXAMPLES:
User: "Tell me about Omar Habli"
{"intent": "employee_details", "employee_name": "Omar Habli", "job_role": null}

User: "Interview questions for Data Scientist"
{"intent": "interview_questions", "employee_name": null, "job_role": "Data Scientist"}

User: "Nagham's leave balance"
{"intent": "leave_balance", "employee_name": "Nagham Habli", "job_role": null}

Return ONLY JSON.
"""

@traceable
def parse_user_query(user_query: str) -> dict:
    prompt = SYSTEM_PROMPT + "\nUser query: " + user_query

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    raw_output = llm.invoke(prompt).content

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {
            "intent": None,
            "employee_name": None,
            "job_role": None
        }
