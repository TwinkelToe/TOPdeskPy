import TOPdeskPy

topdesk = TOPdeskPy.connect("https://url.topdesk.net", "API username", "API password")

# Create operator
operator_param = {}
operator_param['firstName'] = 'test'
operator_param['title'] = 'Master of none'
operator_param['branch'] = topdesk.branche.get_list(query='name==Brandenburchdreef')[0]['id']
topdesk.operator.create('kees', **operator_param)

# update
operetor_update = {}
operetor_update['problemManager'] = True
topdesk.operator.update(topdesk.operator.get_id_operator("kees, test"), **operetor_update)

# get operator
topdesk.operator.get_list(query="dynamicName=='Kees, test'")
topdesk.operator.get_id_operator("kees, test")

# get operatorgroups of operator
topdesk.operator.get_operatorgroups(topdesk.operator.get_id_operator('kees, test'))

# link operatorgroups to operator
topdesk.operator.link_operetorgroups(topdesk.operator.get_id_operator('kees, test'), [topdesk.operatorgroup.get_id_operatorgroup('eduarte')])
topdesk.operator.unlink_operetorgroups(topdesk.operator.get_id_operator('kees, test'), [topdesk.operatorgroup.get_id_operatorgroup('eduarte')])

# Link, get and unlink filters. Requires filter id
topdesk.operator.filters.get_category_list()
topdesk.operator.filters.link_category(topdesk.operator.get_id_operator('kees, test'), ['4a952bed-be13-437c-a96e-d25a11c6eabe', 'dc03788b-95ec-429a-9653-37f9444cd7ea'])
topdesk.operator.filters.unlink_category(topdesk.operator.get_id_operator('kees, test'), ['4a952bed-be13-437c-a96e-d25a11c6eabe', 'dc03788b-95ec-429a-9653-37f9444cd7ea'])

# Archive (needs reason, needs rason id if no deafault is set)
topdesk.get_archiving_reasons()
topdesk.operator.archive('7b451fe2-77d3-4aa2-876e-8bdaea430df9', 'f79b0075-ce02-5bb8-be68-c7857240ebfc')
topdesk.operator.unarchive('7b451fe2-77d3-4aa2-876e-8bdaea430df9')