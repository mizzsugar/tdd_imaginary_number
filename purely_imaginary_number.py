from __future__ import annotations

from dataclasses import dataclass

from myint import MyInt


@dataclass
class PurelyImaginaryNumber:
    myint: MyInt

    def __init__(self, myint: MyInt) -> None:
        self.myint = myint

    def __str__(self) -> str:
        if self.myint.num == 1:
            return 'i'
        elif self.myint.num == -1:
            return '-i'
        return f'{self.myint.num}i'

    def is_conjugate_to(self, other: PurelyImaginaryNumber) -> bool:
        return self.myint.num == other.myint.num * (-1)
