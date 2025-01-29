import typing as PTH

class Block:
    INDENT = object()
    DEDENT = object()

    def __init__(self, text: PTH.Optional[PTH.Union[str, PTH.Sequence[str], 'Block']] = None, indent: PTH.Optional[str] = None):
        self._add_lines(text)
        self.sub_blocks: PTH.List[PTH.Tuple[int, 'Block']] = []
        self.current_indent_level = 0
        self.indentation = indent if indent is not None else ' ' * 4

    def _add_lines(self, text):
        if isinstance(text, str):
            self.lines = text.splitlines()
        elif isinstance(text, PTH.Sequence):
            self.lines = list(text)
        else:
            self._add_lines(str(text)) # Typical:  isinstance(text, Block)


    def __iadd__(self, other: PTH.Union[str, PTH.Sequence[str], 'Block', object]) -> 'Block':
        if other is Block.INDENT:
            self.current_indent_level += 1
        elif other is Block.DEDENT:
            self.current_indent_level = max(0, self.current_indent_level - 1)
        elif isinstance(other, str):
            self.sub_blocks.append((self.current_indent_level, Block(other)))
        elif isinstance(other, Block):
            self.sub_blocks.append((self.current_indent_level, other))
        elif isinstance(other, PTH.Sequence):
            for line in other:
                self.sub_blocks.append((self.current_indent_level, Block(line)))
        return self

    def set_indent(self, indent: str) -> None:
        self.indentation = indent

    def __str__(self) -> str:
        result = []

        for line in self.lines:
            result.append(line)

        for level, block in self.sub_blocks:
            block_indent = self.indentation * level
            for line in str(block).splitlines():
                result.append(block_indent + line)

        return '\n'.join(result)

# Demo
if __name__ == "__main__":
    b = Block("if True:")
    b += Block.INDENT
    b += "print('1')"
    b += Block.DEDENT
    b += "else:"
    b += Block.INDENT
    b += "print('2')"
    print(str(b))
