from django.db import models


class TypographyField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.source = kwargs.pop('source', None)
        self.engine = kwargs.pop("engine", None)
        self.options = kwargs.pop("options", {})
        d = {'editable': False, 'blank': True, 'null': True}
        d.update(kwargs)
        super(TypographyField, self).__init__(*args, **d)
