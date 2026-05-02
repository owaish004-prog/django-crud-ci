import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY","dev")
DEBUG = os.getenv("DEBUG","True") == "True"
ALLOWED_HOSTS = []
INSTALLED_APPS = [
'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
'app',
]
MIDDLEWARE = [
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
]
ROOT_URLCONF='project.urls'
TEMPLATES=[{
'BACKEND':'django.template.backends.django.DjangoTemplates',
'DIRS':[],
'APP_DIRS':True,
'OPTIONS':{'context_processors':[
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
]}
}]
WSGI_APPLICATION='project.wsgi.application'
# DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_I18N=True
USE_TZ=True
STATIC_URL='static/'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
CACHES = {
 'default': {
   'BACKEND':'django_redis.cache.RedisCache',
   'LOCATION': os.getenv('REDIS_URL','redis://127.0.0.1:6379/1')
 }
}

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DB', 'djnagopipe'),
        'USER': os.getenv('MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', 'test@123'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}