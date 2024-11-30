import os
import stat
import subprocess
from pathlib import Path


def get_git_root():
    """Get the git repository root directory."""
    try:
        root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
        return root.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        raise RuntimeError("Not a git repository")


def write_pre_push_hook():
    """Write the pre-push hook script to .git/hooks directory."""
    pre_push_content = '''#!/usr/bin/env python
import subprocess
import sys
import os

def run_tests():
    """Run pytest and return True if all tests pass."""
    print("Running pytest before push...")
    try:
        # Store current directory
        current_dir = os.getcwd()

        # Change to git root directory
        git_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'],
                                         universal_newlines=True).strip()
        os.chdir(git_root)

        # Run pytest
        result = subprocess.run('pytest -m "not benchmark"', 
                              shell=True,
                              capture_output=True,
                              text=True)

        # Change back to original directory
        os.chdir(current_dir)

        if result.returncode != 0:
            print("❌ Tests failed. Push rejected.")
            print("Test output:")
            print(result.stdout)
            print(result.stderr)
            return False

        print("✅ All tests passed. Proceeding with push.")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error running tests: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == '__main__':
    if not run_tests():
        sys.exit(1)
    sys.exit(0)
'''

    git_root = Path(get_git_root())
    hooks_dir = git_root / '.git' / 'hooks'
    hooks_dir.mkdir(exist_ok=True)

    pre_push_path = hooks_dir / 'pre-push'
    pre_push_path.write_text(pre_push_content, encoding='utf-8')

    # Make the hook executable on Unix-like systems
    if os.name != 'nt':  # not Windows
        st = os.stat(pre_push_path)
        os.chmod(pre_push_path, st.st_mode | stat.S_IEXEC)


def main():
    try:
        write_pre_push_hook()
        print("✅ Git pre-push hook installed successfully!")
        print("Pre-push hook will run pytest before each push.")

    except Exception as e:
        print(f"❌ Error installing hook: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()