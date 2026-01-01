# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from castle import aigr

class Components():
    def implement_component(self, ast):
        return aigr.ComponentImplementation(ast.name)

