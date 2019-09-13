class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    pass

class Employee(Person):
    def __init__(self, name, job_title):
        super(Employee, self).__init__(name)
        self.job_title = job_title
    def do_work(self):
        print(f"I am {self.getName()}, I am working {self.job_title}")
    pass

person = Person("Monica")
print(person.getName())

worker = Employee("Chendler","D")
worker.do_work()

# if not hasattr(worker, "aaa"):
#     print("no")


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return "from Triangle"

class Square:
    def __init__(self, height, wet):
        self.height = height
        self.wet = wet

    def area(self):
        return "from Square"

class A(Triangle, Square):
    def __init__(self, base, height, wet):
        pass
        # Square.__init__(height,wet)
        # super(A, self).__init__(base, height, wet)
        # super(Square, self).__init__(height)

    def area(self):
        return "from A"


a = A(2, 4, 6)
print(A.__mro__)


