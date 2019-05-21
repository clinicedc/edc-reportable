#!/usr/bin/env python
import os

from django.conf import settings
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname


class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=dirname(abspath(__file__)),
    APP_NAME="test_project",
    ETC_DIR=os.path.join("tests", "etc"),
    EDC_BOOTSTRAP=3,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "edc_reportable.apps.AppConfig",
        "test_app.apps.AppConfig",
    ],
).settings

if not settings.configured:
    settings.configure(**DEFAULT_SETTINGS)
