# TaskBoard API — CourseCompletionCert Demo Submission

A sample final project for a CourseCompletionCert video demonstration.

## Assignment
Build a small REST API for managing tasks. It should demonstrate:
1. Working endpoints.
2. Input validation and predictable errors.
3. Setup documentation and automated tests.

## Implemented
- `GET /health` — health check.
- `GET /tasks` — list tasks.
- `POST /tasks` — create a task; title is required and cannot be blank.
- JSON error responses for invalid input.
- Unit tests for success and validation paths.

## Run locally
Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API runs at `http://127.0.0.1:5000`.

## Try it
- Open `http://127.0.0.1:5000/health`
- Open `http://127.0.0.1:5000/tasks`
- Send `POST /tasks` with JSON body `{"title":"Prepare demo"}`.
- Send `POST /tasks` with JSON body `{"title":"   "}`; expected HTTP 400.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Submit to CourseCompletionCert
Upload this folder to a public GitHub repository, then submit the actual repository URL through the deployed course UI. This API does not itself connect to a blockchain. Do not claim the contract evaluation or certificate succeeded until the deployed app displays a confirmed result.

## Safety
Use only a test-network wallet and test tokens if a wallet is required. Never enter a seed phrase or private key into a website or test file.
