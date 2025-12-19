# import necessary modules
from abc import ABC, abstractmethod


# create base class
class BaseClass(ABC):

  # Function to print a value
  def print(self, x):
    print("Passed value: ", x)

  @abstractmethod
  def task(self):
    print("we are inside absclass task")


# create subclass
class test_class(BaseClass):
  def task(self):
    print("we are inside subclass task")


# object of test class created
test_obj = test_class()
test_obj.print(100)
test_obj.task()