[Documentation] Generic-tests (aka keywords) for the RPy writer

*** Keywords ***
MockRead ${file}
                LOG  MockRead:: ${file}
    ${AIGR}=    Read and include ${file}    # ToDo (in python)
                RETURN  ${AIGR}


RPY generates code for ${AIGR}
                Given a valid basic ${AIGR}         # check it is valid (V0.0:skip)
    ${main}=    When the castle-RPy-writer is called with ${AIGR}
                RETURN  ${main}

Then the ${code} is valid rPython
    call rpython for ${code}



# MOCKS  -- implement in python

a valid basic ${AIGR}
    [Documentation]   check it is valid (V0.0:skip)
    RETURN  True

When the castle-RPy-writer is called with ${AIGR}
    [Documentation]   implement in python
    RETURN  True

Read and include ${file}
    [Documentation]   implement in python
    RETURN      dummy AIGR

call rpython for ${code}
    [Documentation]   implement in python
    RETURN  True

RPY compiles it for ${AIGR}
    [Documentation]   implement in python
    RETURN  dummy exe

runs ${prog} with @{ARGV}
    [Documentation]   implement in python
    RETURN  dummy actuals

THEN ${outp} matches ${EXPECTATION}, given @{FILTERS}
    [Documentation]   implement in python
    RETURN  True
