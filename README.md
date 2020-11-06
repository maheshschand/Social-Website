# Social Website
Social Website created using Django framework.

## Features
- Bookmark an image.
- User registration.
- Custom profiles.
- Implement features to like a image and follow an user.
- An activity stream application.
- Storing item views in Redis.
- Generating image thumbnails using easy-thumbnails.
- AJAX Pagination.


## Demo
[Social Website](https://suven-social.herokuapp.com/)

## Run project locally
1. Clone the project  
    ```bash
    git clone https://github.com/maheshschand/Social-Website.git 
    ```
2. Create a virtual evironment
    ```bash
    python -m venv venv
    ```
3. Activate your virtual environment  
    **For Windows**
    ```powershell
    cd venv\Scripts
    activate
    ```

    **For linux**
    ```bash
    source venv/bin/activate
    ```
    The shell prompt will include the name of the active virtual environment enclosed in parentheses, as follows:
    ```bash
    (venv) $
    ```
4. Locate the Social-Website folder and run the following command
    ```bash
    (venv) $ pip install -r requirements.txt
    ```
5. Create the database migration for model.  
    Run the following command to create the database migration.
    ```bash
    (venv) $ python manage.py makemigrations
    ```
6. Migrate the database  
    Run the following command to migrate the database.
    ```bash
    (venv) $ python manage.py migrate
    ```
7. Create a administrator account  
    Run the following command to create a super user
    ```bash
    (venv) $ python manage.py createsuperuser
    ``` 
8. Run the following command to turn on the development server
    ```bash
    (venv) $ python manage.py runserver
    ```
    Enter in the browser: http://127.0.0.1:8000

9. Use the management command runserver_plus provided by Django Extensions to run the development server, as follows:
    ```bash
    (venv) $ python manage.py runserver_plus --cert-file cert.crt
    ```
    This provide SSL/TLS certificate for the project. Django Extensions will generate a key and certificate automatically. 