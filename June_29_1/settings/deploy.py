from . base import *
env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))#.env까지의 경로

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n','')
    start=line.find('=')
    key = line[:start] #start까지의 값이 key
    value = line[start+1:] #start 이후의 값이 value
    env_list[key] = value
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-#1^h3bs&z18cztti#o8f8nh-#stp(qmwfk%wbrl@x#4%qkc+$k'
SECRET_KEY = env_list['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
