from behave import *
from login import *

import codecs
import configparser
import os 
from genologics import lims 
from genologics import config
from genologics import entities 

@given ('project with name {project_name} exist')
def checkproject(context, project_name):
	api = login(context)
	project_list = api.get_projects(name=context.table.row['project_name'])
	assert isinstance(project_list, list)
	assert len(project_list) > 0

@then ('create sample with {sample_name} store in container {container_name} and classify in project {project_name}')
def createnewsamples(context, sample_name, container_name, project_name):
	containers = create_containers(login(context),
								   len(context.table.rows),
								   container_name)
	project = get_project(login(context), project_name)

	samples = []
	i = 0
	for row in context.table:
		samples.append(generate_sample(login(context),
									   project,
									   containers[i],
									   "1:1",
									   row))
		i += 1
	assert len(samples) == len(context.table.rows)
	assert len(samples) == len(containers)
	# context.containers = containers
	# context.samples = samples

def generate_sample(api: lims.Lims,
					project: entities.Project,
					container: entities.Container,
					well: str,
					row) :
	sample = entities.Sample.create(lims=api,
									container=container,
									position=well,
									project=project,
									name=row["name"])
	sample.put()
	return sample

def create_containers(api: lims.Lims,
					  size: int,
					  container_name: str):
	type_element = api.get_container_types(name="Tube")
	assert isinstance(type_element, list)
	assert len(type_element) == 1
	container_list = []
	for i in range(size):
		container = entities.Container.create(lims=api,
											  name="{}_{}".format(container_name, i),
											  type=type_element[0])
		container_list.append(container)
	return container_list

def get_project(api: lims.Lims,
				project_name: str):
	project = api.get_projects(name=project_name)
	assert isinstance(project, list)
	print(len(project))
	assert len(project) == 2
	return project[0]