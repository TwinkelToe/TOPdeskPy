from . import _utils
import re

class incident:

    def __init__(self, topdesk_url, credpair):
        self._topdesk_url = topdesk_url
        self._credpair = credpair
        self.utils = _utils.utils(self._topdesk_url, self._credpair)

    def get_uuid(self, uuid):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/id/{}".format(uuid)))
        
    def get_number(self, number):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/number/{}".format(number)))

    def durations(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/durations"))

    def statuses(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/statuses"))

    def deescalation_reasons(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/deescalation-reasons"))
    
    def escalation_reasons(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/escalation-reasons"))
    
    def service_windows(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/slas/services"))

    def call_types(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/call_types"))

    def closure_codes(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/closure_codes"))

    def entry_types(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/entry_types"))

    def categorys(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/categories"))

    def subcategorys(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/subcategories"))

    def impacts(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/impacts"))

    def priorities(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/priorities"))

    def urgencies(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/urgencies"))

    def get_id_impact(self, query):
        result = self.impacts()
        canidates = list()
        for impact in result:
            if re.match(rf"(.+)?{query}(.+)?", impact['name'], re.IGNORECASE):
                canidates.append(impact['id'])

        return self.utils.print_lookup_canidates(canidates)

    def get_id_priority(self, query):
        result = self.priorities()
        canidates = list()
        for priority in result:
            if re.match(rf"(.+)?{query}(.+)?", priority['name'], re.IGNORECASE):
                canidates.append(priority['id'])

        return self.utils.print_lookup_canidates(canidates)

    def get_id_urgency(self, query):
        result = self.urgencies()
        canidates = list()
        for urgency in result:
            if re.match(rf"(.+)?{query}(.+)?", urgency['name'], re.IGNORECASE):
                canidates.append(urgency['id'])

        return self.utils.print_lookup_canidates(canidates)

    def get_id_entryType(self, query):
        result = self.entry_types()
        canidates = list()
        for entryType in result:
            if re.match(rf"(.+)?{query}(.+)?", entryType['name'], re.IGNORECASE):
                canidates.append(entryType['id'])

        return self.utils.print_lookup_canidates(canidates)

    def get_id_callType(self, query):
        result = self.call_types()
        canidates = list()
        for callType in result:
            if re.match(rf"(.+)?{query}(.+)?", callType['name'], re.IGNORECASE):
                canidates.append(callType['id'])

        return self.utils.print_lookup_canidates(canidates)

    def create(self, caller, **kwargs):
        # Caller can be: email, uuid or unregisted user. We'll try it in that order.
        create_body = kwargs
        create_body['caller'] = caller     
        return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/incidents/", self.utils.add_id_jsonbody(**create_body)))

    def update(self, incident, **kwargs):
        if self.utils.is_valid_uuid(incident):
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/incidents/id/{}".format(incident), self.utils.add_id_jsonbody(**kwargs)))
        else:            
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/incidents/number/{}".format(incident), self.utils.add_id_jsonbody(**kwargs)))

    def get_list(self, archived=False, page_size=100, **kwargs):
        # reqeust_uri = "&".join("=".join(_) for _ in kwargs.items())
        # print(reqeust_uri)
        # URL encode.
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/incidents/", archived, page_size, extended_uri=kwargs))

if __name__ == "__main__":
    pass