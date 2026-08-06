# Contributing to AI Trading OS

Thank you for your interest in contributing!

## Development Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Trading-OS.git
```

Go to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```

---

## Coding Standards

- Follow PEP8
- Use type hints
- Write docstrings
- Add tests for new features
- Keep functions small and focused

---

## Pull Requests

Before opening a Pull Request:

- Ensure all tests pass
- Update documentation if required
- Keep commits meaningful
- Describe the purpose of the PR

Thank you for contributing!