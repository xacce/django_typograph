*В пипе старая версия, новую ставить только через гит*


```

    DJANGO_TYPOGRAPH_MODELS = {
        'app_name.model_name': [('field_name','EMT_SAFE'), 'field_name_default_engine')]
    }
    
```

### Only django-jinja

```

{{ variable|typo }}
{{ variable|typo('EMT_SAFE') }}

```