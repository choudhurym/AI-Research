import subprocess
import sys

def run_git_command(command):
    """Execute a git command and return the output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd="."
        )
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return None, str(e), 1

def debug_git_repo():
    """Debug git repository status and issues."""
    print("=== Git Repository Debug ===\n")
    
    # Check git status
    print("1. Repository Status:")
    stdout, stderr, code = run_git_command("git status")
    print(stdout if code == 0 else f"Error: {stderr}")
    
    # Check recent commits
    print("\n2. Recent Commits:")
    stdout, stderr, code = run_git_command("git log --oneline -10")
    print(stdout if code == 0 else f"Error: {stderr}")
    
    # Check branches
    print("\n3. Branches:")
    stdout, stderr, code = run_git_command("git branch -a")
    print(stdout if code == 0 else f"Error: {stderr}")
    
    # Check remote status
    print("\n4. Remote Status:")
    stdout, stderr, code = run_git_command("git remote -v")
    print(stdout if code == 0 else f"Error: {stderr}")
    
    # Check for uncommitted changes
    print("\n5. Uncommitted Changes:")
    stdout, stderr, code = run_git_command("git diff --stat")
    print(stdout if code == 0 else "No changes or error")

if __name__ == "__main__":
    debug_git_repo()