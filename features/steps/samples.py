from login import *

import codecs
import configparser
import os 
from genologics.lims import * 
from genologics import config
from genologics import entities 


@then('check all samples')
def get(context):
	lims = login(context)
	samples = lims.get_samples()
	assert len(samples) > 0
	# sample = samples[0]
	submitter, artifact = [], []
	for sample in samples[:2]:
		submitter.append(sample.submitter)
		artifact.append(sample.artifact)

	return submitter, artifact

@then('get the sample by id with {LIMSid}')
def get(context, LIMSid):
	lims = login(context)
	for row in context.table:
		project = Project(lims, id = row['LIMSid'])
	samples = lims.get_samples(projectlimsid=project.id)
	assert len(samples) > 0
	sample = samples[0]
	assert sample is not None
	return len(samples), project,sample.id, sample.name, sample.date_received, sample.uri
# 	for key, value in sample.udf.items():
#    		print (' ', key, '=', value)
# 	for note in sample.notes:
# 		print (sample.submitter.first_name, sample.artifact.uri,sample.project.id,sample.project.uri)
# 	for file in sample.files:
#    		print ('File', file.content_location)

@then("get the sample by name with {name}")
def get(context, name):
	lims = login(context)
	for row in context.table:
		samples = lims.get_samples(name=row['name'])

	assert len(samples) > 0
	return samples


