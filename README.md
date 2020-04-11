# TOPdeskPy
 Python package to interact with the TOPdesk API

Currently in a very initial stage. Mostly incidents and persons are supported. 

Initeraction with incidents:
```python
import TOPdeskPy

topdesk = TOPdeskPy.connect("https://url.topdesk.net", "API username", "API password")

# Create a new incident
incident_parm = {}
incident_parm['status'] =  'secondLine'
incident_parm['briefDescription'] =  "Small problem"
incident_parm['impact'] = topdesk.incident.get_id_impact('Raakt <10 gebr')
incident_parm['operatorGroup'] = topdesk.operatorgroup.get_id_operatorgroup('netwerkbeheer')
incident_parm['priority'] = topdesk.incident.get_id_priority('2')
incident_parm['callType'] = topdesk.incident.get_id_callType('verzoek')
incident_parm['urgency'] = topdesk.incident.get_id_urgency('kan verder')
incident_parm['entryType'] =  topdesk.incident.get_id_entryType('mail')
incident_parm['request'] = 'My computer is on fire.'
incident_parm['object'] = {"name": "039662"}
topdesk.incident.create('m.laadvermogen@company.nl', **incident_parm)

# # Update an incident
update2_parm = {}
update2_parm['actionInvisibleForCaller'] = True
update2_parm['action'] = "This guy..."
topdesk.incident.update('200410-004', **update2_parm)

# # Get a single incident
topdesk.incident.get_number("200410-004")

# Get a list of incidents based on a filter
incident_list = {}
incident_list['status'] = 'secondLine'
incident_list['completed'] = False
incident_list['operator_group'] =  topdesk.operatorgroup.get_id_operatorgroup('Eduarte')
result = topdesk.incident.get_list(**incident_list)
print('')
```

Interacting with persons:
```python 
import TOPdeskPy

topdesk = TOPdeskPy.connect("https://url.topdesk.net", "API username", "API password")

# Create a new user
person_parm = {}
person_parm['surName'] = "Kees"
person_parm['firstName'] = "Test"
person_parm['jobTitle'] = "Testcase"
person_parm['branch'] = topdesk.branche.get_list(query="name==Brandenburchdreef")[0]['id']
topdesk.person.create(**person_parm)

# List users using FQIL
topdesk.person.get_list(query="dynamicName=='laadvermogen, max'")
topdesk.person.get('f0971929-aa4c-4eec-8d12-202215e1aa72')

# Update a person
person_update_parm = {}
person_update_parm['jobTitle'] = "Director of Things"
topdesk.person.update('f0971929-aa4c-4eec-8d12-202215e1aa72', **person_update_parm)

# Get a list of persons using FQIL
topdesk.person.get_list(query="isManager==true;branch.name==Brandenburchdreef")
