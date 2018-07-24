Feature: LIMS API example test 2
    @test
    Scenario: get and post 
        Given project with name <project_name> exist
           | project_name      | 
           | Testproject0      |
        Then create sample with <sample_name> store in container <container_name> and classify in project <project_name>
           | sample_name     | container_name   | project_name  |
           | test01          | container01      | Testproject0  |
        