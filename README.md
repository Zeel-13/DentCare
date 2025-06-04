
# 🦷 DentCare

**DentCare** is a responsive dental clinic website featuring an intuitive appointment booking system that allows patients to schedule visits online. The platform includes automated email confirmations for seamless communication, ensuring patients receive instant updates. The site is designed for ease of use, improving both the clinic's efficiency and patient experience.

## 🛠 Tech Stack

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript

- **Backend:**
  - Python 3.x
  - Django 3.x

- **Database:**
  - SQLite3 (default for Django projects)

- **Others:**
  - Bootstrap (for responsive design)
  - Django's built-in authentication system

## 🚀 Getting Started

Follow these steps to set up the DentCare project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Git

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Zeel-13/DentCare.git
   cd DentCare
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (for Admin Access):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/` in your web browser.

## 🔧 Configuration

- **Database Settings:**
  - Located in `DentCare/dental/settings.py`.
  - Default configuration uses SQLite3.

- **Static and Media Files:**
  - Static files are served from the `static` directory.
  - Media files (e.g., uploaded images) can be configured in settings.

- **Secret Key:**
  - Ensure the `SECRET_KEY` in `settings.py` is kept confidential in production environments.

- **Email Host User & Email Host Password:**
  - Ensure the `EMAIL_HOST_USER` & `EMAIL_HOST_PASSWORD` in `settings.py` are assigned with your values.

## 📁 Project Structure

```
DentCare/
├── .venv/
├── DentCare/
│   └── dental/
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── static/
├── website/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── dj/
│           └── index.html
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## 📬 Contact

For any inquiries or feedback, feel free to reach out:

- **Email:** zeeldhengre265512@gmail.com
- **LinkedIn:** [Zeel Dhengre](https://www.linkedin.com/in/zeel-dhengre-486771254)

## Screenshot
![screencapture-127-0-0-1-8000-2025-06-04-18_07_38](https://github.com/user-attachments/assets/f8cd4651-1138-4256-a309-e6abd9ed2a35)


