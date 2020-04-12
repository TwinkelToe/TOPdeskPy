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

# Archive
topdesk.get_archiving_reasons()
topdesk.person.archive('7b451fe2-77d3-4aa2-876e-8bdaea430df9', 'f79b0075-ce02-5bb8-be68-c7857240ebfc')
topdesk.person.unarchive('7b451fe2-77d3-4aa2-876e-8bdaea430df9')

