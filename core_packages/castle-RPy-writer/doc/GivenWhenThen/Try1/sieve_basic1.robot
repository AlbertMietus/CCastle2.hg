[Documentation] Test the RPy-writer with sieve/basic1

*** Variables ***
${SIEVE_FILE}        sieve/basic1
@{ARGV}              --max 25
@{FILTERS}
@{EXPECTATION}       2  3  5  7  11  13  17  19  23

*** Settings ***
Resource      ./top.robot

*** Test Cases ***
Valid rpython for sieve
    ${AIGR}=    Given MockRead ${SIEVE_FILE}
    ${code}=    When RPY generates code for ${AIGR}
                Then the ${code} is valid rPython


Run Sieve
    ${AIGR}=    Given MockRead ${SIEVE_FILE}
    ${prog}=    When RPY compiles it for ${AIGR}
    @{outp}=    And runs ${prog} with @{ARGV}
    		Then @{outp} matches ${EXPECTATION}, given @{FILTERS}


