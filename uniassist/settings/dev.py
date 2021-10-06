from .base import *
import os

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myproject',
#         'USER': 'myprojectuser',
#         'PASSWORD': 'password',
#         # 'HOST': 'localhost',
#         # 'PORT': '',
#     }
# }

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = '/root/static'

# for file upload by the user
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
