class Base:
    def show(self):
        print("Base")


class F(Base):
    def show(self):
        print("F")
        super().show()


class E(Base):
    def show(self):
        print("E")
        super().show()


class D(Base):
    def show(self):
        print("D")
        super().show()


class C(D, F):
    def show(self):
        print("C")
        super().show()


class B(E, D):
    def show(self):
        print("B")
        super().show()


class A(B, C):
    def show(self):
        print("A")
        super().show()


A().show()
