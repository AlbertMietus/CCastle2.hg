skip_lines_starting_with=(
    "import logging",
    "raise NotImplementedError",
    "_kids =",
    "logger.warning(",
    "logger.debug(",
    )

def pre_mutation(context):
    skip_on_start(context)

def skip_on_start(context):
    line = context.current_source_line.strip()
    for l in skip_lines_starting_with:
        if line.startswith(l.strip()):
            context.skip = True
            return
