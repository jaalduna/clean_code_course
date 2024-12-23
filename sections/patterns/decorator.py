class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self) -> dict:
        return self._raw_query


class QueryEnhancer:
    def __init__(self, query: DictQuery):
        self.decorated = query

    def render(self) -> dict:
        return self.decorated.render()


class RemoveEmpty(QueryEnhancer):
    def render(self):
        _original = super().render()
        return {k: v for k, v in _original.items() if v}


class CaseInsensitive(QueryEnhancer):
    def render(self):
        _original = super().render()
        return {k: v.lower() for k, v in _original.items()}


# an example of using the decorators
original = DictQuery(kye="value", empty="", none=None, upper="UPPER", title="Title")
original.render()
new_query = CaseInsensitive(RemoveEmpty(original))
new_query.render()
