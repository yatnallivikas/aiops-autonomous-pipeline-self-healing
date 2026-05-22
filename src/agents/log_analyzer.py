import os
import ollama
from datetime import datetime

LOGS_DIR = "src/logs"
REPORTS_DIR = "src/reports"

os.makedirs(REPORTS_DIR, exist_ok=True)

all_logs = ""

for root, dirs, files in os.walk(LOGS_DIR):
    for file in files:
        if file.endswith(".txt"):

            filepath = os.path.join(root, file)

            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                all_logs += f.read()
                all_logs += "\n\n"

prompt = f"""
Analyze the following GitHub Actions workflow failure logs.

Provide:
1. Root Cause
2. Suggested Fix
3. Summary

Logs:
{all_logs}
"""

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

analysis = response["message"]["content"]

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

report_file = f"{REPORTS_DIR}/report_{timestamp}.txt"

with open(report_file, "w", encoding="utf-8") as f:
    f.write(analysis)

print("\nAI ANALYSIS REPORT\n")
print(analysis)

print(f"\nReport saved to: {report_file}")