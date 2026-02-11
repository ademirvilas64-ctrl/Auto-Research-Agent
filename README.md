# Auto Research Agent

Automated Industry Research Pipeline using GitHub Actions and RSSHub.

## How it works
1. **GitHub Actions** starts daily.
2. Spins up a local **RSSHub** instance.
3. Runs `main.py`.
4. `main.py` fetches articles -> Calls AI -> Saves results.

## Setup
1. Push this code to GitHub.
2. Go to **Settings -> Secrets and variables -> Actions**.
3. Add `GEMINI_API_KEY`.
