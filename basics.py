struct = {"Menu": [
          {"Position A": ["spam", "bacon", "spam"]},
          {"Position B": ["eggs", "spam", "eggs"]}
      ]}

from typing import Iterable


def get_unique_keys(struct: dict) -> Iterable[str]:
  """
  Extract all unique keys from the structure.

  Struct is a dict with a single "Menu" item.

  "Menu" is a list (length varies) of "Position" dicts.

  "Position" is a dict with a single item. Key of the item
  varies, its value is a list of "ingredients".

  "Ingredient" is a string.

  Input example:

      {"Menu": [
          {"Position A": ["spam", "bacon", "spam"]},
          {"Position B": ["eggs", "spam", "eggs"]}
      ]}

  Return example (any order):

      ["eggs", "spam", "bacon"]

      ["spam", "eggs", "bacon"]
      """
  men = struct['Menu']
  result = set()
  for p in men:    
  	k=list(p.keys())[0] 
  	for i in p[k]:
  		if not i in result:
  			result.add(i)  
  return result      

# Iterators vs Generators
# (Q1) What is the difference? What is in common?
# Give examples of both

#Iterators brings me the possibility to iter thru items 
#without loading the whole Iterable in memory, with the next command

#Generators are good for creating Iterators, brings me the result with a yield command and continues
#to execute the next iteration, then we can use this generator for iterating thru forloop or iter()
# def ints():
#     x = 0
#     while True:
#         yield x
#         x += 1



# (Q2) Excercise. Write a generator, 
# which is initialized by a list,
# produces lens of its items in reverse order
# Example: ['one', 'two', 'three', 'long number'] -> 11, 5, 3, 3

# def lens(l):    
#     l=sorted(l,key=lambda x:len(x),reverse=True)    
#     for i in l:    	
#         yield len(i)

# l = ['one', 'two', 'three', 'long number']
# items = iter(lens(l))
# items2 = iter(len(i) for i in sorted(l,key=lambda x:len(x),reverse=True))
# print(next(items))
# print(next(items))
# print(next(items))
# print(next(items2))


# Decorator

# Implement decorator "log_execution",
# Which will print text (see example) on execution.
# Apply this decorator to function "my_sum" below.

def log_execution():
    def wrapper():
        print("blah blah")
    return wrapper
    

@log_execution    
def my_sum(a, b):
  return a + b



"""
Expected output:

start execution
3
end execution
"""

# Classes


# class Base:
#   def foo(self):
#     print('Base.foo')

#   def qaz(self):
#     print('Base.qaz')


# class ExtraBase:
#   def qaz(self):
#     print('ExtraBase.qaz')


# class Child(ExtraBase, Base):
#   def foo(self):
#     print('Child.foo')

#   def bar(self):
#     print('Child.bar')


# # (Q1) What happens when we call:
# c = Child()
# c.foo()
# c.bar()
# c.qaz()
# c.extra()


# (Q2) How to simulate attribute error for c.qaz()
# Note: we are not allowed to change classes Base/ExtraBase
# We are not allowed to add qaz() to Child

if __name__ == '__main__'  :
	print(my_sum(1, 2))