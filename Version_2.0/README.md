# Gym Management System — Version 2.0

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)]()
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15%2B-green)]()
[![SQLite](https://img.shields.io/badge/SQLite-stable-lightgrey)]()

A production-ready desktop Gym Management application with a PyQt5 GUI, local SQLite persistence, analytics and management modules for members, trainers, equipment, payments and workouts. This README documents how Version 2.0 is organized, how to run it locally, and where to look when extending or packaging the app.

## Key highlights

- Modern PyQt5 GUI with modular screens: login, dashboard, members, trainers, equipment, payments, plans and analytics.
- Single-file SQLite database (gym.db) for easy offline use and distribution.
- Built-in analytics and metrics modules (charts via matplotlib) to visualize member trends and payments.
- Install scripts for Windows/macOS/Linux (install.bat, install.sh) and a small requirements.txt.

## Stack
- Language(s): Python 3.7+
- Framework / runtime: PyQt5 (desktop GUI)
- Notable libraries: PyQt5, matplotlib, sqlite3 (stdlib)

## What’s in this version (v2.0)
- Full GUI application (replaces the CLI v1.0)
- Database migrations and default data seeding
- Member body metrics and workout plan management
- Payment recording with simple reporting
- Equipment tracking and trainer management
- Simple dashboard with charts and metrics

## Repository — top-level (important files)

```text
Version_2.0/
  main.py           # application entrypoint - starts Login and Dashboard
  login.py          # login window and authentication flow
  dashboard.py      # main dashboard UI and navigation
  database.py       # SQLite wrapper: creates tables & provides CRUD helpers
  members.py        # member UI & controller code
  trainers.py       # trainer UI & controller code
  equipment.py      # equipment UI & controller code
  payments.py       # payment UI & controller code
  memberships.py    # membership plans UI & helpers
  plans.py          # workout-plan UI & helpers
  metrics.py        # metrics collection and helper functions
  analytics.py      # analytics and matplotlib charts for dashboard
  gym.db            # local SQLite database (example / dev DB)
  requirements.txt  # minimal Python dependencies
  install.sh        # POSIX install helper
  install.bat       # Windows install helper
  docs/             # (optional) extended docs and screenshots
Version_1.0/
  Gym Management.py # legacy CLI version
  README.md         # v1.0 documentation
README.md           # project-level overview (legacy)
```

How it fits together: main.py initializes the QApplication and shows the Login window. On successful login the Dashboard module is opened which routes to feature modules. database.py centralizes schema creation and common CRUD helpers used by feature modules (members, trainers, payments, equipment, workout plans). analytics.py and metrics.py gather and plot data for the Dashboard.

## Database (schema summary)
Version 2.0 uses SQLite with the following primary tables (see Version_2.0/database.py for full SQL):
- memberships (membership_id, type, fee, duration)
- trainers (trainer_id, name, specialization, phone, email, salary)
- members (member_id, name, age, gender, phone, email, address, join_date, membership_id, trainer_id)
- body_metrics (record_id, member_id, date, weight, height, bmi)
- workout_plans (plan_id, member_id, trainer_id, goal, level, duration)
- payments (payment_id, member_id, date, amount, payment_mode)
- equipment (equipment_id, name, type, purchase_date, condition)

The database file is Version_2.0/gym.db by default. The application auto-creates tables and inserts default membership plans on first run.

## Quick start (development)

1. Clone

```bash
git clone https://github.com/Mithun0017/Gym-Management-System.git
cd Gym-Management-System/Version_2.0
```

2. Create a virtual environment and install

```bash
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows (PowerShell)
# .\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

3. (Optional) Run the installer script to perform platform-specific steps

- macOS / Linux
  ./install.sh
- Windows
  install.bat

4. Run the app

```bash
python main.py
```

The app will create (or open) Version_2.0/gym.db and seed default membership plans.

## Packaging suggestions
- For a single-file Windows executable use PyInstaller: pip install pyinstaller; pyinstaller --onefile --windowed main.py and include the gym.db and resource files as data.
- Test the packaged binary on a clean VM to ensure the database and matplotlib backends work correctly.

## Developer notes — where to look
- main.py — application lifecycle and Qt application setup
- login.py — login logic and signal to open dashboard
- dashboard.py — navigation and chart placeholders
- database.py — ALL schema creation and higher-level CRUD helpers; change here to alter schema
- analytics.py / metrics.py — chart generation using matplotlib; adapt to add new metrics
- members.py, trainers.py, equipment.py, payments.py, memberships.py, plans.py — UI controllers and dialogs for each domain

If you add new tables, update database.create_tables() and provide a migration path or drop/create logic for development.

## Configuration & environment
- The app uses a local SQLite file by default. To use a different file path, pass the db_name when instantiating Database (see database.py).
- No external secrets are required for v2.0.

## Screenshots / docs
Add screenshots into Version_2.0/docs and reference them here. Example markdown to add:

```markdown
![Dashboard](docs/screenshots/dashboard.png)
```

## Testing
- There are no automated tests included yet. Recommended: add pytest-based unit tests for database.py and core helpers. Mock SQLite connections using temporary files for isolation.

## Roadmap & improvements
- Add user roles & permission levels (admin, staff)
- Add automated backups & export (CSV/PDF) for reports
- Add import/export for members (CSV)
- Add unit/integration tests and CI workflow
- Add internationalization (i18n) for multi-language support
- Consider switching charts to a web-based dashboard (Dash / Plotly) for richer visualizations

## Contributing
- Fork > branch > PR
- Keep changes small and focused. If changing DB schema, include a migration plan and update database.py.

## License
Include your preferred license (e.g., MIT). Add a LICENSE file to the repository.

## Contact
Mithun — mithun200617@gmail.com — https://github.com/Mithun0017

---

Notes: I reviewed the Version_2.0 source (main.py, database.py, analytics.py and feature modules) and used those files to create this README. If you want, I can:
- add screenshots and example images under Version_2.0/docs,
- create a basic PyInstaller spec and packaging script,
- add a CONTRIBUTING.md and LICENSE file.
