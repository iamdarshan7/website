from .base import *
import os
from decouple import config

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('HOST'),   # Or an IP Address that your DB is hosted on
#         'PORT': config('DB_PORT'),
#     }
# }

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
# STATIC_ROOT = '/root/static'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # new


# for file upload by the user
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': "estudyga_garage"
#         'USER': "estudyga_mechanic",
#         'PASSWORD': "study4garage",
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': 3306,
#     }
# }