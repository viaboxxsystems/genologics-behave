# from pyclarity_lims.lims import Lims
from pyclarity_lims.lims import *
from pyclarity_lims.entities import *
from behave import *
# xml = '<?xml version="1.0" encoding="UTF-8"?><smp:samplecreation xmlns:smp="http://genologics.com/ri/sample"><name>Example Sample</name><project uri="http://localhost:8080/api/v2/projects/ADM243"></project><location><container uri="http://localhost:8080/api/v2/containers/27-100001"></container><value>1:1</value></location></smp:samplecreation>'
@Given('retrieve from {sample_index} and {workflow_index} and take the {nth} from this worflow')
def get_stage_from_index(context, sample_index,workflow_index,nth):
	context.l = Lims('https://lims.local.viaboxxsystems.de', 'admin' , 'apassword')
	for row in context.table:
		sample = context.l.get_samples()[int(row['sample_index'])]
	# container = l.get_containers()[0]
	# project = l.get_projects()[0]
	# Retrieve samples/artifact/workflow stage
		context.art = sample.artifact
	# Find workflow 'workflowname' and take its first stage
		context.stage = context.l.get_workflows()[int(row['workflow_index'])].stages[int(row['nth'])]




# Queue the artifacts to the stage
# l.route_artifacts([art],stage_uri= stage.uri)
@Given('find {nth} reagent catagory')
# Find reagent catagory
def get_reagent_catagory(context, nth):
	for row in context.table:
		reagentc = context.l.get_reagent_types()[int(row['nth'])].category

# # Create a new step from that queued artifact
# s = Step.create(l, protocol_step = stage.step, inputs = [art], container_type_name = '96 well plate')

# # Create container
# ct = l.get_container_types(name='96 well plate')[0]
# print(ct)
# c = Container.create(l, type=ct)

# # Retrieve the output artifact that was generated automatically from the input/output map
# print(s.details.input_output_maps)
# output_art = s.details.input_output_maps[0][1]['uri']
# # Place the output artifact in the container

# # Note that the placements is a list of tuples ( A, ( B, C ) ), where A is the output artifact,
# # B is the output Container and C is the location on this container
# output_placement_list=[(output_art, (c, 'B:1'))]
# print(output_placement_list)
# # set_placements creates the placement entity and "put"s it
# s.set_placements([c], output_placement_list)

# # Move from "Record detail" window to the "Next Step"
# s.advance()

# # # Set the next step
# # actions = s.actions.next_actions[0]['action'] = 'complete'
# # s.actions.put()
# # # Complete the step
# s.advance()