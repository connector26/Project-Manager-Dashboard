# 📊 Project Manager Dashboard

A Django and MySQL-based dashboard application designed to help project managers track deliverables and ensure timely delivery of projects. Built for scalability and real-time monitoring of tasks, the dashboard supports both small and large-scale project tracking.

---

## 🚀 Features

- Project deliverable tracking
- Admin panel using Django's built-in admin site
- User authentication and role management
- Static dashboard views
- MySQL integration for robust data management

---

## 🛠️ Installation & Setup

### 1. Prerequisites

Make sure you have the following installed:

- Python (3.8 or later)
- Django (latest stable version)
- MySQL Server

### 2. Create and Activate Virtual Environment

Navigate to your desired folder and run:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Make sure mysqlclient or equivalent is included in your requirements.

4. Database Setup
Update settings.py with your MySQL credentials:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Then run:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Create Superuser (Admin Access)
bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set your admin credentials.

6. Run the Development Server
bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000/ to access the application.

🧭 Project Structure
csharp
Copy
Edit
project-manager-dashboard/
│
├── dashboard/               # Core app
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, images)
├── manage.py
├── db.sqlite3               # (If using SQLite temporarily)
├── requirements.txt
└── README.md
🔮 Future Scope
Integration with Power BI for dynamic dashboards

Task analytics and visual reports

Notification system for missed deadlines

API support for mobile clients

Enhanced project timeline visualization

📬 Contribution
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License
MIT License

👨‍💼 Admin Panel
Accessible at /admin/ after creating a superuser. This is Django's default admin which can be customized and styled for better user experience.
