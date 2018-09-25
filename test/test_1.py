# from pyclarity_lims.lims import Lims
from pyclarity_lims.lims import *
from pyclarity_lims.entities import *
# xml = '<?xml version="1.0" encoding="UTF-8"?><smp:samplecreation xmlns:smp="http://genologics.com/ri/sample"><name>Example Sample</name><project uri="http://localhost:8080/api/v2/projects/ADM243"></project><location><container uri="http://localhost:8080/api/v2/containers/27-100001"></container><value>1:1</value></location></smp:samplecreation>'
l = Lims('https://lims.local.viaboxxsystems.de', 'admin' , 'apassword')
# sample =  l.get_samples(name = "test_jiun_vr2")
# print(sample)
# # uris = sample.uri
# # print(l.get(uri = uris).tostring())
# container = l.get_containers(type = 'Tube', state = 'Empty')[0]
# # print(container)
# project = l.get_projects()[0]
# # urip = project.uri
# # print(urip)
# def generate_sample(api: l,
# 					project: project,
# 					container: container,
# 					well: str,
# 					name):
# 	sample = Sample.create(lims=api,
# 							container=container,
# 							position=well,
# 							project=project,
# 							name= 'test_jiun_vr2')
	
# 	return sample
# generate_sample(l,
# 				project,
# 				container,
# 				"1:1",
# 				"test_jiun_vr2")


# art = l.get_artifacts(sample_name = 'Kidney-1997G3')
# print(art)

sample = l.get_samples()
container = l.get_containers()[0]
project = l.get_projects()[0]
# print(sample)
# print(container)
# print(project)
# sample_new =  Sample.create(lims = l, container = container, position = "1:1", project = project, name = 'test_from_py' )

# Retrieve samples/artifact/workflow stage
art = sample[0].artifact
# Find workflow 'workflowname' and take its first stage
stage = l.get_workflows()[1].stages[0]
# Queue the artifacts to the stage
# container_type_name = l.get_container_types()
# print(container_type_name)
# print(art)
# print(art.workflow_stages)
print(stage)
print(stage.step)
l.route_artifacts([art],stage_uri= stage.uri)
art.workflow_stages[0].status = 'queued'
# print(art.workflow_stages[0].status)
reagentc = l.get_reagent_types()[2].category
print(reagentc)
# Create a new step from that queued artifact
s = Step.create(l, protocol_step = stage.step, inputs = [art], container_type_name = 'Tube', reagent_category = reagentc)
# s.status = 'queued'
# print(s)
# Create the output container
# print(StepPools.get(l))
# print(s.pools) 
# s2 = s.pooled_inputs
# print(s2)
ct = l.get_container_types(name='Tube')[0]
print(ct)
c = Container.create(l, type=ct)
output_art = s.details.input_output_maps[0][1]['uri']
print(s.details.input_output_maps)
# pooled_inputs = {'pool1':(output_art, )}

# Retrieve the output artifact that was generated automatically from the input/output map
# print(s.details.input_output_maps)
# Place the output artifact in the container
# Note that the placements is a list of tuples ( A, ( B, C ) ), where A is the output artifact,
# B is the output Container and C is the location on this container
output_placement_list=[(output_art, (c, '1:1'))]
# print(output_placement_list)
# # set_placements creates the placement entity and "put"s it
s.set_placements([c], output_placement_list)

# Move from "Record detail" window to the "Next Step"
actions = s.actions.next_actions[0]['action'] = 'complete'
s.actions.put()
s.advance()

# # Set the next step
# # Complete the step
s.advance()