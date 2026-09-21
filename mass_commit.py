import os
import time


def pure_python_mass_commit():
    try:
        # 1. Dynamically load GitPython
        try:
            from mass_commit import Repo
        except ImportError:
            print("Installing required git library...")
            import subprocess
            subprocess.run(["pip", "install", "GitPython"], capture_output=True)
            from mass_commit import Repo

        # 2. Identify repository paths
        repo_path = os.getcwd()
        repo = Repo(repo_path)
        dummy_file = os.path.join(repo_path, "activity_log.txt")

        print("Starting 100 local commits...")

        # 3. Create 100 local commits
        for i in range(1, 101):
            with open(dummy_file, "a") as f:
                f.write(f"Commit updates: Iteration {i}\n")

            repo.index.add([dummy_file])
            commit = repo.index.commit(f"Auto-commit patch #{i}")
            print(f"Created commit {i}/100 - SHA: {commit.hexsha[:7]}")
            time.sleep(0.05)

        # 4. Push directly to the master branch
        print("Pushing all 100 commits to GitHub origin (master)...")
        origin = repo.remote(name='origin')

        # Explicitly push the local master branch to remote master
        origin.push(refspec='master:master')
        print("🚀 Successfully pushed 100 commits to the master branch on GitHub!")

    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        print("If it says 'Invalid git repository', open your PyCharm terminal and run: git init")


if __name__ == "__main__":
    pure_python_mass_commit()
