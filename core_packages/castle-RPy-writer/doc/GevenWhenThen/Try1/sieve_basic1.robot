[Documentation] Test the RPy-writer with sieve/basic1

*** Variables ***
${SIEVE_FILE}  = sieve/basic1
${WRITER}      = RPY

${OUTPUT}      = xxxx
@{FILTERS}     = None

*** Test Cases ***
Compile Sieve
    ${AIGR} = Given MockRead ${SIEVE_FILE}
    Check rPython for ${AIGR}

Run Sieve
    {AIGR} = Given MockRead ${SIEVE_FILE}
    When  ${AIGR} is compiled with ${WRITER} and run
    THEN the result should match the expected ${OUTPUT}, given @{FILTERS}


