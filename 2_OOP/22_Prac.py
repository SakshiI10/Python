class A:
    def msg(self):
        print("A")

class B:
    def msg(self):
        print("B")

class C(A, B):
    pass

c = C()
c.msg()
