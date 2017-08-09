from . import EMT


class Driver(object):
    def __init__(self, options):
        self.e = EMT.EMTypograph()
        self.e.setup(options)

    def apply(self, text):
        if not text or text == ' ':
            return text
        return self.e.fast_apply(text)
