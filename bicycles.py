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
      return self.inventory[bicycle.name]['bicycle'], sale_price
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
      self.bicycle, price = shop.sell_bicycle(bike)
      self.fund = self.fund - price
      print "Bought a '{0}' for a price of ${1:.2f}".format(self.bicycle.name, price)
  
if __name__ == '__main__':
  cheapo = Bicycle('El Cheapo Grande', 100, 15)
  roadmax = Bicycle('Roadmax 1985', 50, 100)
  cycletron = Bicycle('Cycletron 1992', 42, 120)
  schwing = Bicycle('Schwing', 20, 300)
  racestar = Bicycle('Racestar 20xx', 12, 400)
  brains = Bicycle('Moremoneythanbrains 1%', 10, 600)
  shop = Bicycle_Shop('OMG Bikes', 20)
  shop.add_inventory(cheapo, 4)
  shop.add_inventory(roadmax, 2)
  shop.add_inventory(cycletron, 2)
  shop.add_inventory(schwing, 1)
  shop.add_inventory(racestar, 1)
  shop.add_inventory(brains, 1)
  bob = Customer('Bob', 200.0)
  jim = Customer('Jim', 500.0)
  rich = Customer('Rich', 1000.0)
  customers = [bob, jim, rich]
  for customer in customers:
    print "Customer {} is able to purchase the following bikes:".format(customer.name)
    bikes = shop.search_by_price(customer.fund)
    for bike in bikes:
      print bike.name
  print "Initial shop inventory:"
  shop.print_inventory()
  for customer in customers:
    print "Customer {} is purchasing a bike...".format(customer.name)
    customer.buy_bicycle(shop)
    print "Customer {0} has ${1:.2f} remaining".format(customer.name, customer.fund)
  shop.print_inventory()
  shop.print_profit()