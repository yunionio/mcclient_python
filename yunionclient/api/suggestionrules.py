from yunionclient.common import base

class Suggestionrule(base.ResourceBase):
    pass


class SuggestionruleManager(base.SuggestionManager):
    resource_class = Suggestionrule
    keyword = 'suggestysrule'
    keyword_plural = 'suggestsysrules'
    _columns = ["Id", "Name", "Type", "Period", "TimeFrom", "Setting"]

