class Bicycle(object):
  def __init__(self, name, weight, cost):
    self.name = name
    self.weight = weight
    self.cost = cost
    
class Bicycle_Shop(object):
  def __init__(self):
    pass

class Customer(object):
  def __init__(self):
    pass
  
if __name__ == '__main__':
  roadmax = Bicycle('Roadmax 1985', 50, 180)
  print roadmax.name
  print roadmax.weight
  print roadmax.cost