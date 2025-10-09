from yunionclient.common import base

class Suggestionalert(base.ResourceBase):
    pass


class SuggestionalertManager(base.SuggestionManager):
    resource_class = Suggestionalert
    keyword = 'suggestsysalert'
    keyword_plural = 'suggestsysalerts'
    _columns = ["Id", "Name", "Rule_Name", "Type", "Problem", "Action", "Provider", "Project", "Cloudaccount", "Amount"]

