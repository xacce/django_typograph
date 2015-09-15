from __future__ import unicode_literals
from django.core.management import BaseCommand
from progressbar import ProgressBar

from django.apps import apps


class Command(BaseCommand):
    def handle(self, *args, **options):
        app = apps.get_app_config("django_typograph")
        for m in app.t_models:
            i = 0
            count = m.objects.count()
            print "\033[95mStart for model %s\033[0m" % m
            with ProgressBar(maxval=count) as progress:
                for r in m.objects.all():
                    r.save(force_update=True)
                    progress.update(i)
                    i += 1
