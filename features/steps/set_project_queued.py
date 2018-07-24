from behave import *
from login import *
import datetime
import codecs
import configparser
import os 
import sys
sys.path.append("..")
from genologics.lims import * 
from genologics import config
from genologics import entities 

@given('get project conditions')
def post(context):
	global project
	lims = log(context)
	project = Project(lims, id='CON1')
	print (project, project.name, project.open_date)
	print (project.udf.items())

	d = datetime.date(2012,1,2)
	print(d)

	# project.udf['Queued'] = d
	# project.put()
		