# Make a Django Front-End for Your SQL Server Database

This tutorial gives you the tools to make a web application to view the tables to your databases and make updates to them without using the SQL language. This is a great tool to use across teams.

## Setup 

The tutorial setup takes a maximum of 5 minutes to complete. Do these steps once before you do the tutorial.

#### Install Python and SQL Server
Head [here](https://aka.ms/sqldev) and choose your operating system under the Python link. Copy and paste the commands in the Set up your environment step. If you already have Python and SQL Server installed, be sure to install the command line tools or open a DB admin GUI where you can create a new database. 

#### Create a Database

On Windows/Linux run this command

`$ sqlcmd -S localhost -U sa -P your_password -Q "CREATE DATABASE Sample;"`

On MacOS run this command

`$ mssql -s localhost -u sa -p your_password -q "CREATE DATABASE Sample;"`

#### Install Packages

If you haven’t already install virtual environment:

`$ pip install virtualenv`

Make new virtual environment with the following command:

`$ virtualenv venv`	

Activate the virtual environment. On Linux/MacOs run this command:

`$ source venv/bin/activate`	

On Windows run: 

`$ venv\Scripts\activate`	

Your prompt should now be prefixed with the name of your environment. 

Install these requirements. Github requirments.txt 

`$ pip install django-pyodbc-azure`	

#### Create a New Django Project 

From the command line, cd into a directory where you’d like to store your code, then run the following command:

`$ django-admin startproject SQLTutorial`

This will create a SQLTutorial directory in your current directory. Navigate into this directory. 

Great now you’re ready to get coding!

## Tutorial

Now we are going to make a front-end for your new database. We will make a schema and migrate it to your database.

#### Connect to your database.  

Navigate into the inner SQLTutorial directory. This directory is the Python package for your project. Open the settings.py file in your favorite text editor and update it with your database information. 

`DATABASES = {

       'default': {
         'ENGINE': 'sql_server.pyodbc’,
         'NAME': 'Sample',
         'USER': 'sa',
         'PASSWORD': 'your_password',
         'HOST': 'localhost',
         'PORT': '1433',
         'OPTIONS': {
            'driver':'ODBC Driver 13 for SQL Server',
         },
     },
}`


Run the following command to migrate Django’s initial installed apps including the admin site

`$ python manage.py migrate`

#### Make your models

We are going to give this database a simple schema with tables for Students, Professors, Departments, Courses and Course Reviews insert database schema diagram. We will make the models and then migrate them to the database. 

Navigate to your outer SQLTutorial directory. Make a directory called app and navigate into it

`$ mkdir app`

`$ cd app`

>TODO models

#### Migrate Models into Database

To include the app folder in our project, first we need to add a reference in settings.py. Naviagate back to SQLTutorial/settings.py and add 'app’ into the INSTALLED_APPS setting. It will look like this:

[For more info](https://docs.djangoproject.com/en/1.10/intro/tutorial02/)

`INSTALLED_APPS = [

    'app’,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]`

>Add an empty __init__.py in app folder

`$ python manage.py makemigrations app`

`$ python manage.py sqlmigrate app 0001`

`$ python manage.py migrate`

#### Tables
>TODO Tables
Install these packages:

`$ pip install django-tables2`

`$ pip install django-bootstrap-toolkit`

`$ pip install django-bootstrap-form`

Add all of these to installed apps in settings.py

    'django_tables2',
    
    'bootstrap_toolkit',
    
    'bootstrapform',

The tables are found in app/tables.py The docs are [here](https://django-tables2.readthedocs.io/en/latest/)

#### Forms

>TODO Forms

We can create forms directly from the models we made with [Django ModelForms](https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/). 
These forms will allow us to add and edit rows in our database. The forms are found in app/forms.py

#### Views
>TODO Views
app/views.py. 
The views enable CRUD for your database. 

#### URLs
> TODO urls

urls.py

#### Templates
The html templates are found in app/templates



