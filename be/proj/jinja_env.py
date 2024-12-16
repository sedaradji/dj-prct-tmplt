"""Jinja env"""
from time import time

from django.conf import settings
from django.templatetags.static import static
from django.urls import resolve, reverse
from jinja2.environment import Environment


def environment(**options):
    """Jinja env"""
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "now": time,
            "url": reverse,
            "view": resolve,
            "settings": settings,
        }
    )
    return env
