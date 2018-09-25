import sys 
from pyclarity_lims.lims import *
import pyclarity_lims.entities as en
from behave import *

@Given('retrieve from {sample} and {workflow} and take its first stage')
def get_workfolw_stage(context, sample, workflow):
	context.l = Lims('https://lims.local.viaboxxsystems.de', 'admin' , 'apassword')
	samples = context.l.get_samples(name=sample)
	assert len(samples) > 0
	workflow = context.l.get_workflows(name=workflow)[0]
	assert len(workflow) > 0
	context.stage = workflow.stages[0]
	context.art = samples[0].artifact
	context.l.route_artifacts([context.art], stage_uri=stage.uri)

@Given('retrieve from {sample_index} and {workflow_index} and take the {nth} from this workflow')
def get_stage_from_index(context, sample_index, workflow_index, nth):
	context.l = Lims('https://lims.local.viaboxxsystems.de', 'admin' , 'apassword')
	for row in context.table:
		sample = context.l.get_samples()[int(row['sample_index'])]
	# container = l.get_containers()[0]
	# project = l.get_projects()[0]
	# Retrieve samples/artifact/workflow stage
		context.art = sample.artifact
	# Find workflow 'workflowname' and take its first stage
		context.stage = context.l.get_workflows()[int(row['workflow_index'])].stages[int(row['nth'])]


@given('queue the artifacts to the stage')
def queue_workflow_status(context):
	context.l.route_artifacts([context.art],stage_uri= context.stage.uri)
	context.art.workflow_stages[0].status = 'queued'


@When('need to create active {lot} with {name} {expiry_date} {status} {lot_number} for the following steps')
def create_active_Lot(context, lot, name, expiry_date, status, lot_number):
	for row in context.table:
		reagentkit = context.l.get_reagent_kits(name = row['lot'])[0]
	# 1uri = reagentkit1.get_uri()
	# reagentkit2 = context.l.get_reagent_kits(name = 'TruSeq DNA PCR-Free Kit - Core Reagents Box')[0]
		lot = ReagentLot.create(context.l, reagent_kit = reagentkit, name = row['name'], expiry_date = row['expiry_date'], status = row['status'], lot_number = row['lot_number'])
	# lot2 = ReagentLot.create(context.l, reagent_kit = reagentkit2, name = 'TruSeq DNA PCR-Free Kit - Core Reagents Box - jiuntest2906', expiry_date = '2020-12-31', status = 'ACTIVE', lot_number = 9999998)

@Given('find {nth} reagent catagory')
# Find reagent catagory
def get_reagent_catagory(context, nth):
	for row in context.table:
		context.reagentc = context.l.get_reagent_types()[int(row['nth'])].category

@Then('create a new step and the output container by {container_type_name} from queued artifact')
def create_new_steps_and_output_container(context, container_type_name):
	for row in context.table:
		context.s = en.Step.create(context.l, protocol_step=context.stage.step, inputs=[context.art], container_type_name=row['container_type_name'],reagent_category = context.reagentc)
		# context.s.status = 'queued'
		ct = context.l.get_container_types(name = row['container_type_name'])[0]
		context.c = en.Container.create(context.l, type=ct)

@Then('retrieve the output artifact that was generated automatically form the input/output map')
def retrieve_output_artifact(context):
	context.output_art = context.s.details.input_output_maps[0][1]['uri']

@then('{pleace} the output artifact in the container')
def pleace_output_artifact(context, pleace):
	for row in context.table:
		context.output_placement_list=[(context.output_art, (context.c, row['pleace']))]

@then('create the placement entity and put it') 
def create_entity(context):
	context.s.set_placements([context.c], context.output_placement_list)

@Then('move from "Record Detail" window to the "Next Step"')
def move_to_next_step(context):
	context.s.advance()

@then('Set the next step')
def set_next_step(context):
	actions = context.s.actions.next_actions[0]['action'] = 'nextstep'
	context.s.actions.put()

@Then('complete the step') 
def complete(context):
	context.s.advance()