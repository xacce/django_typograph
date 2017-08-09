from django.apps import apps


def update(instance, **kwargs):
    app = apps.get_app_config("django_typograph")
    app.apply(instance)
