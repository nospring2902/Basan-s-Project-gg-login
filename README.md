# Basan project

## Description
Never mind about the name of the folder haha. The API folder is the app of the Django project, the music controller is the main directory of our project. If you have other questions, ask me via Line and I will explain in details.

## How to Install and Run This Web Application

you can clone my repo following the instructions below and run it on localhost:

### Requirements
Before proceeding with the installation steps below, you need to install [Python](https://www.python.org/) and then [pip](https://www.youtube.com/watch?v=fJKdIf11GcI).

### Installation
1. **Install Git**  
   ```bash
   winget install --id Git.Git -e --source winget
   ```
2. **Clone my repo**  
   After installing Git, to clone my repo you need to close the `cmd` and restart it, but this time **run as administrator**.  
   After restarting under admin rights, run the following command:  
   ```bash
   git clone https://github.com/LyMuc/Basan-s-Project
   ```
3. **Change directory**  
   Navigate to the project directory:  
   ```bash
   cd Basan-s-Project
   ```
4. **Install Django**  
   Install Django using pip:
   ```bash
   pip install django
   ```
5. **Install necessary module**
   Run the following commands to install modules that are used in the project
   ```bash
   pip install djangorestframework
   ```
   ```bash
   pip install django-crispy-forms
   ```
   ```bash
   pip install django-bootstrap4
   ```
   ```bash
   pip install crispy-bootstrap4
   ```
7. **Make migrations and then migrate**  
   Run the 2 following commands:  
   ```bash
   python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate
   ```
8. **Create a superuser**
   In order to run this app, we need to create a superuser. Run the following command:
   ```bash
   python manage.py createsuperuser
   ```
   Feel free to choose your user name, email and password. (Email is optional)
9. **Run server**
   ```bash
   python manage.py runserver
   ```
   When the server is hosted, you can run this webapp at this URL: http://127.0.0.1:8000
