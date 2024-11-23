# Gamble Search
Like Binary search, except it picks a random pivot instead of splitting the array in the middle.

# Git Hooks Setup

This repository uses Git hooks to ensure code quality by running tests before each push.

After cloning the repository, run:
```bash
python install_hooks.py
```

This will install a pre-push hook that runs your tests automatically before each push. If any tests fail, the push will be blocked.

## Running Tests Manually

You can run the tests manually at any time by running this command from the root directory:
```bash
pytest
```

## Requirements

- Python 3.6 or higher
- pytest (`pip install pytest`)