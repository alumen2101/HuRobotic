from config.settings.base import *
from .base import *
import os
# override base.py settings

databases = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}