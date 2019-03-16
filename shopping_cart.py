
class ShoppingCart:
    # write your code here
    def __init__(self, discount=None):
      self.total = 0
      self.discount = discount
      self.items = []

    def add_item(self, name, price, quantity=1):
      self.total += (price * quantity)
      self.items.append([name, price, quantity])

    def mean_item_price(self):
      return self.total / sum([item[2] for item in self.items])

    def median_item_price(self):
      prices = []
      for item in self.items:
         for price in range(item[2]):
            prices.append(item[1])
      sorted_by_price = sorted(prices)
      
      i = (len(sorted_by_price) // 2) - 1
      j = i + 1
      if len(sorted_by_price) % 2 == 0:
         return (sorted_by_price[i] + sorted_by_price[j]) / 2
      else:
         return sorted_by_price[j]

    def apply_discount(self):
      for item in self.items:
         if self.discount:
            item[1] =  item[1] * (1 - (self.discount * .01))
         else:
            return f"Sorry there is no discount to apply to your cart :("

    def void_last_item(self, quantity):
      if len(self.items) > 0:
         if self.items[-1][2] == 1:
            del self.items[-1]
         else:
            self.items[-1][2] -= quantity
         self.total -= (self.items[-1][1] * quantity)
      else:
         return f"There are no items"


shopping_cart = ShoppingCart()
shopping_cart.add_item("rainbow sandals", 45.99)
shopping_cart.add_item("argyle socks", 10.50)
shopping_cart.add_item("jeans", 50.00, 3)
print(shopping_cart.items)
print(shopping_cart.median_item_price())

discount_shopping_cart = ShoppingCart(20)
discount_shopping_cart.add_item('macbook_air', 1000)
discount_shopping_cart.apply_discount()
print(discount_shopping_cart.items)

shopping_cart.void_last_item(1)
print(shopping_cart.items)
print(shopping_cart.total)
