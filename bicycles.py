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
    self.profit = self.profit - (quantity * bicycle.cost)
      
  def print_inventory(self):
    for name, bicycle in self.inventory.iteritems():
      print "We have {0} bicycles of model '{1}' in stock".format(bicycle['quantity'], name)
      
  def print_profit(self):
    print "We have made ${} selling bicycles".format(self.profit)
    
  def sell_bicycle(self, bicycle):
    if bicycle.name in self.inventory and self.inventory[bicycle.name]['quantity'] >= 1:
      sale_price = self.inventory[bicycle.name]['bicycle'].cost * ((self.markup / 100.0) + 1.0)
      print "Here is your '{0}'.  That will be ${1}, please.".format(bicycle.name, sale_price)
      self.inventory[bicycle.name]['quantity'] = self.inventory[bicycle.name]['quantity'] - 1
      self.profit = self.profit + sale_price
    else:
      print "Sorry, we don't have the '{}' in stock.".format(bicycle.name)
    self.print_inventory()
    self.print_profit()

class Customer(object):
  def __init__(self, name):
    self.name = name
  
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
  shop.add_inventory(roadmax, 2)
  shop.add_inventory(racestar, 1)
  shop.print_inventory()
  shop.add_inventory(racestar, 2)
  shop.print_inventory()
  shop.print_profit()
  shop.sell_bicycle(roadmax)