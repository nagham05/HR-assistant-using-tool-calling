# 🧑‍💼 AI-Powered HR Assistant

An intelligent conversational HR assistant built with LLMs, LangChain, and Gradio. This project demonstrates production-ready AI system architecture with tool-augmented LLM reasoning, intent classification, and state management.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Community-green.svg)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange.svg)
![Ollama](https://img.shields.io/badge/Ollama-LLaMA3-red.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Screenshots](#screenshots)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [System Design](#system-design)
- [Technical Highlights](#technical-highlights)
- [Example Interactions](#example-interactions)
- [Customization Guide](#customization-guide)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **AI-Powered HR Assistant** is a conversational AI system designed to handle various HR-related queries through natural language interaction. It intelligently routes requests between direct LLM responses and structured tool executions, demonstrating modern AI agent architecture patterns.

### Key Capabilities

1. **Employee Information Retrieval** - Get detailed employee information by name
2. **Leave Balance Checking** - Query remaining leave days for employees
3. **Interview Question Generation** - Generate role-specific interview questions
4. **General HR Knowledge** - Answer policy questions and HR-related queries

---

## 📸 Screenshots

### Main Interface

<img width="1512" height="866" alt="Screenshot 2026-02-06 at 7 25 35 PM" src="https://github.com/user-attachments/assets/7ddb11d6-d0a5-44fa-85be-31a3aeaff636" />

*Clean, professional interface with example queries and full-screen chat experience*

### Employee Information Query

<img width="894" height="551" alt="Screenshot 2026-02-06 at 7 24 55 PM" src="https://github.com/user-attachments/assets/29ed899a-3c85-4ef5-9ee6-5cf7e410213f" />

*Multi-employee disambiguation and detailed employee information retrieval*

### Leave Balance & Interview Questions
<img width="880" height="460" alt="Screenshot 2026-02-06 at 7 25 12 PM" src="https://github.com/user-attachments/assets/f1d398b5-4ed2-48ae-96e3-cf7196d37a0e" />

*Instant leave balance lookup and role-specific interview question generation*

### General HR Knowledge
<img width="810" height="540" alt="Screenshot 2026-02-06 at 7 25 22 PM" src="https://github.com/user-attachments/assets/d9dcabc3-019f-4330-80a5-f022427b2815" />

*Comprehensive HR knowledge base for policy and definition queries*

---

## ✨ Features

### Core Functionality

- ✅ **Intent Classification** - Automatically detects user intent from natural language
- ✅ **Tool-Augmented LLM** - Seamlessly integrates LLM reasoning with structured data retrieval
- ✅ **Multi-Turn Conversations** - Maintains context across conversation turns
- ✅ **Ambiguity Resolution** - Handles duplicate employee names with clarification flow
- ✅ **State Management** - Tracks conversation state for follow-up queries
- ✅ **Observability** - Integrated LangSmith tracing for debugging and monitoring

### UI Features

- 🎨 **Modern Gradio Interface** - Clean, professional chat interface
- 🚀 **Quick Actions** - Pre-built example queries for common use cases
- 📱 **Responsive Design** - Full-screen chat experience
- 🎯 **Real-time Responses** - Instant feedback on user queries

---

## 🏗️ Architecture

### High-Level System Flow

```
┌─────────────┐
│ User Input  │
└──────┬──────┘
       │
       v
┌─────────────────────┐
│ Intent              │
│ Classification      │
│ (LLM Parser)        │
└──────┬──────────────┘
       │
       v
┌─────────────────────┐
│ Tool Required?      │
└──────┬──────────────┘
       │
   ┌───┴───┐
   │       │
   v       v
┌──────┐  ┌──────────────┐
│Direct│  │Tool Execution│
│Reply │  │& Argument    │
│      │  │Extraction    │
└──┬───┘  └──────┬───────┘
   │             │
   └──────┬──────┘
          v
   ┌──────────────┐
   │Final Response│
   └──────────────┘
```

### Component Architecture

```
┌───────────────────────────────────────────────────┐
│                  chat_interface.py                │
│              (Gradio UI Layer)                    │
└─────────────────────┬─────────────────────────────┘
                      │
                      v
┌───────────────────────────────────────────────────┐
│                    main.py                        │
│         (Orchestration & State Management)        │
└─────────────────────┬─────────────────────────────┘
                      │
         ┌────────────┼────────────┐
         v            v            v
┌─────────────┐ ┌──────────┐ ┌──────────┐
│llm_parser.py│ │hr_logic.py│ │hr_tools.py│
│(Intent      │ │(Business  │ │(Data     │
│Detection)   │ │Logic)     │ │Access)   │
└─────────────┘ └──────────┘ └──────────┘
```

---

## 📁 Project Structure

```
hr-assistant/
├── chat_interface.py      # Gradio web interface
├── main.py               # Main orchestration logic
├── llm_parser.py         # LLM-based intent classification
├── hr_logic.py           # Business logic handlers
├── hr_tools.py           # Data access layer (tool functions)
├── test_chat.py          # Terminal-based testing interface
├── logic_map.txt         # Detailed system logic documentation
├── .env                  # Environment variables
└── README.md             # This file
```

### File Descriptions

| File | Purpose | Key Functions |
|------|---------|---------------|
| **chat_interface.py** | Gradio UI setup and event handlers | `respond()` |
| **main.py** | Request routing and state management | `chat()` |
| **llm_parser.py** | Intent extraction using LLM | `parse_user_query()` |
| **hr_logic.py** | Intent-specific business logic | `handle_intent()`, `handle_employee_details()`, `handle_leave_query()`, `handle_interview_questions()` |
| **hr_tools.py** | Database/API simulation layer | `get_employee_details()`, `check_leave_balance()`, `generate_interview_questions()` |
| **test_chat.py** | CLI testing interface | `start_terminal_chat()` |

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed with LLaMA3 model
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/hr-assistant.git
cd hr-assistant
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
```
gradio==4.16.0              # Web interface framework
langchain-community==0.0.20 # LangChain ChatOllama integration
langsmith==0.1.0            # Tracing and observability
python-dotenv==1.0.0        # Environment variable management (.env file support)
requests==2.31.0            # HTTP library (imported but currently unused)
```

**What each package does:**
- **gradio**: Creates the web-based chat interface with minimal code
- **langchain-community**: Provides ChatOllama for LLM integration via Ollama
- **langsmith**: Enables tracing and debugging of LLM calls (optional but recommended)
- **python-dotenv**: Loads environment variables from `.env` file (used in main.py to load LangSmith API key)
- **requests**: HTTP library (imported in llm_parser.py; included for potential future API integrations)

### Step 3: Set Up Ollama

```bash
# Install Ollama (if not already installed)
# Visit: https://ollama.ai/download

# Pull LLaMA3 model
ollama pull llama3
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
# LangSmith (optional - for observability)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=hr-assistant
```

### Step 5: Run the Application

**Web Interface:**
```bash
python chat_interface.py
```

**Terminal Interface (for testing):**
```bash
python test_chat.py
```

---

## 💡 Usage

### Web Interface

1. Launch the application: `python chat_interface.py`
2. Open your browser to `http://localhost:7860`
3. Try the example queries or type your own
4. Chat naturally with the HR assistant

### Example Queries

```
✅ "Tell me about Omar Habli"
✅ "Check Nagham Habli leave balance"
✅ "Interview questions for Data Scientist"
✅ "What does HR do?"
✅ "How many leave days does Marwa Baba have?"
```

### Handling Ambiguity

When multiple employees share the same name:

```
User: "Tell me about Omar Habli"
Assistant: "I found multiple employees with that name:
- ECE (ID: 456)
- Data Science (ID: 912)
Please clarify which one you mean."

User: "456"
Assistant: "Details found!
Name: Omar Habli
Dept: ECE
Role: Junior Electric Engineering"
```

---

## 🧠 System Design

### Intent Classification

The system uses an LLM-based parser to extract structured intent from natural language:

**Supported Intents:**

| Intent | Description | Requires Tool | Example |
|--------|-------------|---------------|---------|
| `employee_details` | Get employee information | ✅ Yes | "Tell me about John Doe" |
| `leave_balance` | Check remaining leave days | ✅ Yes | "How many leaves does Jane have?" |
| `interview_questions` | Generate role-specific questions | ✅ Yes | "Interview questions for Data Scientist" |
| `hr_general` | General HR knowledge | ❌ No | "What does HR do?" |

### State Management

The system maintains conversation state to handle multi-turn interactions:

```python
session_state = {
    "awaiting_id": False  # Tracks if system is waiting for employee ID
}
```

### Response Pipeline

```
1. User Input
   ↓
2. Intent Classification (LLM Parser)
   ↓
3. Decision Gate: Direct Response or Tool Call?
   ↓
4. [If Tool] Argument Extraction
   ↓
5. [If Tool] Tool Execution
   ↓
6. Response Generation
   ↓
7. User Output
```

---

## 🔧 Technical Highlights

### 1. **LLM-Powered Intent Detection**

Uses structured prompting to extract JSON from natural language:

```python
SYSTEM_PROMPT = """
You are a professional HR Assistant. Extract the user's intent into JSON.

INTENTS:
- employee_details: User asks about a specific person.
- leave_balance: User asks about leave for a person.
- interview_questions: User needs help with hiring for a SPECIFIC job role.
- hr_general: General HR knowledge or definitions.

JSON STRUCTURE:
{
  "intent": "string",
  "employee_name": "string or null",
  "job_role": "string or null",
  "direct_response": "string or null"
}
"""
```

### 2. **Robust Error Handling**

- Graceful fallbacks for malformed LLM outputs
- Pattern matching for metadata cleanup
- Validation before tool execution

### 3. **Separation of Concerns**

- **UI Layer** (chat_interface.py) - Pure presentation
- **Orchestration Layer** (main.py) - Request routing
- **Logic Layer** (hr_logic.py) - Business rules
- **Data Layer** (hr_tools.py) - Data access

### 4. **Observability**

LangSmith tracing decorators on all critical functions:

```python
@traceable
def parse_user_query(user_query: str) -> dict:
    # Function implementation
```

### 5. **Anti-Hallucination Design**

- Strict tool boundaries prevent LLM from inventing data
- Structured outputs enforce data contracts
- Fallback mechanisms for edge cases

---

## 📊 Example Interactions

### 1. Employee Lookup with Disambiguation

**User Query:**
```
Tell me about Omar Habli
```

**System Response:**
```
I found multiple employees with that name:
- ECE (ID: 456)
- Data Science (ID: 912)
Please clarify which one you mean.
```

**User Follow-up:**
```
912
```

**Final Response:**
```
Details found!
Name: Omar Habli
Dept: Data Science
Role: Data Scientist
```

---

### 2. Leave Balance Check

**User Query:**
```
Check Nagham Habli leave balance
```

**System Response:**
```
Remaining Leave Days: 15
```

---

### 3. Interview Question Generation

**User Query:**
```
Interview questions for Data Scientist
```

**System Response:**
```
Interview Questions for Data Scientist:
- What is the difference between a classification and regression problem?
- How do you handle multicollinearity in a dataset?
- Explain the concept of cross-validation.
```

---

### 4. General HR Knowledge

**User Query:**
```
What does HR do?
```

**System Response:**
```
Human Resources (HR) departments are responsible for managing an organization's workforce. 
This includes tasks such as:

○ Recruiting and hiring new employees
○ Onboarding and training new hires
○ Managing employee benefits, compensation, and performance reviews
○ Handling employee conflicts and disputes
○ Maintaining accurate records of employee data and personnel files
○ Ensuring compliance with labor laws and regulations
○ Developing and implementing HR policies and procedures
○ Providing support and guidance to employees and management alike

In summary, the primary goal of an HR department is to ensure that the organization 
has the right people in the right roles, at the right time, and that they are supported 
and motivated to perform their best.
```

---

## 🛠️ Customization Guide

### Adding New Employees

Edit `hr_tools.py`:

```python
employees = {
    "123": {"name": "Nagham Habli", "department": "AI development", "role": "Junior AI developer"},
    "999": {"name": "New Employee", "department": "Marketing", "role": "Marketing Manager"}
}
```

Update `hr_logic.py`:

```python
EMPLOYEE_NAME_TO_IDS = {
    "nagham habli": ["123"],
    "new employee": ["999"]
}
```

### Adding New Job Roles

Edit `hr_tools.py`:

```python
questions = {
    "marketing manager": [
        "What is your experience with digital marketing campaigns?",
        "How do you measure marketing ROI?",
        "Describe a successful product launch you've managed."
    ]
}
```

### Adding New Intents

1. Update `llm_parser.py` SYSTEM_PROMPT
2. Add handler function in `hr_logic.py`
3. Create corresponding tool in `hr_tools.py` (if needed)
4. Update `handle_intent()` function

---

## 🧪 Testing

### Terminal Interface

Use the terminal interface for quick testing:

```bash
python test_chat.py
```

<img width="545" height="358" alt="terminal_testing" src="https://github.com/user-attachments/assets/bcf6285e-964e-49c9-8eb7-92e5c6b5ccdb" />

### Manual Testing

Test various scenarios:
- Employee queries with unique names
- Employee queries with duplicate names
- Leave balance checks
- Interview question generation
- General HR knowledge queries
- Edge cases and error handling

---



## 🎓 Key Learning Outcomes

This project demonstrates:

✅ **Tool-Augmented LLMs** - How to extend LLM capabilities with structured tools  
✅ **Agent-Like Reasoning** - Intent detection and dynamic decision-making  
✅ **Production Architecture** - Clean separation between LLM and application logic  
✅ **State Management** - Handling multi-turn conversations  
✅ **Error Handling** - Graceful degradation and fallback strategies  
✅ **UI Integration** - Connecting AI logic to user interfaces  
✅ **Observability** - Tracing and debugging AI systems  


---

## 🙏 Acknowledgments

- **LangChain** - For the excellent LLM framework
- **Gradio** - For the intuitive UI library
- **Ollama** - For local LLM deployment
- **LangSmith** - For observability and tracing

---




---

*Last Updated: February 2026*
