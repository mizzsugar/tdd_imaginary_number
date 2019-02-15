from __future__ import annotations

from dataclasses import dataclass

from complex_number.myint import MyInt
from complex_number.imaginary_number import ImaginaryNumber


@dataclass
class PurelyImaginaryNumber(ImaginaryNumber):
    imaginary: MyInt

    def __init__(self, imaginary: MyInt) -> None:
        super().__init__(0, imaginary)

    def __str__(self) -> str:
        if self.imaginary.num == 1:
            return 'i'
        elif self.imaginary.num == -1:
            return '-i'
        return f'{self.imaginary.num}i'
