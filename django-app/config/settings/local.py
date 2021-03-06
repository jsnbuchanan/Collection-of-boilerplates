from .base import *
import datetime


# -->> Email setup
EMAIL_HOST = ""
EMAIL_PORT = ""
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ""
DEFAULT_FROM_EMAIL = ""
ADMINS = (("name", "email"),)

MANAGERS = ADMINS

# -->> .env setup
# -->> for local.py
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="#qyfwdupwy_h)95jot--$+cc8bibaco2ui7!3@7(5-z5%2mu(+"
)

# -->> Debug is true
# -->> Allowed host can be empty
DEBUG = env.bool("DJANGO_DEBUG", default=True)

INTERNAL_IPS = ["127.0.0.1"]


SESSION_EXPIRE_AT_BROWSER_CLOSE = True


ROOT_URLCONF = "config.urls.local"

THIRD_PARTY_APPS = ("debug_toolbar",)
LOCAL_APPS = ("home",)
INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
