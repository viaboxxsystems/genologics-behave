from behave import *
from login import *

import codecs
import configparser
import os 
from genologics.lims import * 
from genologics.config import *
from genologics.entities import * 

# Date = '2012-05-30'
# LIMSid = 'CON1'

@then('check all projects')
def get_all(context):
	lims = login(context)
	projects = lims.get_projects()
	assert len(projects) > 0 
	# print(len(projects), 'projects in total')

@then('get project by id with {LIMSid}')
def getp1(context, LIMSid):
	lims = login(context)
	for row in context.table:
		project = Project(lims, id = row['LIMSid'])
		assert project is not None
	# context.project = project

		# print (project, project.name, project.open_date, project.close_date)
	# print ('    UDFs:')
	# for key, value in project.udf.items():
	#     if isinstance(value, unicode):
	#         value = codecs.encode(value, 'UTF-8')
	#     print (' ', key, '=', value)

	# udt = project.udt
	# print ('    UDT:', udt.udt)
	# for key, value in udt.items():
	#     if isinstance(value, unicode):
	#         value = codecs.encode(value, 'UTF-8')
	#     print (' ', key, '=', value)
	for file in project.files:
		if file.id :
			return file.content_location, file.original_location

@then('get project by opendate with {opendate}')
def getp1(context, opendate):
	lims = login(context)
	for row in context.table:
		projects = lims.get_projects(open_date = row['opendate'])
		assert len(projects) > 0
		# print (len(projects), 'projects opened since', opendate)
	


