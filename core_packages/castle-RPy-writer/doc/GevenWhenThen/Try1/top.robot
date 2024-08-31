
*** Test Cases ***

Generate rPython
    [Documentation]  Every (full, basic) AIGR should result in (valid) rpython codde
    GIVEN a valid basic ${AIGR}
    WHEN the RPy backend in called
    THEN valid rPython is generated
    [Documentation]  *Valid* can te verified by compiling it.

Run rPython
    [Documentation]  Generated code should match the exectations, when run.
    GIVEN a valid basic ${$AIGR}
    WHEN the RPy backend in called
    THEN the run code should match the expexted ${OUTPUT}, given @{FILTERS}
