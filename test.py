
A = 0

class B:
    def __init__(self):
        global A
        A = A + 1
        print(A)


B()
B()
B()

