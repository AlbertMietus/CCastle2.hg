# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from castle import aigr

class _A1: # Rename and move to other file
    def parameter(self, ast):
        return aigr.TypedParameter(name=ast.name, type=ast.type)

class CastleActions(_A1):
    pass
