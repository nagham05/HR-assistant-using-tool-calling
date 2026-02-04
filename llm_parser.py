import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are an HR assistant.
Extract structured information from the user query.

Return ONLY valid JSON in this exact format:
{
  "intent": "",
  "employee_name": null,
  "job_role": null
}

Valid intents:
- employee_details
- leave_balance
- interview_questions

Rules:
- Use null if information is missing
- Do not explain anything
- Do not add extra text
"""

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

    raw_output = response.json()["response"]

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        return {
            "intent": None,
            "employee_name": None,
            "job_role": None
        }
