class A:
    def say_name(self):
        print('A sayname is A')

class B(A):
    pass

class C:
    pass

class D(C):
    def say_name(self):
        print('D sayname is D')

class E(B,D):
    pass
print(E.__mro__)
