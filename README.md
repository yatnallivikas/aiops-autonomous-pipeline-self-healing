# GitHub Actions AI Monitor

An autonomous AI-powered CI/CD failure monitoring and troubleshooting system built using:

- Python
- GitHub Actions
- GitHub REST API
- Ollama
- Qwen2.5
- Local LLM inference

This project continuously monitors GitHub Actions workflow failures, automatically fetches failure logs, analyzes them using a local LLM, and generates AI-powered remediation reports.

---

# Overall Workflow

```text
Developer Pushes Code
          ↓
GitHub Actions Workflow Runs
          ↓
Workflow Fails
          ↓
Watcher Detects Failure Automatically
          ↓
GitHub API Fetches Workflow Logs
          ↓
Logs Downloaded Locally
          ↓
AI Agent Analyzes Failure
          ↓
Root Cause Generated
          ↓
Suggested Fix Generated
          ↓
AI Report Saved Automatically
```

---

# Project Architecture

```text
GitHub Actions
        ↓
GitHub REST API
        ↓
Watcher Service
        ↓
Log Fetcher
        ↓
AI Log Analyzer
        ↓
Ollama + Qwen2.5
        ↓
Generated Reports
```

---

# Features

- Autonomous GitHub Actions failure monitoring
- Automatic failed workflow detection
- GitHub Actions log extraction
- Local AI-powered troubleshooting
- Root cause analysis
- Suggested remediation generation
- Continuous polling-based monitoring
- Fully local LLM inference
- No paid APIs required

---

# Repository Structure

```text
github-actions-ai-monitor/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── src/
│   ├── agents/
│   │   ├── github_log_fetcher.py
│   │   └── log_analyzer.py
│   │
│   ├── logs/
│   │
│   ├── reports/
│   │
│   ├── watcher.py
│   │
│   └── app.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# File Descriptions

## `src/app.py`

Sample Python application intentionally designed to fail GitHub Actions workflows for testing AI analysis pipelines.

Example:
```python
import numpy
```

without installing dependencies.

---

## `src/watcher.py`

Autonomous monitoring service.

Responsibilities:
- Continuously checks GitHub Actions workflow runs
- Detects failed workflows
- Triggers log fetching
- Triggers AI analysis automatically
- Runs continuously in polling mode

---

## `src/agents/github_log_fetcher.py`

GitHub Actions log ingestion service.

Responsibilities:
- Connects to GitHub REST API
- Fetches failed workflow runs
- Downloads workflow logs
- Extracts ZIP log archives
- Saves logs locally

---

## `src/agents/log_analyzer.py`

AI-powered troubleshooting engine.

Responsibilities:
- Reads GitHub Actions logs
- Sends logs to local LLM
- Generates:
  - Root Cause
  - Suggested Fix
  - Failure Summary
- Saves AI reports automatically

---

## `src/logs/`

Stores downloaded GitHub Actions workflow logs.

Example:
```text
github_failure.log
```

---

## `src/reports/`

Stores AI-generated troubleshooting reports.

Example:
```text
report_20260521_120755.txt
```

---

## `.github/workflows/python-ci.yml`

GitHub Actions CI workflow.

Automatically runs when code is pushed to GitHub.

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core automation |
| GitHub Actions | CI/CD workflows |
| GitHub REST API | Workflow log retrieval |
| Ollama | Local LLM runtime |
| Qwen2.5 | Local AI model |
| Requests | API communication |
| dotenv | Environment variable management |

---

# Setup Instructions

---

# 1. Clone Repository

```bash
git clone https://github.com/yatnallivikas/github-actions-ai-monitor.git
```

```bash
cd github-actions-ai-monitor
```

---

# 2. Create Virtual Environment

```bash
python -m venv venv
```

---

# 3. Activate Virtual Environment

## Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 4. Install Dependencies

```bash
pip install strands-agents
```

```bash
pip install ollama
```

```bash
pip install requests python-dotenv
```

---

# 5. Install Ollama

Download and install:

https://ollama.com/download

---

# 6. Pull Qwen Model

```bash
ollama pull qwen2.5:7b
```

---

# 7. Create `.env`

Create a `.env` file in project root.

```env
GITHUB_TOKEN=your_github_token
GITHUB_OWNER=your_github_username
GITHUB_REPO=your_repository_name
```

---

# 8. Start Ollama

```bash
ollama serve
```

---

# 9. Start Autonomous Watcher

```bash
python src/watcher.py
```

---

# How To Trigger Workflow Failures

Modify:

```text
src/app.py
```

Example:

```python
import tensorflow
```

without installing the dependency.

Then push changes:

```bash
git add .
```

```bash
git commit -m "Trigger workflow failure"
```

```bash
git push
```

GitHub Actions workflow will fail automatically.

Watcher will:
- detect failure
- fetch logs
- analyze logs
- generate AI report

---

# Example AI Output

```text
Root Cause:
Missing dependency: tensorflow

Suggested Fix:
Install tensorflow package or add it to requirements.txt

Summary:
GitHub Actions workflow failed because the tensorflow module was unavailable during execution.
```

---

# Important Commands Used

## Git Commands

```bash
git init
git add .
git commit -m "message"
git push
git push --force
git remote add origin <repo_url>
git remote remove origin
git status
```

---

## Python Commands

```bash
python -m venv venv
python src/watcher.py
python src/agents/log_analyzer.py
python src/agents/github_log_fetcher.py
```

---

## Ollama Commands

```bash
ollama serve
ollama pull qwen2.5:7b
ollama ps
```

---

# Future Improvements

- Temporal workflow orchestration
- GitHub webhook integration
- Slack notifications
- Jira ticket automation
- AI severity scoring
- Root cause categorization
- Kubernetes log analysis
- Docker failure analysis
- Streamlit dashboard
- Multi-agent architecture
- Vector memory integration
- Cloud deployment support

---

# Why This Project Matters

Most AI projects focus only on prompts and chatbots.

This project demonstrates:
- AI workflow automation
- DevOps observability
- Autonomous monitoring
- Local LLM orchestration
- Event-driven troubleshooting
- Real-world CI/CD analysis

This is a practical AI + DevOps systems engineering project rather than a simple LLM demo.

---

# License

MIT License
