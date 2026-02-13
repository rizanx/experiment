# Experiment Project

Experimental purpose

Minimal experiment scaffold: Python (FastAPI) backend + static frontend.

Quick start (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```

Open the frontend by opening frontend/index.html in your browser and use the UI to call the API.

Tests:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
pytest -q
```

Files of interest:
- backend/app/main.py
- frontend/index.html
- backend/requirements.txt
