from behave import *
import codecs
import configparser
import os
import sys
print(sys.path)
from genologics import lims   
from genologics import config
from genologics import entities

@given('login')
def login(context):
	BASEURI, USERNAME, PASSWORD, _, _ = config.load_config(sys.path[0] + '/genologics.conf')
	limslogin = lims.Lims(BASEURI,USERNAME,PASSWORD)
	# assert 
	limslogin.check_version() 
	#!= None

	return limslogin

