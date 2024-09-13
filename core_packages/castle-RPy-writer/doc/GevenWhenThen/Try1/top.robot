[Documentation] Generic-tests (aka keywords) for the RPy writer

*** Keywords ***

Check rPython for ${AIRG}
    [Documentation]  Every (full, basic) AIGR should result in (valid) rpython code
    GIVEN a valid basic ${AIGR}
    WHEN the RPy backend is called
    THEN valid rPython is generated
    [Documentation]  Valid can te verified by compiling it.

When ${AIGR} Is compiled with ${WRITER} and run
    [Documentation]  Generated code should match the expectations, when run.
    GIVEN a valid basic ${$AIGR}
    WHEN the ${WRITER} backend is called
    THEN run the code and return result


