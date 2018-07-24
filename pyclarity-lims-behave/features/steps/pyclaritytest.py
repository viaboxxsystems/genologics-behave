from pyclarity_lims.lims import *
from pyclarity_lims.entities import *
from behave import *

@Given('retrieve the workflow and take its first stage')
def get_workfolw_stage(context):
	context.l = Lims('https://demo.claritylims.com', 'admin' , 'apassword')
	samples = context.l.get_samples(name="Kidney-1997G3")
	assert len(samples) > 0
	workflow = context.l.get_workflows(name='TruSeq DNA for HiSeq 5.0')[0]
	assert len(workflow) > 0
	stage = workflow.stages[0]
	context.art = samples[0].artifact
	context.l.route_artifacts([context.art], stage_uri=stage.uri)

@given('queue the artifacts to the stage')
def queue_workflow_status(context):
	context.art.workflow_stages.status = 'queued'

@When('need to create active Lot for the following steps')
def create_active_Lot(context):
	reagentkit1 = context.l.get_reagent_kits(name = 'Covaris Snap-cap microTUBE')[0]
	# 1uri = reagentkit1.get_uri()
	reagentkit2 = context.l.get_reagent_kits(name = 'TruSeq DNA PCR-Free Kit - Core Reagents Box')[0]
	lot1 = ReagentLot.create(context.l, reagent_kit = reagentkit1, name = 'Covaris Snap-cap microTUBE - jiuntest2906', expiry_date = '2020-12-31', status = 'ACTIVE', lot_number = 9999999)
	lot2 = ReagentLot.create(context.l, reagent_kit = reagentkit2, name = 'TruSeq DNA PCR-Free Kit - Core Reagents Box - jiuntest2906', expiry_date = '2020-12-31', status = 'ACTIVE', lot_number = 9999998)

@Then('create a new step from queued artifact')
def create_new_steps(context):
	context.s = Step.create(l, protocol_step=stage.protocol.steps[0], inputs=[context.art], container_type_name='BioAnalyzer DNA 1000 Chip')

@then('create the ouput container')
def create_out_container(context):
	ct = l.get_container_types(name='BioAnalyzer DNA 1000 Chip')[0]
	context.c = Container.create(context.l, type=ct)

@Then('retrieve the output artifact that was generated automatically form the input/output map')
def retrieve_output_artifact(context):
	context.output_art = context.s.details.input_output_maps[0][1]['uri']

@then('pleace the output artifact in the container')
def pleace_output_artifact(context):
	context.output_placement_list=[(context.output_art, (context.c, 'A:1'))]

@then('create the placement entity and put it') 
def create_entity(context):
	context.s.set_placements([context.c], context.output_placement_list)

@Then('move from "Record Detail" window to the "Next Step"')
def move_to_next_step(context):
	context.s.advance()

@then('Set the next step')
def set_next_step(context):
	actions = context.s.actions.next_actions[0]['action'] = 'complet=e'
	context.s.actions.put()

@Then('complete the step') 
def complete(context):
	context.s.advance()