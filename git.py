import subprocess
import os
import time

REPO_PATH = os.getcwd()


def run_git_command(command):
    """Executes a Git command in the terminal."""
    result = subprocess.run(command, cwd=REPO_PATH, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        raise Exception(result.stderr.strip())
    return result.stdout.strip()


def mass_commit_loop():
    try:
        os.chdir(REPO_PATH)
        dummy_file = "activity_log.txt"

        # Loop exactly 100 times
        for i in range(1, 101):
            # 1. Modify the file so Git detects a change
            with open(dummy_file, "a") as f:
                f.write(f"Commit updates: Iteration {i}\n")

            # 2. Stage the modified file
            run_git_command(f"git add {dummy_file}")

            # 3. Create a unique commit message
            commit_message = f"Auto-commit patch #{i}"
            run_git_command(f'git commit -m "{commit_message}"')
            print(f"Created commit {i}/100")

            # Optional: Short pause to avoid overwhelming the system
            time.sleep(0.1)

        # 4. Push all 100 commits to GitHub at once
        print("Pushing all 100 commits to GitHub...")
        run_git_command("git push origin ma")  # Change 'main' to your branch name if different
        print("Successfully pushed 100 commits!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    mass_commit_loop()
