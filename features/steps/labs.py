from behave import *
from login import *

import codecs
import configparser
import os 
from genologics.lims import * 
from genologics import config
from genologics import entities 

@then('check all labs')
def get_all(context):
	lims = login(context)
	labs = lims.get_labs()
	assert lens(labs) > 0
	print(len(labs), 'labs in total')
	#check details
	for lab in labs:
		print (lab, id(lab), lab.name, lab.uri, lab.id)
		print (lab.shipping_address.items())
	for key, value in lab.udf.items():
		if isinstance(value, unicode):
			value = codecs.encode(value, 'UTF-8')

	udt = lab.udt
	if udt:
		print ('UDT:', udt.udt)
		for key, value in udt.items():
			if isinstance(value, unicode):
				value = codecs.encode(value, 'UTF-8')
			print(' ', key, '=', value)

@given('get labs by id with <Labid>')
def get(context):
	lims = login(context)
	lab = Lab(lims, id='2')
	assert lab > 0
	print(lab, id(lab), lab.name, lab.uri, lab.id)



	

