import re, base64
from . import _incident
from . import _person
from . import _utils
# from .incident import incident
class connect:
    # Created API-version 3.0.5

    def __init__(self, topdesk_url, topdesk_username, topdesk_password):
        self._topdesk_url = topdesk_url
        self._credpair = (base64.b64encode((topdesk_username + ':' + topdesk_password).encode("utf-8"))).decode("utf-8")
        self._partial_content_container = []
        self.incident = _incident.incident(self._topdesk_url, self._credpair)
        self.person = _person.person(self._topdesk_url, self._credpair)
        self.utils = _utils.utils(self._topdesk_url, self._credpair)
        self.department = self._operator(self._topdesk_url, self._credpair)
        self.branche = self._branche(self._topdesk_url, self._credpair)
        self.location = self._location(self._topdesk_url, self._credpair)
        self.supplier = self._supplier(self._topdesk_url, self._credpair)
        self.operatorgroup = self._operatorgroup(self._topdesk_url, self._credpair)
        self.operator = self._operator(self._topdesk_url, self._credpair)

    class _operator:

        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)
            
        def get_list(self, archived=False, page_size=100, query=None):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators", archived, page_size, query))

        def get(self, id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}".format(id)))


        def get_operatorgroups_operator(self, id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}/operatorgroups".format(id)))

        def get_id_operator(self, query):
            result = self.get_list()
            canidates = list()
            for operator_dynamic_name in result:
                if re.match(rf"(.+)?{query}(.+)?", operator_dynamic_name['dynamicName'], re.IGNORECASE):
                    canidates.append(operator_dynamic_name['id'])

            return self.utils.print_lookup_canidates(canidates)

    class _operatorgroup:
        
        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)
        
        def get_operators_operatorgroup(self, id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operatorgroups/id/{}/operators".format(id)))

        def get_list(self, archived=False, page_size=100, query=None):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operatorgroups", archived, page_size, query))

        def get_id_operatorgroup(self, query):
            result = self.get_list()
            canidates = list()
            for operatorgroup in result:
                if re.match(rf"(.+)?{query}(.+)?", operatorgroup['groupName'], re.IGNORECASE):
                    canidates.append(operatorgroup['id'])

            return self.utils.print_lookup_canidates(canidates)

    class _supplier:

        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)

        def get(self, id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/suppliers/{}".format(id)))

        def get_list(self, archived=False, page_size=100, query=None):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/suppliers", archived, page_size, query)) 

    class _location:

        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)
        
        def get_list(self, archived=False, page_size=100, query=None):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/locations", archived, page_size, query))

        def get(self, id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/locations/id/{}".format(id)))
 
    class _branche:
        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)

        def get_list(self, archived=False, page_size=100, query=None):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/branches", archived, page_size, query))

        def get(self, id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/branches/id/{}".format(id)))
            
    class _department:

        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)

        def get_list(self, archived=False, page_size=100):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/departments", archived, page_size))

        def get(self, query):
            result = self.get_list()
            canidates = list()
            for departments in result:
                if re.match(rf"(.+)?{query}(.+)?", departments['name'], re.IGNORECASE):
                    canidates.append(departments['id'])

            return self.utils.print_lookup_canidates(canidates)

    def get_countries(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/countries"))    

    def get_budgetholders(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/budgetholders"))

    def get_archiving_reasons(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/archiving-reasons"))

    def get_timespent_reasons(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/timespent-reasons"))               


if __name__ == "__main__":
    pass
