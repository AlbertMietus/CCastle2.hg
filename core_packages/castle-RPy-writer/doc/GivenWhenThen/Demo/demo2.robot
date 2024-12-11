*** Test Cases ***
Embedded arguments
    Select cat from list
    Select dog from list

*** Keywords ***
Select ${animal} from list
    Open Page    Pet Selection
    Select Item From List    animal_list    ${animal}
