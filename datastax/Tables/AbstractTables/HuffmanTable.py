from abc import ABC as AbstractClass, abstractmethod


class HuffmanTable(AbstractClass):
    data: dict[str, str]
    _frequencies: dict[str, int]
    _size = 0

    @property
    def frequencies(self):
        return self._frequencies

    @property
    def size(self):
        return self._size

    def __str__(self):
        items = self.data
        padding = 4
        max_width = max(len(code) for *_, code in items.values()) + padding * 2
        if max_width < 10:
            max_width = 12
        mid_width = max_width * 2 - (4 if max_width > 12 else 0)

        h_border = f"╔{'═' * max_width}╤{'═' * mid_width}╤{'═' * max_width}╗\n"
        header = (
            f"║{'Unique'.center(max_width)}"
            f"│{'Occurrence /'.center(mid_width)}│"
            f"{'Huffman'.center(max_width)}║\n"
            f"║{'Characters'.center(max_width)}"
            f"│{'Frequency'.center(mid_width)}│"
            f"{'Code'.center(max_width)}║\n"
        )
        sep = f"╟{'─' * max_width}┼{'─' * mid_width}┼{'─' * max_width}╢\n"
        data_template = "║{}│{}│{}║\n"

        body = ""
        for character, huffman_code in items.items():
            body += sep
            body += data_template.format(
                character.center(max_width),
                str(self.frequencies[character]).center(mid_width),
                huffman_code.rjust(max_width - padding).center(max_width),
            )
        f_border = f"╚{'═' * max_width}╧{'═' * mid_width}╧{'═' * max_width}╝"
        return h_border + header + body + f_border

    @abstractmethod
    def set_frequencies(self, frequencies: dict):
        ...

    @abstractmethod
    def set_size(self):
        ...
