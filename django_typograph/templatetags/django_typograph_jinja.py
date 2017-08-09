# coding: utf-8
from __future__ import unicode_literals
from django.apps import apps
from django.utils.safestring import mark_safe
from django_jinja import library


@library.filter
def typo(text, engine=None):
    return mark_safe(apps.get_app_config('django_typograph').apply_for_text(text, engine))
