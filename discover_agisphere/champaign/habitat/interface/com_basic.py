class ComOriginate(object):
    def __init__(self, type) -> None:
        self._type = type

    def is_running(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    @property
    def type(self):
        return self._type