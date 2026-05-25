# GitHub Actions AI Monitor

An autonomous AI-powered CI/CD failure monitoring and troubleshooting system built using:

- Python
- GitHub Actions
- GitHub REST API
- Ollama
- Qwen2.5
- Self-hosted GitHub Runners
- Local LLM inference

This project continuously monitors GitHub Actions workflow failures, automatically fetches workflow logs, analyzes failures using a locally running LLM, and generates AI-powered remediation reports without using paid cloud AI APIs.

---

# What This Project Does exactly

This system creates a fully autonomous AI debugging pipeline for CI/CD workflows.

Whenever a GitHub Actions workflow fails:

- The failure is automatically detected
- Logs are downloaded automatically
- AI analyzes the failure
- Root cause is generated
- Suggested fixes are generated
- AI troubleshooting reports are saved automatically

All AI inference happens locally using Ollama + Qwen2.5.

---

# Overall Workflow

```text
Developer Pushes Code
          ↓
GitHub Actions Workflow Runs
          ↓
Workflow Fails
          ↓
workflow_run Event Triggered
          ↓
AI Failure Monitor Starts Automatically
          ↓
GitHub API Fetches Workflow Logs
          ↓
Logs Downloaded Locally
          ↓
Ollama Invoked
          ↓
Qwen2.5 Analyzes Failure
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
workflow_run Trigger
        ↓
Self-hosted GitHub Runner
        ↓
GitHub REST API
        ↓
Log Fetcher
        ↓
AI Log Analyzer
        ↓
Ollama
        ↓
Qwen2.5
        ↓
Generated Reports
```

---

# Features

- Autonomous GitHub Actions failure monitoring
- Event-driven AI workflow automation
- Automatic failed workflow detection
- GitHub-native workflow triggers
- GitHub Actions log extraction
- Local AI-powered troubleshooting
- Root cause analysis
- Suggested remediation generation
- Self-hosted GitHub Actions runner integration
- Fully local LLM inference
- No paid APIs required
- Real-time AI debugging pipeline

---

# Repository Structure

```text
github-actions-ai-monitor/
│
├── .github/
│   └── workflows/
│       ├── python-ci.yml
│       └── ai-monitor.yml
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
│   └── app.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# File Descriptions

---

## `src/app.py`

Sample Python application intentionally designed to fail GitHub Actions workflows for testing AI analysis pipelines.

Example:

```python
import tensorflow
```

without installing dependencies.

This intentionally triggers CI/CD failures so the AI monitoring system can analyze them.

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
- Sends logs to Ollama
- Uses Qwen2.5 for analysis
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
report_20260522_124500.txt
```

---

## `.github/workflows/python-ci.yml`

Main CI workflow.

Responsibilities:

- Runs on every push
- Executes application
- Intentionally fails for testing AI analysis pipeline

---

## `.github/workflows/ai-monitor.yml`

Autonomous AI monitoring workflow.

Responsibilities:

- Triggered automatically using `workflow_run`
- Detects failed workflows
- Fetches workflow logs
- Runs AI analysis
- Uploads AI-generated reports

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core automation |
| GitHub Actions | CI/CD workflows |
| workflow_run | Event-driven automation |
| Self-hosted Runner | Local workflow execution |
| GitHub REST API | Workflow log retrieval |
| Ollama | Local LLM runtime |
| Qwen2.5 | Local AI model |
| Requests | API communication |
| dotenv | Environment variable management |

---

# Why Self-hosted Runner Was Used

GitHub-hosted runners cannot access locally running Ollama models.

To enable local AI inference inside GitHub Actions workflows, a self-hosted GitHub runner was configured.

This allows:

```text
GitHub Actions
        ↓
Runs directly on local machine
        ↓
Accesses Ollama locally
        ↓
Runs Qwen2.5 inference
```

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
pip install -r requirements.txt
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

# 7. Start Ollama

```bash
ollama serve
```

---

# 8. Configure Self-hosted GitHub Runner

Go to:

```text
GitHub Repository
→ Settings
→ Actions
→ Runners
→ New Self-hosted Runner
```

Choose:

- Windows
- x64

Run all setup commands provided by GitHub.

Start runner:

```powershell
.\run.cmd
```

---

# 9. Create `.env`

Create a `.env` file in project root.

```env
GITHUB_TOKEN=your_github_token
```

---

# 10. Push Code

```bash
git add .
```

```bash
git commit -m "Initial AI monitoring setup"
```

```bash
git push origin main
```

---

# How Workflow Failure Detection Works

The project uses GitHub Actions `workflow_run` event trigger.

Example:

```yaml
on:
  workflow_run:
    workflows: ["Python CI"]
    types:
      - completed
```

This automatically triggers AI analysis whenever the CI workflow completes.

If workflow status is:

```yaml
failure
```

AI analysis starts automatically.

---

# Example Workflow Failure

Example failure:

```python
import tensorflow
```

without installing dependency.

This causes:

```text
ModuleNotFoundError
```

which triggers the AI monitoring pipeline.

---

# Example AI Output

```text
Root Cause:
Missing dependency tensorflow

Suggested Fix:
Install tensorflow package or add it to requirements.txt

Summary:
GitHub Actions workflow failed because tensorflow module was unavailable during execution.
```

---

# Where AI Reports Are Stored

AI-generated reports are saved in:

```text
src/reports/
```

and uploaded as GitHub Actions artifacts automatically.

---

# Important Commands Used

---

## Git Commands

```bash
git init
git add .
git commit -m "message"
git push
git pull --rebase
git status
```

---

## Python Commands

```bash
python src/app.py
python src/agents/log_analyzer.py
python src/agents/github_log_fetcher.py
```

---

## Ollama Commands

```bash
ollama serve
ollama pull qwen2.5:7b
ollama list
```

---

## GitHub Runner Commands

```powershell
cd C:\actions-runner
.\run.cmd
```

---

# Future Improvements

- Slack notifications
- Jira ticket automation
- AI severity scoring
- Root cause categorization
- Kubernetes log analysis
- Docker failure analysis
- Multi-agent AI workflows
- Streamlit dashboard
- Vector memory integration
- Historical failure analytics
- Automatic PR generation
- Self-healing pipelines

---

# Why This Project Matters

Most AI projects focus only on prompts and chatbots.

This project demonstrates:

- AI workflow automation
- Autonomous CI/CD monitoring
- Local LLM orchestration
- Event-driven troubleshooting
- AI-powered DevOps automation
- Real-world AIOps architecture
- Self-hosted AI infrastructure
- Intelligent failure remediation

This is a practical AI + DevOps systems engineering project rather than a simple LLM demo.

---

# Final Outcome

This project successfully demonstrates:

```text
GitHub Actions
        ↓
Self-hosted Runner
        ↓
Ollama
        ↓
Qwen2.5
        ↓
Autonomous AI Failure Analysis
```

using completely local AI inference without paid cloud APIs.

---

# License

MIT License
