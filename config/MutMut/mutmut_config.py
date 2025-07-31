skip_lines_starting_with=(
    "import logging",
    "raise NotImplementedError",
    "logger.warning(",
    "logger.debug(",
    "logger.info(",
    "raise TypeError",
    )

def pre_mutation(context):
    skip_on_start(context)

def skip_on_start(context):
    line = context.current_source_line.strip()
    for l in skip_lines_starting_with:
        if line.startswith(l.strip()):
            context.skip = True
            return
