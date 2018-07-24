Feature: pyclarityLIMS API 
	Scenario: forward the steps to next
		Given retrieve the workflow and take its first stage 
		and queue the artifacts to the stage
		When need to create active Lot for the following steps
		Then create a new step from queued artifact
		and create the ouput container
		Then retrieve the output artifact that was generated automatically form the input/output map
		and pleace the output artifact in the container 
		and create the placement entity and put it 
		Then move from "Record Detail" window to the "Next Step"
		and Set the next step
		Then complete the step 




		