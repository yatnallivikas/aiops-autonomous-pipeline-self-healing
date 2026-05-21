from strands import Agent
from strands.models.ollama import OllamaModel

from datetime import datetime

import os


# =========================
# OLLAMA MODEL
# =========================

model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen2.5:7b"
)


# =========================
# SYSTEM PROMPT
# =========================

system_prompt = """
You are an expert DevOps troubleshooting assistant.

Your job:
- Analyze CI/CD workflow failures
- Identify root cause
- Suggest remediation
- Summarize issues clearly

Rules:
- Keep responses concise
- Focus only on important failures
- Ignore unnecessary warnings
"""


# =========================
# CREATE AGENT
# =========================

agent = Agent(
    model=model,
    system_prompt=system_prompt
)


# =========================
# READ LOG FILE
# =========================

log_file = "src/logs/github_failure.log"


with open(log_file, "r", encoding="utf-8") as file:

    logs = file.read()


# =========================
# LIMIT HUGE LOGS
# =========================

logs = logs[:12000]


# =========================
# CREATE PROMPT
# =========================

prompt = f"""
Analyze the following GitHub Actions CI/CD logs.

Logs:
{logs}

Provide response in this format:

1. Root Cause
2. Suggested Fix
3. Summary
"""


# =========================
# RUN ANALYSIS
# =========================

print("\n========== ANALYZING LOGS ==========\n")

response = agent(prompt)


# =========================
# PRINT OUTPUT
# =========================

print("\n========== AI ANALYSIS ==========\n")

print(response)


# =========================
# SAVE REPORT
# =========================

os.makedirs("src/reports", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

report_file = f"src/reports/report_{timestamp}.txt"


with open(report_file, "w", encoding="utf-8") as file:

    file.write(str(response))


print("\n========== REPORT SAVED ==========\n")

print(report_file)