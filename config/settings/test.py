"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="GlSRVXhTNJXx3Fnu5HUYlgeoMIXy3rl76CIhfOAEHtXE4jrGAEDbAWyzIpW7SVQn",
)
# The first key will be used to encrypt all new data, and decryption of existing values will be attempted
# with all given keys in order. This is useful for key rotation: place a new key at the head of the list
# for use with all new or changed data, but existing values encrypted with old keys will still be accessible
FERNET_KEYS = [
    env(
        "FERNET_SECRET_KEY_1",
        default="c1a70768d2e913ecc107963b307d1e2c6e4b78cc46f856c50caf035e4467adfa",
    )
]
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
# Your stuff...
# ------------------------------------------------------------------------------

DATABASES = {"default": env.db("DATABASE_URL", default="postgres:///care-test")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# https://whitenoise.evans.io/en/stable/django.html#whitenoise-makes-my-tests-run-slow
WHITENOISE_AUTOREFRESH = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(levelname)s %(asctime)s %(module)s %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "ERROR",
    },
}

CELERY_TASK_ALWAYS_EAGER = True
