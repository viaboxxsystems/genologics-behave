from behave import *
from login import *

import codecs
import configparser
import os 

from genologics.lims import * 
from genologics import config
from genologics import entities 


@then('check all artifacts')
def get_all(context):
	lims = login(context)
	artifacts = lims.get_artifacts()
	assert len(artifacts) > 0
	print (len(artifacts), 'total artifacts')
	artifacts = lims.get_batch(artifacts)
	assert artifacts is not None
	for artifact in artifacts:
		print (artifact, artifact.name, artifact.state)


@then("get artifacts of id conditions by {LIMSid}")
def get(context, LIMSid):
	lims = login(context)
	for row in context.table:
		artifacts = lims.get_artifacts(samplelimsid = row['LIMSid'])
		assert artifacts is not None
		artifacts = lims.get_batch(artifacts)
		assert artifacts is not None
		for artifact in artifacts:
			print (artifact, artifact.name, artifact.state)

@then("get artifacts of conditions by {qc_status}")
def get(context, qc_status):
	lims = login(context)
	for row in context.table:
		artifacts = lims.get_artifacts(qc_flag = row['qc_status'])
		print(len(artifacts) )
	#context.artifacts = artifacts
		assert len(artifacts) > 0
		artifacts = lims.get_batch(artifacts)
		assert artifacts is not None
		for artifact in artifacts:
			print (artifact, artifact.name, artifact.state)

