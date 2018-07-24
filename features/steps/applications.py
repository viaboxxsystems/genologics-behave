from behave import *
from login import *

import codecs
import configparser
import os 

from genologics.lims import * 
from genologics import config
from genologics import entities 

@then('get project of application by id with {LIMSid} and udf area')
def get(context, LIMSid):
	lims = login(context)
	for row in context.table:
		project = Project(lims, id = row['LIMSid'])
		assert project is not None
		print(project)
		assert project.udf.items() is not None
		print(project.udf.items())
	return project
		


