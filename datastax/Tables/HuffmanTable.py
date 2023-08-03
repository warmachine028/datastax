from datastax.Tables.AbstractTables import HuffmanTable as AbstractTable


class HuffmanTable(AbstractTable):
    def __init__(self, data: dict[str, str],
                 frequencies: dict[str, int]):
        self.data = data
        self.set_frequencies(frequencies)
        self.set_size()

    def set_size(self):
        size = 0
        for char, huff_code in self.data.items():
            size += ord(char).bit_length() + len(huff_code)
        self._size = size

    def set_frequencies(self, frequencies: dict[str, int]):
        self._frequencies = frequencies
