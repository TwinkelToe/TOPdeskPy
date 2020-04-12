from . import _utils
import re

class operator:

    def __init__(self, topdesk_url, credpair):
        self._topdesk_url = topdesk_url
        self._credpair = credpair
        self.utils = _utils.utils(self._topdesk_url, self._credpair)
        self.filters = self._filters(self._topdesk_url, self._credpair)
        
    def get_list(self, archived=False, page_size=100, query=None):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators", archived, page_size, query))

    def get(self, id):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}".format(id)))

    def get_operatorgroups(self, operator_id):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}/operatorgroups".format(operator_id)))

    def get_permissiongroups(self, operator_id):
        return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}/permissiongroups".format(operator_id)))

    def link_permissiongroups(self, operator_id, id_list):
        return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/operators/id/{}/permissiongroups".format(operator_id), self.utils.add_id_list(id_list)))

    def unlink_permissiongroups(self, operator_id, id_list):
        return self.utils.handle_topdesk_response(self.utils.delete_from_topdesk("/tas/api/operators/id/{}/permissiongroups".format(operator_id), self.utils.add_id_list(id_list)))

    def link_operetorgroups(self, operator_id, id_list):
        return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/operators/id/{}/operatorgroups".format(operator_id), self.utils.add_id_list(id_list)))

    def unlink_operetorgroups(self, operator_id, id_list):
        return self.utils.handle_topdesk_response(self.utils.delete_from_topdesk("/tas/api/operators/id/{}/operatorgroups".format(operator_id), self.utils.add_id_list(id_list)))

    def get_id_operator(self, query):
        result = self.get_list()
        canidates = list()
        for operator_dynamic_name in result:
            if re.match(rf"(.+)?{query}(.+)?", operator_dynamic_name['dynamicName'], re.IGNORECASE):
                canidates.append(operator_dynamic_name['id'])

        return self.utils.print_lookup_canidates(canidates)

    def create(self, surName, **kwargs):
        kwargs['surName'] = surName
        return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/operators", (self.utils.add_id_jsonbody(**kwargs))))

    def update(self, operator_id, **kwargs):
        return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operators/id/{}".format(operator_id), self.utils.add_id_jsonbody(**kwargs)))

    def archive(self, operator_id, reason_id=None):
        if reason_id:
            param = {'id': reason_id}
        return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operators/id/{}/archive".format(operator_id), param))

    def unarchive(self, operator_id):
        return self.utils.handle_topdesk_response(self.utils.put_to_topdesk("/tas/api/operators/id/{}/unarchive".format(operator_id), None))

    class _filters:

        def __init__(self, topdesk_url, credpair):
            self._topdesk_url = topdesk_url
            self._credpair = credpair
            self.utils = _utils.utils(self._topdesk_url, self._credpair)

        def get_branch_list(self):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/filters/branch"))

        def get_category_list(self):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/filters/category"))

        def get_operator_list(self):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/filters/operator"))

        def branch_of_operetor(self, operator_id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}/filters/branch".format(operator_id)))

        def category_of_operetor(self, operator_id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}/filters/category".format(operator_id)))

        def operator_of_operetor(self, operator_id):
            return self.utils.handle_topdesk_response(self.utils.request_topdesk("/tas/api/operators/id/{}/filters/operator".format(operator_id)))

        def link_branch(self, operator_id, id_list):                
            return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/operators/id/{}/filters/branch".format(operator_id), self.utils.add_id_list(id_list)))

        def link_category(self, operator_id, id_list):
            return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/operators/id/{}/filters/category".format(operator_id), self.utils.add_id_list(id_list)))

        def link_operetor(self, operator_id, id_list):
            return self.utils.handle_topdesk_response(self.utils.post_to_topdesk("/tas/api/operators/id/{}/filters/operator".format(operator_id), self.utils.add_id_list(id_list)))

        def unlink_branch(self, operator_id, id_list):
            return self.utils.handle_topdesk_response(self.utils.delete_from_topdesk("/tas/api/operators/id/{}/filters/branch".format(operator_id), self.utils.add_id_list(id_list)))

        def unlink_category(self, operator_id, id_list):
            return self.utils.handle_topdesk_response(self.utils.delete_from_topdesk("/tas/api/operators/id/{}/filters/category".format(operator_id), self.utils.add_id_list(id_list)))

        def unlink_operetor(self, operator_id, id_list):
            return self.utils.handle_topdesk_response(self.utils.delete_from_topdesk("/tas/api/operators/id/{}/filters/operator".format(operator_id), self.utils.add_id_list(id_list)))

if __name__ == "__main__":
    pass