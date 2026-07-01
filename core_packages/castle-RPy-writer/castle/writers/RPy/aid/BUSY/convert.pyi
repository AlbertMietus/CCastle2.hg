# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.aid.convert``.

def fString_2_modulo(s: str) -> tuple[str, tuple[str, ...]]:
    """Convert a Castle f-string template to a ``%``-style format string.

    Replaces every ``{name}`` placeholder with ``%s`` and collects the
    placeholder names into the returned tuple.

    Parameters
    ----------
    s:
        A Castle f-string value such as ``"Hello {name}!"``.

    Returns
    -------
    tuple[str, tuple[str, ...]]
        ``(format_string, args)`` where *format_string* uses ``%s`` markers
        and *args* holds the original placeholder names in order.

    Example
    -------
    ::

        fmt, args = fString_2_modulo("Hi {first} {last}")
        # fmt  -> "Hi %s %s"
        # args -> ("first", "last")
    """
    ...
