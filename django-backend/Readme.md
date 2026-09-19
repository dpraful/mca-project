# Healthcare Management Django Project

This is a Django-based healthcare management system for hospitals, field workers, disease tracking, alerts, vaccination campaigns, surveys, and AI-based disease prediction.

This project is designed to be easy to run on a new PC for beginners.

## Project Overview

- Project name: HealthcareProject
- App name: HelathApp
- Backend: Django
- Database: SQLite (default)
- Frontend templates: Django HTML templates
- Static files: CSS, JS, images
- Extra libraries: pandas, matplotlib, statsmodels, requests, python-dotenv, django-cors-headers

## Prerequisites

Before running this project, make sure you have installed:

- Python 3.12 or 3.13 recommended
- Git
- VS Code (optional but recommended)
- A browser such as Chrome or Edge

> This project is currently working with Django 6.1.1, so Python 3.12 or 3.13 is the safest choice.

## 1. Clone the Project

Open PowerShell or Command Prompt and run:

```powershell
git clone <your-repository-url>
cd django-backend
```

## 2. Create a Virtual Environment

Inside the project folder, create a virtual environment:

```powershell
py -3.12 -m venv .venv
```

Then activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again:

```powershell
.venv\Scripts\activate.bat
```

## 3. Install Dependencies

Install all required packages:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If `requirements.txt` is not present, install the required packages manually:

```powershell
pip install Django==6.1.1 python-dotenv==1.2.3 django-cors-headers==4.9.0 pillow==12.3.0 numpy==2.5.3 pandas==3.0.6 matplotlib==3.11.2 statsmodels==0.15.0 requests==2.34.2
```

## 4. Set Up Environment Variables

This project reads environment variables from a `.env` file.

Create a file named `.env` in the project root based on `.env.example`:

```env
DJANGO_SECRET_KEY=change-this-to-a-random-secret-key
GROQ_API_KEY=
```

You can copy the example file:

```powershell
copy .env.example .env
```

> If you do not have a Groq API key, the app may still start, but some AI-based features may not work properly.

## 5. Apply Database Migrations

Run:

```powershell
python manage.py migrate
```

This creates the SQLite database file (`db.sqlite3`) if it does not already exist.

## 6. Create an Admin User (Optional but Recommended)

Create a superuser account to access the Django admin panel:

```powershell
python manage.py createsuperuser
```

Follow the prompt and enter:

- Username
- Email (optional)
- Password

Then go to:

```text
http://127.0.0.1:8000/admin/
```

## 7. Run the Server

Start the development server:

```powershell
python manage.py runserver
```

Open in your browser:

```text
http://127.0.0.1:8000/
```

## Project Structure

```text
django-backend/
├── HelathcareProject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── HelathApp/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── manage.py
├── requirements.txt
├── db.sqlite3
├── .env
├── media/
└── static/
```

## Common Issues and Fixes

### Problem: `ModuleNotFoundError`

If a package is missing, install it again:

```powershell
pip install -r requirements.txt
```

### Problem: `django.core.exceptions.ImproperlyConfigured`

Check whether your `.env` file exists and contains the proper values.

### Problem: `python` command does not work

Try:

```powershell
py
```

or use:

```powershell
py -3.12
```

### Problem: migrations fail

Run:

```powershell
python manage.py makemigrations HelathApp
python manage.py migrate
```

## Useful Commands

```powershell
python manage.py check
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```

## Development Notes

- The project uses SQLite for local development.
- Static files are stored in the `static/` directory.
- Uploaded media files are saved in the `media/` directory.
- The app uses HTML templates from the `HelathApp/templates` folder.

## Final Step

Once the server is running, you can open the app in your browser and start using the healthcare dashboard and management panels.

If you are a beginner, the most important commands are:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Good luck with the project!
