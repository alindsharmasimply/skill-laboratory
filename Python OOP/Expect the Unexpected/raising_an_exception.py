class EvenOnly(list[int]):
    def append(self, n: int):
        match n:
            case int():
                if n % 2 != 0:
                    raise ValueError("Number should only be even")
            case _:
                raise TypeError("Only integers can be added")
        super().append(n)


x = EvenOnly()
x.append(2)
x.append(3)
x.append("Sachin")
