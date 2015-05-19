from bicycles import Bicycle, Bicycle_Shop, Customer

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