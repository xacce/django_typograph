from django.apps import AppConfig
from django.utils.module_loading import import_string
from django_typograph import recievers
from django.db.models.signals import pre_save
from django.apps import apps
from django.conf import settings


class DjangoTypographConfig(AppConfig):
    name = "django_typograph"

    engines = {
        'EMT': {
            'path': 'django_typograph.engine.EMT.driver.Driver',
            'options': {},
        },
        'EMT_SAFE': {
            'path': 'django_typograph.engine.EMT.driver.Driver',
            'options': {
                'OptAlign.all': 'off',
                'OptAlign.oa_oquote': 'off',
                'OptAlign.oa_obracket_coma': 'off',
                'OptAlign.layout': 'off',
                'Text.paragraphs': 'off',
                'Text.auto_links': 'off',
                'Text.breakline': 'off',
                'Text.no_repeat_words': 'off',
            }
        }
    }

    default_engine = "EMT_SAFE"

    def ready(self):
        self._models = dict()
        self._engines = {}
        for name, config in self.engines.items():
            self._engines[name] = import_string(config['path'])(config.get('options'))

        for model, fields in getattr(settings, 'DJANGO_TYPOGRAPH_MODELS', {}).items():
            model = apps.get_model(model)
            self._models[model] = {}
            for field in fields:
                if hasattr(field, '__iter__'):
                    field, engine = field
                else:
                    engine = self.default_engine

                self._models[model][field] = self._engines[engine]

                pre_save.connect(recievers.update, model)

    def apply(self, instance):
        model = instance.__class__
        if model not in self._models:
            return

        for field, engine in self._models[model].items():
            setattr(instance, field, engine.apply(getattr(instance, field)))

    def apply_for_text(self, text, engine=None):
        return self._engines[engine or self.default_engine].apply(unicode(text))
