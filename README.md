# Flask NLP Learning Application

A Flask learning project with login/session flows and interfaces for named-entity
recognition and sentiment analysis using the ParallelDots API.

## Code guide

- `app.py`: Flask routes, sessions and rendered pages.
- `api.py`: ParallelDots NLP integration.
- `db.py`: JSON-backed account-storage helper.
- `templates/` and `static/`: page templates, CSS and JavaScript.

## Local exploration

Use a Python virtual environment and install `flask` and `paralleldots`.
Review the external API configuration in `api.py` before running `python app.py`.
An external API account and local configuration are required for NLP requests.

## Project status

This is a learning demo, not a production authentication system. The current
account and password-reset flows require security work, and the session key must
be configured securely before any deployment. Use synthetic accounts only;
do not use real passwords or expose the development server publicly. Some routes
reference templates that still need implementation.
