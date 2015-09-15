from django.apps import AppConfig
from django.apps import apps
from django_typograph import fields
from django_typograph import recievers
from django.db.models.signals import pre_save


class DjangoTypographConfig(AppConfig):
    name = "django_typograph"

    engines = {
        'EMT': {
            'path': 'django_typograph.engine.EMT.driver.typography',
            'options': {},
        },
        'EMT_SAFE': {
            'path': 'django_typograph.engine.EMT.driver.typography',
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

    default_engine = "EMT"

    def get_engine_for(self, field):
        engine = field.engine if field.engine else self.default_engine
        engine_data = self.engines.get(engine)
        engine_data['options'].update(field.options)

        return engine_data

    def ready(self):
        self.t_models = set([])
        for m in apps.get_models(include_auto_created=True):
            for f in m._meta.fields:
                if not isinstance(f, fields.TypographyField):
                    continue
                self.t_models.add(m)

        for m in self.t_models:
            pre_save.connect(recievers.update, m)
