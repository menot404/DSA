
#____________________________________
#
#   Classes and Object in Programming
#_____________________________________

"""
    # In Data Structures, programs often work with complex data and operations that need to be organized efficiently. Object-Oriented Programming concepts like classes and objects help structure data and related operations in a clear and manageable way.

        ==> Combines data (variables) and operations (functions) within a single structure.
        ==> Helps manage complex implementations by keeping related functionality together.
        ==> Improves reusability and organization when implementing data structures.
"""


"""
### Class #####
    A class is a blueprint or template used to create objects. It defines the structure that specifies the data members (attributes) and functions (methods) an object will contain. A class typically contains two main components:

1. Attributes (Data Members): Attributes are the properties or characteristics of an object. They store information related to the object.

2. Methods (Functions): Methods define the actions or behaviors that an object can perform.

Features of a Class

    ==> Describes the data and operations related to a particular entity.
    ==> Serves as a reusable template from which multiple objects can be created.
    ==> Helps organize code by grouping related variables and functions.
    ==> Supports modular programming, making programs easier to understand and maintain.
"""

#### Class ####
class Car_ex :
    # Attribute
    def __init__(self, color, model):
        self.color = color
        self.model = model

        # Method
        def start_engine(self):
            print("Engine started")


class Car:

    # Method: constructor (optional)
    def __init__(self):
        self.color = ""
        self.model = ""

    # Method: starts the engine
    def startEngine(self):
        print(f"{self.model} engine started")

    #Method: starts the engine
    def stopEngine(self):
        print(f"{self.model} engine stopped")


if __name__ == "__main__":

    # Create fisrt car object
        myCar = Car()
        myCar.color = "Red"
        myCar.model = "Toyota"
    #  Use attributes methods
        print(f"My car color: {myCar.color}")
        myCar.startEngine()
        myCar.stopEngine()

"""
### Classes and Objects in Data Structures ###

In Data Structures, classes and objects help organize data and the operations performed on that data. A class acts as a blueprint that defines the structure and behavior, while an object is an instance of that class used to perform operations.

    ==> Allow you to reuse code (write once, use many times).
    ==> Make it easier to represent real-world structures like: Stack (push, pop), Queue (enqueue, dequeue) and Linked List (nodes with data + next pointer).

# Example: Stack Using Class and Object
In a Stack data structure, elements are inserted and removed following the LIFO (Last In, First Out) principle. A class can be used to define the structure of the stack and the operations performed on it.

Here, the class represents the stack design, while the objects allow us to perform stack operations such as push and pop.
"""

# Class representing a stack

class Stack:
    def __init__(self):
        self.arr = [0]*5
        self.top = -1
    
    # Method to push element
    def push(self, x):

        if self.top == 4:
            print("Stack Overflow")
            return
        
        self.top += 1
        self.arr[self.top] = x

    # Method to pop element
    def pop(self):

        if self.top == -1:
            print("Stack Underflow")
            return
        
        self.top -= 1

    # Method to display stack
    def display(self):

        if self.top == 4:
            print("Stack Overflow")
            return
        
        if self.top == -1:
            print("Stack Underflow")
            return
        
        for i in range(self.top, -1, -1):
            print(self.arr[i], end=" ")
        print()
        print(self.arr)


# driver code

if __name__ == "__main__" :

    # Creating stack object
    s = Stack()

    # Performing operations
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack elements: ", end=" ")
    s.display()

    s.pop()

    print("After pop: ", end=" ")
    s.display()