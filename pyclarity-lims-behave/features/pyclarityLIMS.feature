Feature: pyclarityLIMS API 
	@
	Scenario: forward the steps to next
		Given retrieve from <sample> and <workflow> and take its first stage
			| sample            | worflow                   |
        	| Kidney-1997G3     | TruSeq DNA for HiSeq 5.0  | 
        
        Given queue the artifacts to the stage   
		When need to create active <lot> with <name> <expiry_date> <status> <lot_number> for the following steps
			| lot                                         | name             | expiry_date | status | lot_number |
			| Covaris Snap-cap microTUBE                  | test_2906_Cov    | 2020-12-31  | ACTIVE | 9999999    | 
			| TruSeq DNA PCR-Free Kit - Core Reagents Box | test_2906_TruSeq | 2020-12-31  | ACTIVE | 9999998    |
		Then create a new step by <container_type_name> from queued artifact
			| container_type_name       |
			| BioAnalyzer DNA 1000 Chip |
		and create the ouput container by <container_type_name>
			| container_type_name       |
			| BioAnalyzer DNA 1000 Chip |
		Then retrieve the output artifact that was generated automatically form the input/output map
		and <pleace> the output artifact in the container 
			| pleace |
			| A:1    |
		and create the placement entity and put it 
		Then move from "Record Detail" window to the "Next Step"
		and Set the next step
		Then complete the step 


	@test
	Scenario: test on blank database
	Given retrieve from <sample_index> and <workflow_index> and take the <nth> from this workflow
        	| sample_index | workflow_index | nth |
        	| 0            | 1              | 1   |   
    Given queue the artifacts to the stage
    Given find <nth> reagent catagory 
    		| nth |
    		| 2   |	
    Then create a new step and the output container by <container_type_name> from queued artifact
   			| container_type_name     |
			| 96 well plate |
	Then retrieve the output artifact that was generated automatically form the input/output map
	and <pleace> the output artifact in the container 
			| pleace |
			| B:1    |
	and create the placement entity and put it 
	and Set the next step
		Then complete the step 



		