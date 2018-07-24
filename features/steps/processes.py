from behave import *
from login import *

import codecs
import configparser
import os 
from genologics.lims import * 
from genologics import config
from genologics import entities 
LIMSid = ''

@then('check all processes')
def all_get(context):
	api = login(context)
	processes = api.get_processes()
	assert len(processes) > 0


@then('And get sample of {LIMSid} processes')
def get(context,LIMSid):
	api = login(context)
	process = Process(api, id = LIMSid)
	print (process, process.id, process.type, process.type.name)
	for input, output in process.input_output_maps:
		if input:
			return input.items()
		if output:
			return output.items()
