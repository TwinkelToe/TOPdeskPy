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
topdesk.incident.get_list(**incident_list)

# actions
topdesk.incident.action.get_list('200211-001')
topdesk.incident.action.get('200211-001', '3067f000-1916-4a29-aa79-2dc99c677108')
topdesk.incident.action.delete('200211-001', '3067f000-1916-4a29-aa79-2dc99c677108')

# Requests
topdesk.incident.request.get_list('200211-001')
topdesk.incident.request.get('200211-001', '3067f000-1916-4a29-aa79-2dc99c677108')
topdesk.incident.request.delete('200211-001', '3067f000-1916-4a29-aa79-2dc99c677108')

# Escalate and deescalte
topdesk.incident.escalation_reasons()
topdesk.incident.deescalation_reasons()
topdesk.incident.escalate('200211-001')
topdesk.incident.escalate('200211-001', '6467f000-1916-4a29-aa74-2dc99c677181')
topdesk.incident.deescalate('200211-001')
topdesk.incident.deescalate('200211-001', '6467f000-1916-4a29-aa74-2dc99c677181')