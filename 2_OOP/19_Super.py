'''
Why super is not used in multiple inheritance?
a) super() follows a specific path (called Method Resolution Order or MRO).
b) It calls only one parent at a time, not both.
c) If your parent classes are (base1, base2) don’t use super, because parts of the chain can skip. So, if you just use super() in the child class, only one base class might get initialized, and the other will be ignored.
'''

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
# Python uses left-to-right depth-first search for method resolution. That's why A printed.