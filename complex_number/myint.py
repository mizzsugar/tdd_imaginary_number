from dataclasses import dataclass


@dataclass
class MyInt:
    num: int

    def __init__(self, num):
        if num == 0:
            raise ValueError('cannot create  MyInt with 0')
        self.num = num
