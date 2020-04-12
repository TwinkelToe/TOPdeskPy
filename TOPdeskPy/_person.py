from . import _utils
class person:

    def __init__(self, topdesk_url, credpair):
        self._topdesk_url = topdesk_url
        self._credpair = credpair
        self.utils = _utils.utils(self._topdesk_url, self._credpair)
        self.private_details = self._private_details(self._topdesk_url, self._credpair)
        self.contract = self._contract(self._topdesk_url, self._credpair)

    def get(self, id):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/persons/id/{}".format(id)))
    
    def get_list(self, archived=False, page_size=100, query=None):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/persons/", archived, page_size, query))        

    def create(self, **kwargs):
        return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/persons", (self.utils.add_id_jsonbody(**kwargs))))

    def update(self, person, **kwargs):
        return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/persons/id/{}".format(person), self.utils.add_id_jsonbody(**kwargs)))

    def archive(self, person_id, reason_id=None):
        if reason_id:
            param = {'id': reason_id}
        return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/persons/id/{}/archive".format(person_id), param))

    def unarchive(self, person_id):
        return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/persons/id/{}/unarchive".format(person_id), None))

    class _contract:
        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)

        def get(self, person_id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/persons/id/{}/contract".format(person_id)))

        def update(self, person_id, **kwargs):
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/persons/id/{}/contract".format(person_id), self.utils.add_id_jsonbody(**kwargs)))

    class _private_details:
        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)
        
        def get(self, person_id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/persons/id/{}/privateDetails".format(person_id)))

        def update(self, person_id, **kwargs):
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/persons/id/{}/privateDetails".format(person_id), self.utils.add_id_jsonbody(**kwargs)))

if __name__ == "__main__":
    pass