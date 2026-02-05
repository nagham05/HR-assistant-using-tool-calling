"""
Pipeline logic for Human Resources (HR) management system.

Input -> Normalize -> Intent detection -> Tool needed? -> Which tool? -> Extract arguments -> Validate arguments
-> Execute tool -> Interpret result -> Respond
"""
from langsmith import traceable


from hr_tools import (
    get_employee_details,
    check_leave_balance,
    generate_interview_questions,
)

EMPLOYEE_NAME_TO_IDS = {
    "nagham habli": ["123"],
    "omar habli": ["456", "912"],  # future duplicate
    "marwa baba": ["789"]
}

job_roles = [
    "Junior AI developer",
    "Junior Electric Engineering",
    "Senior Software Engineer",
    "Data Scientist"
]

@traceable
def extract_employee_ids_from_name(query):
    query = query.lower()
    matched_ids = []

    for name, emp_ids in EMPLOYEE_NAME_TO_IDS.items():
        if name in query:
            matched_ids.extend(emp_ids)

    return matched_ids

@traceable
def handle_employee_details(data: dict):
    employee_name = data["employee_name"]

    if not employee_name:
        return "Please specify the employee name."

    employee_ids = extract_employee_ids_from_name(employee_name)

    if not employee_ids:
        return "I couldn’t find any employee with that name."

    if len(employee_ids) > 1:
        return (
            "I found multiple employees with that name:\n" +
            "\n".join(
                f"- {get_employee_details(eid)['department']} (ID: {eid})"
                for eid in employee_ids
            ) +
            "\nPlease clarify which one you mean."
        )

    emp = get_employee_details(employee_ids[0])

    return (
        f"Name: {emp['name']}\n"
        f"Department: {emp['department']}\n"
        f"Role: {emp['role']}"
    )

@traceable
def handle_leave_query(data: dict):
    employee_name = data["employee_name"]

    if not employee_name:
        return "Please specify the employee name."

    employee_ids = extract_employee_ids_from_name(employee_name)

    if len(employee_ids) != 1:
        return "Please clarify which employee you mean."

    leave = check_leave_balance(employee_ids[0])
    return f"Remaining Leave Days: {leave['remaining days']}" 

@traceable
def handle_interview_questions(data: dict):
    role = data["job_role"]

    if not role:
        return "Please specify the job role."

    questions = generate_interview_questions(role)
    return f"Interview Questions for {role}:\n" + "\n".join(questions)

@traceable
def handle_intent(intent_data: dict):
    intent = intent_data["intent"]

    if intent == "employee_details":
        return handle_employee_details(intent_data)

    elif intent == "leave_balance":
        return handle_leave_query(intent_data)

    elif intent == "interview_questions":
        return handle_interview_questions(intent_data)
    
    elif intent == "hr_general":
        return "HR_GENERAL"

    return "Sorry, I couldn’t understand your HR request."
