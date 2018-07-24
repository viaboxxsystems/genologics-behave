from behave import *
from login import *

import codecs
import configparser
import os 
from genologics.lims import * 
from genologics import config
from genologics import entities 

@given('get sample conditions')
def post(context):
	lims = log(context)
	sample = Sample(lims, id='CON1A2')
	print (sample, sample.name)

	sample.name = 'testforthis11.05'
	print(sample,sample.name)

	# Set the value of one of the UDFs
	# sample.udf['Emmas field 2'] = 5
	# for key, value in sample.udf.items():
	#     print ' ', key, '=', value

	# sample.put()
	# print 'Updated sample', sample

		