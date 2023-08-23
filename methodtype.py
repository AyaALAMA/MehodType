
class Calculator:
  
# constructor
  def __init__(self, x, y):
 
    self.x = x
    self.y = y

# instance method
  def add(self):  
    return self.x + self.y

 # class method
  @classmethod
  def average(cls, numbers):
    return sum(numbers) / len(numbers)

# static method
  @staticmethod
  def power(number, exponent):
    return pow(number, exponent)

calc = Calculator(3, 5)

print("sum x و y :", calc.add())
print("average [1, 2, 3, 4, 5] :", Calculator.average([1, 2, 3, 4, 5]))
print("2 ^ 10 :", Calculator.power(2, 10))
