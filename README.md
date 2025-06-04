
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

   *Note: If `requirements.txt` is not present, you can install Django directly:*

   ```bash
   pip install django
   ```

5. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (for Admin Access):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up the superuser account.

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/` in your web browser.

## 🔧 Configuration

- **Database Settings:**
  - Located in `DentCare/settings.py`.
  - Default configuration uses SQLite3. To switch to another database (e.g., PostgreSQL), update the `DATABASES` section accordingly.

- **Static and Media Files:**
  - Static files are served from the `static` directory.
  - Media files (e.g., uploaded images) are stored in the `media` directory.

- **Secret Key:**
  - Ensure the `SECRET_KEY` in `settings.py` is kept confidential in production environments.

- **Email Host User & Email Host Password:**
  - Ensure the `EMAIL_HOST_USER` & `EMAIL_HOST_PASSWORD` in `settings.py` are assigned with your values.



## 📁 Project Structure

```
DentCare/
├── DentCare/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── appointments/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── templates/
│   └── base.html
├── static/
│   ├── css/
│   └── js/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## 📬 Contact

For any inquiries or feedback, feel free to reach out:

- **Email:** zeeldhengre265512@gmail.com
- **LinkedIn:** [Zeel Dhengre](https://www.linkedin.com/in/zeel-dhengre-486771254)
