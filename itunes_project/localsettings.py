# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_database',
        'HOST': 'localhost',
        'USER' : 'root',
        'PASSWORD' : 'Sanders20'
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-82@yj!-sdvk8hur3$kw20!cjp%wlmh)(i@#e@glor#&6kz$f8+'