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
        self.budgetholder = self._budgetholder(self._topdesk_url, self._credpair)
        self.operational_activities = self._operational_activities(self._topdesk_url, self._credpair)

    class _operator:

        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)
            
        def get_list(self, archived=False, page_size=100, query=None):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators", archived, page_size, query))

        def get(self, id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}".format(id)))


        def get_operatorgroups(self, operator_id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}/operatorgroups".format(operator_id)))

        def get_id_operator(self, query):
            result = self.get_list()
            canidates = list()
            for operator_dynamic_name in result:
                if re.match(rf"(.+)?{query}(.+)?", operator_dynamic_name['dynamicName'], re.IGNORECASE):
                    canidates.append(operator_dynamic_name['id'])

            return self.utils.print_lookup_canidates(canidates)

        def create(self, **kwargs):
            return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/operators", (self.utils.add_id_jsonbody(**kwargs))))

        def update(self, operator_id, **kwargs):
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operators/id/{}".format(operator_id), self.utils.add_id_jsonbody(**kwargs)))

        def archive(self, operator_id, reason_id=None):
            if reason_id:
                param = {'id': reason_id}
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operators/id/{}/archive".format(operator_id), param))

        def unarchive(self, operator_id):
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operators/id/{}/unarchive".format(operator_id), None))

    class _operatorgroup:
        
        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)
        
        def get_operators(self, operatorgroup_id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operatorgroups/id/{}/operators".format(operatorgroup_id)))

        def get_list(self, archived=False, page_size=100, query=None):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operatorgroups", archived, page_size, query))

        def get_id_operatorgroup(self, query):
            result = self.get_list()
            canidates = list()
            for operatorgroup in result:
                if re.match(rf"(.+)?{query}(.+)?", operatorgroup['groupName'], re.IGNORECASE):
                    canidates.append(operatorgroup['id'])

            return self.utils.print_lookup_canidates(canidates)

        def create(self, groupName, **kwargs):
            kwargs['groupName'] = groupName
            return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/operatorgroups", (self.utils.add_id_jsonbody(**kwargs))))

        def update(self, operatorgroup_id, **kwargs):
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operatorgroups/id/{}".format(operatorgroup_id), self.utils.add_id_jsonbody(**kwargs)))

        def archive(self, operatorgroup_id, reason_id=None):
            if reason_id:
                param = {'id': reason_id}
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operatorgroups/id/{}/archive".format(operatorgroup_id), param))

        def unarchive(self, operatorgroup_id):
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operatorgroups/id/{}/unarchive".format(operatorgroup_id), None))

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

        def create(self, name, **kwargs):
            kwargs['name'] = name
            return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/branches", self.utils.add_id_jsonbody(**kwargs)))

        def update(self, branche_id, **kwargs):
            return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/branches/id/{}".format(branche_id), self.utils.add_id_jsonbody(**kwargs)))
            
    class _operational_activities:
        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)

        def get_list(self, **kwargs):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operationalActivities", extended_uri=kwargs))

        def get(self, id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operationalActivities/{}".format(id)))

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

    class _budgetholder:

        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)

        def get(self):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/budgetholders"))

        def create(self, name, **kwargs):
            kwargs['name'] = name
            return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/branches", self.utils.add_id_jsonbody(**kwargs)))

    def get_countries(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/countries"))    

    def get_archiving_reasons(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/archiving-reasons"))

    def get_timespent_reasons(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/timespent-reasons"))

    def get_permissiongroups(self):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/permissiongroups"))


if __name__ == "__main__":
    pass
