from dataclasses import dataclass

from complex_number.purely_imaginary_number import PurelyImaginaryNumber


@dataclass
class ImaginaryNumber:
    real: int
    imaginary: PurelyImaginaryNumber

    def __init__(self, real: int, imaginary: PurelyImaginaryNumber):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.real == 0:
            return str(self.imaginary)
        if self.imaginary.myint.num < 0:
            num = -1 * self.imaginary.myint.num
            return f"{self.real} - {num}i"
        return f"{self.real} + {self.imaginary}"
