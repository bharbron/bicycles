import random

class Bicycle(object):
  def __init__(self, name, weight, cost):
    self.name = name
    self.weight = weight
    self.cost = cost
    
  def __repr__(self):
    return 'Bicycle("{0}","{1}","{2:.2f}")'.format(self.name, self.weight, self.cost)
    
class Bicycle_Shop(object):
  def __init__(self, name, markup):
    self.name = name
    self.markup = markup
    self.inventory = {}
    self.profit = 0.0
    
  def __repr__(self):
    return 'Bicycle_Shop("{0}","{1}","{2}","{3:.2f}")'.format(self.name,self.markup,self.inventory,self.profit)
    
  def add_inventory(self, bicycle, quantity):
    if bicycle.name in self.inventory:
      self.inventory[bicycle.name] = {'bicycle': bicycle, 'quantity': self.inventory[bicycle.name]['quantity'] + quantity}
    else:
      self.inventory[bicycle.name] = {'bicycle': bicycle, 'quantity': quantity}
    self.profit = self.profit - (quantity * bicycle.cost)
      
  def print_inventory(self):
    for name, item in self.inventory.iteritems():
      print "We have {0} bicycles of model '{1}' in stock".format(item['quantity'], name)
      
  def print_profit(self):
    print "We have made ${:.2f} selling bicycles".format(self.profit)
    
  def calc_sale_price(self, bicycle):
    return bicycle.cost * ((self.markup / 100.0) + 1.0)
    
  def sell_bicycle(self, bicycle):
    if bicycle.name in self.inventory and self.inventory[bicycle.name]['quantity'] >= 1:
      sale_price = self.calc_sale_price(self.inventory[bicycle.name]['bicycle'])
      print "Here is your '{0}'.  That will be ${1:.2f}, please.".format(bicycle.name, sale_price)
      self.inventory[bicycle.name]['quantity'] = self.inventory[bicycle.name]['quantity'] - 1
      self.profit = self.profit + sale_price
      return self.inventory[bicycle.name]['bicycle']
    else:
      print "Sorry, we don't have the '{}' in stock.".format(bicycle.name)
      return None
      
  def search_by_price(self, fund):
    affordable_bikes = []
    for name, item in self.inventory.iteritems():
      sale_price = self.calc_sale_price(item['bicycle'])
      if item['quantity'] >= 1 and sale_price <= fund:
        affordable_bikes.append(item['bicycle'])
    return affordable_bikes
      

class Customer(object):
  def __init__(self, name, fund):
    self.name = name
    self.fund = fund
    self.bicycle = None
    
  def __repr__(self):
    return 'Customer("{0}","{1:.2f}","{2}")'.format(self.name, self.fund, self.bicycle)
    
  def buy_bicycle(self, shop):
    bikes = shop.search_by_price(self.fund)
    if bikes:
      bike = random.choice(bikes)
      self.bicycle = shop.sell_bicycle(bike)
      #TODO calculate remaining funds
  
if __name__ == '__main__':
  roadmax = Bicycle('Roadmax 1985', 50, 100)
  print roadmax
  racestar = Bicycle('Racestar 20xx', 12, 400)
  print racestar
  shop = Bicycle_Shop('OMG Bikes', 20)
  print shop
  shop.add_inventory(roadmax, 2)
  shop.add_inventory(racestar, 1)
  shop.print_inventory()
  shop.add_inventory(racestar, 2)
  shop.print_inventory()
  shop.print_profit()
  shop.sell_bicycle(roadmax)
  shop.print_inventory()
  shop.print_profit()
  print shop
  bob = Customer('Bob', 200.0)
  print bob
  jim = Customer('Jim', 500.0)
  print jim
  print shop.search_by_price(bob.fund)
  jim.buy_bicycle(shop)
  print jim