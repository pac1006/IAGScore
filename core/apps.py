"""
This file is used to configure the app name in the Django admin panel.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Core configurations
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
