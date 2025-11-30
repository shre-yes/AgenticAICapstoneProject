# 🤖 The F.A.I.R. Trading Advisor Agent

F.A.I.R. stands for **Financial Analysis & Integrated Risk**. This is a multi-agent system designed to provide comprehensive, risk-adjusted financial advice by simulating a human advisory team's workflow, including technical, fundamental, risk, and psychological analysis.

## 🚀 Key Features

*   **Structured Advisory Workflow**: Follows a rigorous, multi-step process: Data → Strategy → Execution → Risk → Behavioral.
*   **Integrated Risk Management**: Uses a dedicated Risk Analyst to enforce position sizing and stop-loss logic.
*   **Behavioral Filter**: Includes a Behavioral Analyst to warn against market mania (Fear/Greed) and user-specific cognitive biases.
*   **Secure Configuration**: Uses environment variables to protect sensitive API keys.

## 🛠️ Project Structure

This project uses a modular design for clarity and maintainability.

```
.
├── .gitignore          # Tells Git what to ignore (.env, .venv, etc.)
├── requirements.txt    # List of all Python dependencies
├── .venv/              # (Local - Created by user) Virtual Environment
└── trading_advisor/
    ├── __init__.py     # Package initialization
    ├── .env.example    # Required configuration template (PUBLIC)
    ├── .env            # Private configuration file (LOCAL & IGNORED)
    ├── agent.py        # Core orchestration logic (the Coordinator)
    └── prompt.py       # Contains all system prompts (DA_PROMPT, BP_PROMPT, etc.)
```

## ⚙️ Setup and Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone [YOUR_REPOSITORY_URL_HERE]
cd [project-folder-name]
```

### 2. Create and Activate Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

```bash
# Create the environment
python -m venv .venv

# Activate the environment (Linux/macOS)
source .venv/bin/activate

# Activate the environment (Windows)
.\.venv\Scripts\activate
```

### 3. Install Dependencies

Install all necessary Python packages (like `requests`, `python-dotenv`, etc.):

```bash
pip install -r requirements.txt
```

### 4. Configuration (API Keys) 🔑

This agent requires access to external data sources.

**Duplicate the Template**: Copy the provided configuration template and rename it to the private file that Git ignores:

```bash
cp trading_advisor/.env.example trading_advisor/.env
```

**Add Your Keys**: Open the newly created `trading_advisor/.env` file and replace the placeholder values with your actual API keys.

Example of required variables:

```ini
# Example: Replace with your actual key
GOOGLE_SEARCH_API_KEY="AIzaSy...XYZ123" 
# Add any other required keys here (e.g., BROKER_API_KEY)