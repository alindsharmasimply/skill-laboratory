class A:
    def __init__(self):
        print("Initializing A")


class B(A):
    def __init__(self):
        super().__init__()
        print("Initializing B")


class C(A):
    def __init__(self):
        super().__init__()
        print("Initializing C")


class D(A):
    def __init__(self):
        super().__init__()
        print("Initializing D")


class E(B, C, D):
    def __init__(self):
        super().__init__()
        print("Initializing E")


e = E()
