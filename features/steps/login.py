from behave import *
import codecs
import configparser
import os 
from os.path import expanduser
home = expanduser("~")
from genologics import lims   
from genologics import config
from genologics import entities

@given('login')
def login(context):
	BASEURI, USERNAME, PASSWORD, _, _ = config.load_config(specified_config = home +'/genologics.conf')
	limslogin = lims.Lims(BASEURI,USERNAME,PASSWORD)
	# assert 
	limslogin.check_version() 
	#!= None

	return limslogin
