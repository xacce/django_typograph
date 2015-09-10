from __future__ import unicode_literals
from django.utils.module_loading import import_string
import logging


class Master(object):
    def __init__(self, engine_data):
        self.engine_data = engine_data

    def typography(self, text):
        try:
            return import_string(self.engine_data.get('path'))(text, self.engine_data.get('options'))
        except Exception, e:
            logging.error("Typograph error. Engine: %s. Error: %s" % (self.engine, e))
            return text
