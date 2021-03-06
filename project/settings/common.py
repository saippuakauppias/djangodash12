import os
import djcelery


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)
PROJECT_ROOT = os.path.abspath(PROJECT_ROOT)
PACKAGE_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = [
    ("Dima Kukushkin", "kukushkin@trilan.ru"),
    ("Denis Veselov", "veselov@trilan.ru"),
    ("Alexander Aslanov", "aslanov@trilan.ru"),
]

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don"t share it with anybody.

SECRET_KEY = 'SECRET KEY'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",

    "blogs.context_processors.blogger",
    "repositories.context_processors.github",
]


MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "project.urls"

# Python dotted path to the WSGI application used by Django"s runserver.
WSGI_APPLICATION = "project.wsgi.application"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

INSTALLED_APPS = (
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "south",
    "djcelery",
    "djkombu",

    "blogs",
    "repositories",
    "project.core",
    "parser",
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PACKAGE_ROOT, "fixtures"),
]

USE_TZ = False


GITHUB_ID = os.environ.get('GITHUB_ID', '')
GITHUB_SECRET = os.environ.get('GITHUB_SECRET', '')
GITHUB_SCOPES = ('user', 'public_repo', 'repo')
GITHUB_AUTH_URL = 'https://github.com/login/oauth/authorize'
GITHUB_API_HOST = 'https://api.github.com'
GITHUB_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_CALLBACK_URL = 'http://djangodash12.trilandev.com/repositories/oauth2callback/'


GOOGLE_ID = os.environ.get('GOOGLE_ID', '')
GOOGLE_SECRET = os.environ.get('GOOGLE_SECRET', '')
GOOGLE_SCOPES = (
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/blogger.readonly',
)
GOOGLE_AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_CALLBACK_URL = 'http://djangodash12.trilandev.com/blogs/oauth2callback'

GOOGLE_API_ROOT = 'https://www.googleapis.com/oauth2/v1/'
BLOGGER_API_ROOT = 'https://www.googleapis.com/blogger/v3/'

PARSE_PAGES_COUNT = 20

djcelery.setup_loader()

BLOGS_ROOT = os.path.join(PROJECT_ROOT, 'blogs')
KEYS_ROOT = os.path.join(PACKAGE_ROOT, 'keys')
