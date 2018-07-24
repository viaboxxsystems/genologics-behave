from behave import *
from login import * 

import codecs
import configparser
import os 
from genologics.lims import * 
from genologics import config
from genologics import entities 


@then('check all containers')
def get_all(context):
    lims = login(context)
    containers = lims.get_containers()
    assert len(containers) > 0 
    for container in containers:
        print (container.name)
        print (container.id)
        #print(container.placements)
        print (container.placements.keys())
    arts=lims.get_artifacts(containername=container.name)
    assert arts is not None 
    for art in arts:
        print (art.name)
        print (art.type)
        #print (art.udf.items())
        print (art.parent_process)

@then('get containers by {type} and {state}')
def get(context, type, state):
    lims = login(context)
    for row in context.table:
        containers = lims.get_containers(type=row['type'],state=['state'])
        assert len(containers) > 0 
        print (len(containers))
        container = containers[0]
        print (container, container.occupied_wells)

    placements = container.placements
    for location, artifact in sorted(placements.items()):
        print (location, artifact.name, id(artifact), repr(artifact), artifact.root)

    containertype = container.type
    print (containertype, containertype.name, containertype.x_dimension, containertype.y_dimension)


@given('a container of type "{container_type}" with name "{container_name}"')
def step_impl(context, container_type, container_name):
    api = login(context)
    container_list = api.get_containers(type=container_type,
                                        name=container_name)
    assert isinstance(container_list, list)
    container = None
    if len(container_list) == 0:
        print("Creating non-existent container", container_name)
        type_element = api.get_container_types(name=container_type)
        assert isinstance(type_element, list)
        assert len(type_element) == 1
        container = entities.Container.create(lims=api,
                                              name=container_name,
                                              type=type_element[0])
        container.put()
    else:
        print("Found container", container_name)
        assert len(container_list) == 1
        container = container_list[0]
    assert container is not None
    print(container.id)
    context.container = container
    print(context.container)
        
@given('a set of samples in the project "{project}" in the tubes with prefix "{tube_prefix}"')
def samples_in_temptubes(context, project: str, tube_prefix: str):
    project = get_project(lims.Lims, project)
    containers = create_containers(login(context),
                                   len(context.table.rows),
                                   tube_prefix)
    samples = []
    i = 0
    for row in context.table:
        samples.append(generate_sample(lims.Lims,
                                       project,
                                       containers[i],
                                       "1:1",
                                       row))
        i += 1
    assert len(samples) == len(context.table.rows)
    assert len(samples) == len(containers)
    context.containers = containers
    context.samples = samples

def create_containers(api: lims.Lims,
                      size: int,
                      prefix: str):
    type_element = api.get_container_types(name="Tube")
    assert isinstance(type_element, list)
    assert len(type_element) == 1
    container_list = []
    for i in range(size):
        container = entities.Container.create(lims=api,
                                              name="{}_{}".format(prefix, i),
                                              type=type_element[0])
        container_list.append(container)

def generate_sample(api: lims.Lims,
                    project: entities.Project,
                    container: entities.Container,
                    well: str,
                    row):
    sample = entities.Sample.create(lims=api,
                                    container=container,
                                    position=well,
                                    project=project,
                                    name=row["name"])
    sample.put()
    return sample


