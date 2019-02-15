from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from complex_number.myint import MyInt


@dataclass
class ImaginaryNumber:
    real: int
    imaginary: MyInt

    def __init__(self, real: int, imaginary: MyInt):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: Any) -> bool:
        return (
                isinstance(other, ImaginaryNumber)
                and self.real == other.real
                and self.imaginary == other.imaginary
        )

    def __str__(self):
        if self.real == 0:
            return f"{self.imaginary.num}i"
        if self.imaginary.num < 0:
            num = -1 * self.imaginary.num
            return f"{self.real} - {num}i"
          