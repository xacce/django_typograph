# Типограф для Django 1.7+

## Установка

``` pip install django_typograph```

В settings.py INSTALLED_APPS добавить

``` django_typograph ```

## Использование

Импортировать 

``` from django_typograph.fields import TypographyField```

Добавить поле в модель

``` 
 _text = models.TextField()
field_name = TypographyField(source='_text') ```

```

Выполнить миграции


## Пример модели:

```
from django.db import models
from django_typograph.fields import TypographyField

class TestModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    _text = models.TextField()
    text = TypographyField(source='_text')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'TestModel'
        
```



## Доступные настройки у поля TypographyField

* source - Из какого поля брать исходный код для типографии
* engine - Использовать другой движок для типографии именно у этого поля
* options - настройки для указанного движка. Если движок не указан, то настройки все равно будут применены к текущим



## Настройка
Для тонкой настройки нужно переопределить AppCfg приложения

Создайте файл:
```project_root/project_name/apps/django_typograph.py```

Со след. содержимым
```
from django_typograph.apps import DjangoTypographConfig


class CustomTypographConfig(DjangoTypographConfig):
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
```

А теперь рисуем сову собственно.