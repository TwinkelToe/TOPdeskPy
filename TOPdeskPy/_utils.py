import re, requests, json, urllib.parse

class utils:

    def __init__(self, topdesk_url, credpair):
        self._topdesk_url = topdesk_url
        self._credpair = credpair
        self._partial_content_container = []

    def is_valid_uuid(self, uuid):
        return re.match(r"^[0-9a-g]{8}-([0-9a-g]{4}-){3}[0-9a-g]{12}$", uuid)

    def is_valid_incident_id(self, id):
        return re.match(r"^[0-9a-g]{8}-([0-9a-g]{4}-){3}[0-9a-g]{12}$", id)

    def is_valid_incident_number(self, number):
        return re.match(r"^\d{6}-\d{3}(\d?){2}$", number)
    
    def is_valid_email_addr(self, email_addr):
        return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_addr)

    def print_lookup_canidates(self, possible_canidates):
        if len(possible_canidates) == 1:
            return possible_canidates[0]
        elif len(possible_canidates) > 1:
            print("To many canidates: " + "; ".join(possible_canidates))
            return 
        else:
            print("No canidates found.")
            return

    def handle_topdesk_response(self, response):        
        if response.status_code == 200 or response.status_code == 201:
            # response = response.json()
            if not self._partial_content_container:
                if response.text == "":
                    return "Success"
                else:
                    return response.json()
            else:
                self._partial_content_container += response.json()
                placeHolder = self._partial_content_container
                self._partial_content_container = []
                return placeHolder
        elif response.status_code == 404:
            print ("status_code {}, message: {}".format('404', 'Not Found'))
            return
        elif response.status_code == 204:
            print ("status_code {}, message: {}".format('204', 'No content'))
            return "success"
        elif response.status_code == 405:
            print ("status_code {}, message: {}".format('405', 'Method not allowed'))
            return
        # Partial content returned.
        elif response.status_code == 206:
            # can we make this recursive?
            self._partial_content_container += response.json()

            page_size = int(re.findall(r'page_size=(\d+)', response.url)[0])   # Page size none crashes here.
            if 'start=' in response.url:
                # Start allready in url replace value.
                current_start = int(re.findall(r'start=(\d+)', response.url)[0])
                self.new_start = page_size + current_start
                partial_new_url = re.sub(r'start=(\d+)', 'start={}'.format(str(self.new_start)), response.url)
            else:
                # start= not yet present in URL. insert it.
                partial_new_url = re.sub(r'(page_size=\d+)', r'\1&start=RaNdOmStRing', response.url)
                partial_new_url = partial_new_url.replace("RaNdOmStRing", str(page_size))
            # Remove base url
            partial_new_url = partial_new_url.replace(self._topdesk_url, "")
            return self.handle_topdesk_response(self.request_topdesk(partial_new_url))
        else:
            # general failure
            status_code = response.status_code
            response = response.json()
            if 'errors' in response:
                print ("status_code {}, message: {}".format(status_code, response['errors'][0]['errorMessage']))
            else:
                print ("status_code {}, message: {}".format(status_code, response[0]['message']))
            
            #return {"status_code" : self.status_code, "message" : self.response[0]['message']}
            return
    
    def request_topdesk(self, uri, archived=None, page_size=None, query=None, custom_uri=None, extended_uri=None):
        headers = {'Authorization':"Basic {}".format(self._credpair), "Accept":'application/json'}
        if custom_uri:
            uri += urllib.parse.urlencode(custom_uri, quote_via=urllib.parse.quote_plus)
        else:
            if page_size:
                uri += "?page_size={}".format(page_size)
            if extended_uri:
                uri += "&" + urllib.parse.urlencode(extended_uri, quote_via=urllib.parse.quote_plus)
            if archived:
                if 'page_size' in uri:
                    uri += '&'
                else:
                    uri += '?'
                uri += 'query=archived=={}'.format(archived)
            if query:
                #Some query param need to be URL encoded.
                query = urllib.parse.quote(query)
                if ('query=' in uri):
                    uri += ';{}'.format(query)
                elif 'page_size' in uri:
                    uri += '&query={}'.format(query)
                else:
                    uri += '?query={}'.format(query)
        return requests.get(self._topdesk_url + uri, headers=headers)

    def post_to_topdesk(self, uri, json_body):
        headers = {'Authorization':"Basic {}".format(self._credpair), "Accept":'application/json', \
            'Content-type': 'application/json'}
        return requests.post(self._topdesk_url + uri, headers=headers, json=json_body)

    def put_to_topdesk(self, uri, json_body):
        headers = {'Authorization':"Basic {}".format(self._credpair), "Accept":'application/json', \
            'Content-type': 'application/json'}
        return requests.put(self._topdesk_url + uri, headers=headers, json=json_body)

    def delete_from_topdesk(self, uri, json_body):
        headers = {'Authorization':"Basic {}".format(self._credpair), "Accept":'application/json', \
            'Content-type': 'application/json'}
        return requests.delete(self._topdesk_url + uri, headers=headers, json=json_body)

    def add_id_list(self, id_list):
        param = []
        for item in id_list:
            param.append({'id': item})
        return param

    def add_id_jsonbody(self, **kwargs):
        request_body = {}
        
        # args = posible caller
        if 'caller' in kwargs:            
            if self.is_valid_email_addr(kwargs['caller']):
                caller_type = "email"
            elif self.is_valid_uuid(kwargs['caller']):
                caller_type = "id"
            else:
                caller_type = "dynamicName"
            request_body['callerLookup'] = { caller_type: kwargs['caller']}

        for key in kwargs:
            if self.is_valid_uuid(str(kwargs[key])):
                request_body[key] = { 'id' : kwargs[key] }
            else:
                if key == 'caller': 
                    continue
                request_body[key] = kwargs[key]
        return request_body

if __name__ == "__main__":
    pass