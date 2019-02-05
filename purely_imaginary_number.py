from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PurelyImaginaryNumber:
    num: int

    def __init__(self, num) -> None:
        if num == 0:
            raise ValueError
        self.num = num

    def __str__(self) -> str:
        if self.num == 1:
            return 'i'
        elif self.num == -1:
            return '-i'
        return f'{self.num}i'

    def is_conjugate_to(self, other: PurelyImaginaryNumber) -> bool:
        return self.num == other.num * (-1)
