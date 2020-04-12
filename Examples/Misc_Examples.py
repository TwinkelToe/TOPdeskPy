import TOPdeskPy

topdesk = TOPdeskPy.connect("https://url.topdesk.net", "API username", "API password")

topdesk.get_archiving_reasons()
topdesk.get_countries()
topdesk.get_permissiongroups()
topdesk.get_timespent_reasons()

# Create a custom notification
notification_param = {}
notification_param['operatorIds'] = [topdesk.operator.get_id_operator('kees, test')]
notification_param['title'] = "Title of the notification"
topdesk.notification(**notification_param)

# Suppliers
topdesk.supplier.get_list()
topdesk.supplier.get('7b451fe2-77d3-4aa2-876e-8bdaea430df9')

# Branches
topdesk.branche.get_list()
topdesk.branche.get('7b451fe2-77d3-4aa2-876e-8bdaea430df9')

branch_create= {}
branch_create['phone'] = '055471657'
branch_create['website'] = 'www.github.com/twinkeltoe'
topdesk.branche.create('Building', **branch_create)

branch_update = {}
branch_update['email'] = 'user@twinkeltoe.com'
branch_update['specification'] = 'No users on this site'
branch_id = topdesk.branche.get_list(query='name==brandenburchdreef')[0]['id']
topdesk.branche.update(branch_id, **branch_update)

# Locations
topdesk.location.get_list()
topdesk.location.get_list(query='branch.name=="brandenburchdreef"')
topdesk.location.get('7b451fe2-77d3-4aa2-876e-8bdaea430df9')

# Budgetholders
topdesk.budgetholder.get_list()

budget_param = {}
topdesk.budgetholder.create('Super budgetholder', **budget_param)

# Departments
topdesk.department.get_list()

department_param = {}
topdesk.department.create('Super department', **department_param)

# operation activities
topdesk.operational_activities.get_list(**kwargs)
topdesk.operational_activities.get(id)