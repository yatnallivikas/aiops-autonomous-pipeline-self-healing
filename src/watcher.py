import requests
import time
import subprocess
import os

from dotenv import load_dotenv


# =========================
# LOAD ENV
# =========================

load_dotenv()


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("GITHUB_OWNER")
REPO = os.getenv("GITHUB_REPO")


headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


# =========================
# TRACK LAST FAILURE
# =========================

last_run_id = None


print("\n========== WATCHER STARTED ==========\n")


while True:

    try:

        url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs"

        response = requests.get(url, headers=headers)

        runs = response.json()["workflow_runs"]


        failed_run = None

        for run in runs:

            if run["conclusion"] == "failure":

                failed_run = run
                break


        if failed_run:

            current_run_id = failed_run["id"]


            if current_run_id != last_run_id:

                print("\nNEW FAILED WORKFLOW DETECTED")

                print("Workflow:", failed_run["name"])

                last_run_id = current_run_id


                # =========================
                # FETCH LOGS
                # =========================

                print("\nFetching logs...")

                subprocess.run([
                    "python",
                    "src/agents/github_log_fetcher.py"
                ])


                # =========================
                # RUN AI ANALYSIS
                # =========================

                print("\nRunning AI analysis...")

                subprocess.run([
                    "python",
                    "src/agents/log_analyzer.py"
                ])


        else:

            print("\nNo failed workflows found")


    except Exception as e:

        print("\nERROR:", str(e))


    # =========================
    # WAIT BEFORE NEXT CHECK
    # =========================

    time.sleep(30)