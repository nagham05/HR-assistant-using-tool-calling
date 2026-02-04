"""
Pipeline logic for Human Resources (HR) management system.

Input -> Normalize -> Intent detection -> Tool needed? -> Which tool? -> Extract arguments -> Validate arguments
-> Execute tool -> Interpret result -> Respond
"""

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

def handle_query(user_query: str):
    user_query = user_query.lower()

    if "employee" in user_query or "details" in user_query:
        return handle_employee_details(user_query)

    elif "leave" in user_query:
        return handle_leave_query(user_query)

    elif "interview" in user_query or "questions" in user_query:
        return handle_interview_questions(user_query)

    else:
        return "Sorry, I couldn’t understand your HR request."



def extract_employee_ids_from_name(query):
    query = query.lower()
    matched_ids = []

    for name, emp_ids in EMPLOYEE_NAME_TO_IDS.items():
        if name in query:
            matched_ids.extend(emp_ids)

    return matched_ids


def handle_employee_details(query):
    employee_ids = extract_employee_ids_from_name(query)

    if not employee_ids:
        return "I couldn’t find any employee with that name."

    if len(employee_ids) > 1:
        return (
            "I found multiple employees with that name:\n" +
            "\n".join(
                f"- {get_employee_details(eid)['department']} (ID: {eid})"
                for eid in employee_ids
            ) +
            "\nPlease specify which one you mean."
        )

    # Exactly one match
    data = get_employee_details(employee_ids[0])

    return (
        f"Name: {data['name']}\n"
        f"Department: {data['department']}\n"
        f"Role: {data['role']}"
    )

def handle_leave_query(query: str):
    employee_ids = extract_employee_ids_from_name(query)

    if not employee_ids:
        return "I couldn’t find any employee with that name."

    if len(employee_ids) > 1:
        return (
            "I found multiple employees with that name:\n" +
            "\n".join(
                f"- {get_employee_details(eid)['department']} (ID: {eid})"
                for eid in employee_ids
            ) +
            "\nPlease specify which one you mean."
        )

    # Exactly one match
    data = check_leave_balance(employee_ids[0])

    return f"Remaining Leave Days: {data['remaining days']}"


def handle_interview_questions(query: str):
    
    for role in job_roles:
        if role.lower() in query:
            questions = generate_interview_questions(role)
            return f"Interview Questions for {role}:\n" + "\n".join(questions)
    return "No questions available for this role."

