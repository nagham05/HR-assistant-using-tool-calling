# function to get employee details by employee ID
def get_employee_details(employee_id):
    employees = {
        "123": {"name": "Nagham Habli", "department": "AI development", "role": "Junior AI developer"},
        "456": {"name": "Omar Habli", "department": "ECE", "role": "Junior Electric Engineering"},
        "789": {"name": "Marwa Baba", "department": "Software Development", "role": "Senior Software Engineer"}
    }
    return employees.get(employee_id, {"error": "Employee not found"})

# function to check leave balance by employee ID 
def check_leave_balance(employee_id):
    leave_balances = {
        "123": {"remaining days": 15},
        "456": {"remaining days": 5},
        "789": {"remaining days": 10}
    }
    return leave_balances.get(employee_id, {"error": "Employee not found"})

# function to generate interview questions based on job role
def generate_interview_questions(job_role):
    questions = {
        "Junior AI developer": [
            "What is overfitting in machine learning?",
            "Explain the difference between supervised and unsupervised learning.",
            "How do you handle missing data in a dataset?"
        ],
        "Junior Electric Engineering": [
            "What is Ohm's Law?",
            "Explain the difference between AC and DC current.",
            "What are the main components of an electrical circuit?"
        ],
        "Senior Software Engineer": [
            "Describe the software development lifecycle.",
            "How do you ensure code quality in your projects?",
            "What design patterns are you familiar with?"
        ],
        "Data Scientist": [
            "What is the difference between a classification and regression problem?",
            "How do you handle multicollinearity in a dataset?",
            "Explain the concept of cross-validation."
        ]
    }
    return questions.get(job_role, ["No questions available for this role."])
