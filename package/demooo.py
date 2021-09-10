# from package.prgm import *
# add(2,3)
# sub(7,3)

# from packexc.printexc import printe
# printe()


# def cube(x):
#     return x*x*3
# n=int(input("enter num"))
# print(cube(n))

# cube=lambda x:x**3
# print(cube(5))

# add=lambda x,y:x+y
# print(add(5,3))

# word=lambda x:x[0]
# print(word("world"))

class Vscode:
    def compile(self):
        print("compiling using vscode")
    def execute(self):
        print("executing using vscode")
    def debug(self):
        print("debugging using vscode")
class Pycharm:
    def compile(self):
        print("compiling using pycharm")
    def execute(self):
        print("executing using pycharm")
    def debug(self):
        print("debugging using pycharm")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
dev=Programmer()
pyc=Pycharm()
dev.coding(pyc)