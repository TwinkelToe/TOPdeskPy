import TOPdeskPy

topdesk = TOPdeskPy.connect("https://url.topdesk.net", "API username", "API password")

# Create operatorgroupo
operatorgroup_param = {}
operatorgroup_param['branch'] = topdesk.branche.get_list(query='name==Brandenburchdreef')[0]['id']
topdesk.operator.create('Me myself and i', **operatorgroup_param)

# update
update = {}
update['groupName'] = 'Myself and i'
topdesk.operatorgroup.update(topdesk.operatorgroup.get_id_operatorgroup('Me myself and i'), **update)

# get operator
topdesk.operatorgroup.get_list(query="dynamicName=='Kees, test'")
topdesk.operatorgroup.get_id_operatorgroup("Eduarte")

# get operator of operatorgroups
topdesk.operatorgroup.get_operators(topdesk.operatorgroup.get_id_operatorgroup('eduarte'))

# Archive (needs reason, needs rason id if no deafault is set)
topdesk.get_archiving_reasons()
topdesk.operatorgroup.archive('7b451fe2-77d3-4aa2-876e-8bdaea430df9', 'f79b0075-ce02-5bb8-be68-c7857240ebfc')
topdesk.operatorgroup.unarchive('7b451fe2-77d3-4aa2-876e-8bdaea430df9')