class Bicycle(object):
  def __init__(self, name, weight, cost):
    self.name = name
    self.weight = weight
    self.cost = cost
    
class Bicycle_Shop(object):
  def __init__(self, name, markup):
    self.name = name
    self.markup = markup
    self.inventory = {}
    self.profit = 0.0
    
  def add_inventory(self, bicycle, quantity):
    if bicycle.name in self.inventory:
      self.inventory[bicycle.name] = {'bicycle': bicycle, 'quantity': self.inventory[bicycle.name]['quantity'] + quantity}
    else:
      self.inventory[bicycle.name] = {'bicycle': bicycle, 'quantity': quantity}
      
  def print_inventory(self):
    for name, bicycle in self.inventory.iteritems():
      print "We have {0} bicycles of model '{1}' in stock".format(bicycle['quantity'], name)

class Customer(object):
  def __init__(self):
    pass
  
if __name__ == '__main__':
  roadmax = Bicycle('Roadmax 1985', 50, 180)
  print roadmax.name
  print roadmax.weight
  print roadmax.cost
  racestar = Bicycle('Racestar 20xx', 12, 480)
  shop = Bicycle_Shop('OMG Bikes', 20)
  print shop.name
  print shop.markup
  print shop.inventory
  print shop.profit
  shop.add_inventory(roadmax, 10)
  shop.add_inventory(racestar, 3)
  shop.print_inventory()
  shop.add_inventory(racestar, 2)
  shop.print_inventory()