from django_typograph.fields import TypographyField
from django.apps import apps
from django_typograph.engine.master import Master


def update(sender, **kwargs):
    i = kwargs['instance']
    for field in i._meta.fields:
        if isinstance(field, TypographyField):
            m = Master(apps.get_app_config("django_typograph").get_engine_for(field))
            setattr(i, field.name, m.typography(getattr(i, field.source)))
