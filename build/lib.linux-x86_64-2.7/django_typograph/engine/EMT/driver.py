from . import EMT


def typography(text, options=None):
    e = EMT.EMTypograph()
    e.setup(options)
    return e.fast_apply(text)
