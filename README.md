# User Profile REST API

A simple Django REST Framework (DRF) API for managing user profiles, with automatic age calculation and validation.

---

## 📋 Features

- Create, Read, Update, and Delete user profiles (CRUD)
- Automatically calculate age from date of birth
- Validation to prevent future dates or under-1-year-old users
- Search users by name
- JSON API endpoints

---

## 🧱 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (default, can be changed)
- **Language:** Python 3.x  

---


---

## ⚙️ Installation & Setup

1. Create and activate a virtual environment
   ```bash
    python -m venv venv
   # Windows:
    venv\Scripts\activate    
   #MacOs:
    source venv/bin/activate

2. Install dependencies
   ```bash
    pip install django djangorestframework


3. **Clone the repository**
   ```bash
   git clone https://github.com/s01dier-0f-g0d/simple_user_api-drf.git
   cd simple_user_api-drf

4. Register the api in settings.py
   ```bash
   # Update api_crud/settings.py as shown below -->
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
   ]
    REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
    }

5. Include URLs from the api app
   ```bash
   # Replace the code inside api_crud/urls.py with the below -->
   
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('api/',include('api.urls'))
      ]

5. Run database migrations
   ```bash
    python manage.py makemigrations
    python manage.py migrate

6. Start the development server
   ```bash
    python manage.py runserver
   
7. Navigate to http://localhost/api/

## 🌐 API Endpoints
### 1️⃣ API Home
### GET /api/
→ Returns API overview with available endpoints.

### 2️⃣ Get All Users / Create User
GET /api/users/

POST /api/users/


## 🧠 Model Overview
| Field           | Type           | Description              |
| --------------- | -------------- | ------------------------ |
| `id`            | AutoField      | Primary key              |
| `name`          | CharField(100) | User’s full name         |
| `date_of_birth` | DateField      | Date of birth            |
| `age`           | Property       | Calculated automatically |

## 🚀 Example Flow

1. Create a new user via POST /api/users/

2. View all users via GET /api/users/

3. Retrieve one via /api/users/<id>/

4. Update or delete using PUT or DELETE methods

5. Search users by name using /api/search/?name=<term>

### 👨‍💻 Author: Darshan M
### 📧 Email: darshan8216@gmail.com
### 🌐 GitHub: https://github.com/s01dier-0f-g0d
