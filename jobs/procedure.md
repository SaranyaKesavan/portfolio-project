<div>
    <h3>For the unapplied changes to reflect in db run :</h3>
    <h4>
        <strong>python manage.py migrate</strong>
    </h4>
    <h3>when a new model is added or something run :</h3>
    <h4>updates the database
        <strong>python manage.py makemigrations</strong>
    </h4>
</div>
<div>
    <p>When a new app is added, add the new app to settings.py as below,
    </p>
    <ul>
        <li>Goto settings.py ->INSTALLED_APPS</li>
        <li>add 'appname.apps.cpyclsnamefrmapps.py'</li>

    </ul>
</div>

TO add media files:
1. GOTO settings.py 
2. GOTO end of the file and add the following
    - #media files (images)
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    - # where to access media files (value can be anything as u want - user defined)
    MEDIA_URL = '/media/'

3. Then run python manage.py makemigrations

To use ImageField we need pillow to be installed use the following command:(installed version 7.0.0)
For Windows:
python -m pip install pillow

For ubuntu:
pip install pillow

To see db structure / schema for app say jobs:
goto jobs/migrations/0001_initail.py (filename)


DEALING WITH WITH ADMIN::

Creating Super user:
python manage.py createsuperuser

- give username
- give email or simply enter
- provide password
- confirm password

restart server before login after creating super user (no need if server is already running)

TO show any model in the admin portal add that to admin.py in that respective app like

from .models import Job (model class name)

# to register
admin.site.register(Job)

To show the image when clicked from admin portal do the following
in urls.py add the (media path)following

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...............
    ...............
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


Postgresql:

used version : 12.2 

For Linux:
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql



For Windows:
Install postgresql for windows

TO access postgresql from windows command prompt
1. Adding bin folder path to environmental variable (psql)
    C:\Program Files\PostgreSQL\12\bin
2. Adding lib folder path to environmental variable
    C:\Program Files\PostgreSQL\12\lib

1. To connect from cmd :
    psql -U <username> <dbname>
    psql -U postgres postgres

2. To list the relations
    \dt

3. To list users:
    \du

4. To exit or quit
    \q

5. To change password
    \password <username>

6. Creating new db:
    CREATE DATABASE <dbname>;


Connecting Django with Postgresql:
used version psycopg2-2.8.4
IN settings.py: NAME - dbname

DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql',
        'NAME'    : 'portfoliodb',
        'USER'    : 'postgres',
        'PASSWORD': '#welcome123',
        'HOST'    : '127.0.0.1',
        'PORT'    : '5432',
    }
}


1. install the following libraby
    pip install psycopg2

2. Need to do migrations cuz we changed from sqlite to postgres

3. run: python manage.py migrate

4. need to create super user again

Reading from db showing in fronted


Using static :
1. in settings.py add the below:

STATICFILES_DIRS = [
                os.path.join(BASE_DIR, 'portfolio/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

2. then run : python manage.py collectstatic



