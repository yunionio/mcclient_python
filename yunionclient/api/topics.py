from yunionclient.common import base

class Topic(base.ResourceBase):
    pass


class TopicManager(base.NotifyManager):
    resource_class = Topic
    keyword = 'topic'
    keyword_plural = 'topics'
    _columns = ["Id", "Name", "Type", "Enabled", "Resources"]

