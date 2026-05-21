import requests
import zipfile
import io
import os

from dotenv import load_dotenv


# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("GITHUB_OWNER")
REPO = os.getenv("GITHUB_REPO")


# =========================
# DEBUG ENV VARIABLES
# =========================

print("\n========== ENV VARIABLES ==========")

print("OWNER:", OWNER)
print("REPO:", REPO)

if GITHUB_TOKEN:
    print("TOKEN LOADED SUCCESSFULLY")
else:
    print("TOKEN NOT FOUND")


# =========================
# GITHUB API HEADERS
# =========================

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


# =========================
# FETCH WORKFLOW RUNS
# =========================

url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs"

print("\nFetching workflow runs...")
print(url)

response = requests.get(url, headers=headers)


# =========================
# DEBUG RESPONSE
# =========================

print("\n========== API RESPONSE ==========")

print("Status Code:", response.status_code)

try:
    response_json = response.json()
    print(response_json)

except Exception as e:
    print("Failed to parse JSON:", str(e))
    exit()


# =========================
# VALIDATE RESPONSE
# =========================

if "workflow_runs" not in response_json:

    print("\nERROR: workflow_runs key not found")
    print("Possible reasons:")
    print("- Invalid GitHub token")
    print("- Wrong repository name")
    print("- Wrong owner name")
    print("- Repository has no workflows yet")

    exit()


runs = response_json["workflow_runs"]


# =========================
# FIND FAILED WORKFLOW
# =========================

failed_run = None

for run in runs:

    if run["conclusion"] == "failure":

        failed_run = run
        break


# =========================
# VALIDATE FAILED RUN
# =========================

if not failed_run:

    print("\nNo failed workflow runs found")
    exit()


print("\n========== FAILED WORKFLOW ==========")

print("Workflow Name:", failed_run["name"])
print("Run ID:", failed_run["id"])


# =========================
# DOWNLOAD LOGS
# =========================

run_id = failed_run["id"]

logs_url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs/{run_id}/logs"

print("\nDownloading workflow logs...")

logs_response = requests.get(logs_url, headers=headers)


# =========================
# VALIDATE LOG DOWNLOAD
# =========================

if logs_response.status_code != 200:

    print("\nFailed to download logs")
    print("Status:", logs_response.status_code)

    exit()


# =========================
# EXTRACT ZIP CONTENT
# =========================

zip_content = zipfile.ZipFile(io.BytesIO(logs_response.content))


# =========================
# READ ALL LOG FILES
# =========================

all_logs = ""

for file_name in zip_content.namelist():

    print("\nReading:", file_name)

    with zip_content.open(file_name) as log_file:

        content = log_file.read().decode("utf-8")

        all_logs += "\n\n"
        all_logs += f"===== {file_name} =====\n"
        all_logs += content


# =========================
# CREATE LOG DIRECTORY
# =========================

os.makedirs("src/logs", exist_ok=True)


# =========================
# SAVE LOGS
# =========================

log_file_path = "src/logs/github_failure.log"

with open(log_file_path, "w", encoding="utf-8") as file:

    file.write(all_logs)


# =========================
# SUCCESS MESSAGE
# =========================

print("\n========== SUCCESS ==========")

print("Logs downloaded successfully")
print(f"Saved to: {log_file_path}")