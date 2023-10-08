class ObjectRepository(object):

    def __init__(self):
        self._objDict = {}
        self._idList = []

    def __del__(self):
        self.clear()

    def _has_key(self, key):
        return key in self._objDict

    def add(self, key, obj):
        if self._has_key(key):
            raise Exception('key: "%s" is existed!' % (key))
        self._objDict[key] = obj
        return True

    def find(self, key):
        obj = self._objDict.get(key)
        return obj

    def delete(self, key):
        if self._has_key(key):
            del self._objDict[key]
            return True
        return False

    def clear(self):
        self._objDict.clear()
        self._idList = []

    def items(self):
        return self._objDict.items()

    def values(self):
        return self._objDict.values()

    def keys(self):
        return self._objDict.keys()

    def update(self, key, obj):
        self._objDict.update({key: obj})