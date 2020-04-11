from . import _utils
class person:

    def __init__(self, topdesk_url, credpair):
        self._topdesk_url = topdesk_url
        self._credpair = credpair
        self.utils = _utils.utils(self._topdesk_url, self._credpair)

    def get(self, id):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/persons/id/{}".format(id)))
    
    def get_list(self, archived=False, page_size=100, query=None):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/persons/", archived, page_size, query))        

    def create(self, **kwargs):
        return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/persons", (self.utils.add_id_jsonbody(**kwargs))))

    def update(self, person, **kwargs):
        return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/persons/id/{}".format(person), self.utils.add_id_jsonbody(**kwargs)))

if __name__ == "__main__":
    pass