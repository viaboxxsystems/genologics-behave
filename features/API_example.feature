Feature: LIMS API example test
    @containers
    Scenario: get containers 
        Given login
        Then check all containers 
        Then get containers by <type> and <state>
           | type                      | state      |
           | 96 well plate             | Populated  |
           | BioAnalyzer RNA Nano Chip | Populated  |
        Given a container of type <container_type> with name <container_name>
           | container_type            | container_name   |
           | Illumina Flow Cell        | 0                |
           | Tube                      | 27-55            |
        Given a set of samples in the project <project> in the tubes with prefix <tube_prefix>
           | project          | tube_prefix  |
           | CON51            | tt           |
           | ADM101           | tt           |
    @artifacts
    Scenario: get artifacts
        Given login
        then check all artifacts 
        Then get artifacts of id conditions by <LIMSid>
           | LIMSid   |
           | 92-462   |
        And get artifacts of conditions by <qc_status> 
          | qc_status |
          | PASSED    |   

    @applications
    Scenario: get applications 
        Given login
        Then get project of application by id with <LIMSid> and udf area
           | LIMSid   |
           | CON1     |
        
    @labs
    Scenario: get labs
        Given login
        Then check all labs 
        And get labs by id with <Labid>
          | Labid   |
          | CON1    |

        

    @samples
    Scenario: get samples
        Given login
        Then check all samples
        And get the sample by id with <LIMSid>
          | LIMSid   |
          | CON1A194 |
          | CON1     |
        And get the sample by name with <name>
          | name          |
          | Kidney-9267E5 |
        


    @projects
    Scenario: get projects
        Given login   
        Then check all projects
        And get project by id with <LIMSid> 
          | LIMSid   |
          | CON1     |
        And get project by opendate with <opendate>
          | opendate    |
          | 2014-07-08  |



    @processes
    Scenario:get processes
        Given login
            Then check all processes
            And get sample of <LIMSid> processes


    @set_project_queued
    Scenario:set project
        Given login
        Given get project conditions

    @set_sample_name
    Scenario:set sample name
        Given login
        Given get sample conditions 


   


        
