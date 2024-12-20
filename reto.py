
class MenuItem:
  """
  base class that define general parameters for each item from menu

  Attributes:
    name (str): Name of the item from menu
    price (float): Price of the item from menu
  """
  def __init__(self, name: str, price: float):
    """
  Initializes the class with values for name and price.

  Args:
    name (str): The initial value for name.
    price (int): The initial value for price.
    """
    self.name = name
    self.price = price
 
class Beverage(MenuItem):
  """
  A subclass of MenuItem that represent Beverage

  Inherits:
    MenuItem: The base class

  Aditional Atributes:
    Size: The size of the beverage
  """

  def __init__(self, name, price, size: str):
    super().__init__(name, price)
    self.size = size

class Appetizer(MenuItem):
  """
  A subclass of MenuItem that represent Appetizer

  Inherits:
    MenuItem: The base class

  Aditional Atributes:
    is_vegetarian: If the food is vegetarian or not
  """
  
  def __init__(self, name, price, is_vegetarian: bool = False):
    super().__init__(name, price)
    self.is_vegetarian = is_vegetarian

class MainCourse(MenuItem):
  """
  A subclass of MenuItem that represent Beverage

  Inherits:
    MenuItem: The base class

  Aditional Atributes:
    Protein: The protein of the maincourse
    is_vegetarian: If the food is vegetarian or not
  """
  
  def __init__(self, name, price, protein: str, is_vegetarian: bool = False):
    super().__init__(name, price)
    self.protein = protein
    self.is_vegetarian = is_vegetarian

class Dessert(MenuItem):
  """
  A subclass of MenuItem that represent Beverage

  Inherits:
    MenuItem: The base class

  Aditional Atributes:
    Topping: The topping of each dessert
  """

  def __init__(self, name, price, topping: str):
    super().__init__(name, price)
    self.topping = topping

class Order:
  """
Class that handles the order and total calculation by applying discounts.

Discounts:
- Birthday discount: 5% (if `your_birthday` is True).
- Discount for total over 120,000: 20%.
- Discount for total over 90,000: 10%.
- No discount for totals under 90,000.

  Args:
    your_birthday (bool): Indicate if it is the client's birthday.
  """
  def __init__(self):
    self.__items = []
    self._total = 0.0

  def add_item(self, item: MenuItem) -> None:
    """
    Adds an item to the order.

    Args:
      item (MenuItem): The item to aggregate.
    """
    if item:
      self.__items.append(item)
      self._total += item.price

  def calculate_total(self, your_birthday: bool = False, include_tax: bool = True) -> str:
    total = self._total
    print("your order is:")
    for item in self.__items:
      print(f"{item.name}: ${item.price}")

    print(f"total price: ${total}")

    # Apply birthday discount if applicable
    if your_birthday:
      total *= 0.95  # 5% discount 

    # Apply tax if applicable
    if include_tax:
      total *= 1.19  # 19% tax

    # Apply discounts to the total order
    if total > 120000:
      total *= 0.8  # 20% de discount 
    elif total > 90000:
      total *= 0.9  # 10% discount

    return f"Total: ${total}"


class Menu:
  """
  Represents a menu containing various menu items, including appetizers, beverages,
  main courses, and desserts.

  Attributes:
    menu_items (list): A list of predefined menu items, each represented as an instance
    of a specific subclass (e.g., Appetizer, Beverage, MainCourse, Dessert).

    Methods:
    show_menu() -> None:
      Displays the menu items with their names and prices.

    get_item(name: str) -> MenuItem:
      Retrieves a menu item by its name.
  """

  def __init__(self):
    self.__menu_items = [
      Appetizer("Nuggets", 12000),
      Appetizer("Onion soup", 14000, True),
      Beverage("Coke", 3000, "Medium"),
      Beverage("Water", 2000, "Medium"),
      Beverage("Coffee", 3500, "Medium"),
      MainCourse("Burger", 20000, "Cow meat"),
      MainCourse("Vurger", 23000, "Bean meat", True),
      MainCourse("Caesar salad", 18000, "Chicken"),
      Dessert("Oreo McFlurry", 13000, "Oreo"),
      Dessert("m&m McFlurry", 13000, "m&m")]
    
  def get_item(self, name: str):
    for item in self.__menu_items:
      if item.name == name:
        return item 
    return None  

  
  def show_menu(self) -> None:
    print("\tMenu")
    for item in self.__menu_items:
        print(f"{item.name}: ${item.price}")
    print("-------------------------")



if __name__ == "__main__":
  # Example menu
  menu = Menu()
  menu.show_menu()
  order = Order()
  order.add_item(menu.get_item("Coke"))
  order.add_item(menu.get_item("Vurger"))
  order.add_item(menu.get_item("Oreo McFlurry"))
  order.add_item(menu.get_item("m&m McFlurry"))
  order.add_item(menu.get_item("Water"))
  order.add_item(menu.get_item("Coffee"))
  order.add_item(menu.get_item("Burger"))
  order.add_item(menu.get_item("Nuggets"))
  order.add_item(menu.get_item("Onion soup"))
  order.add_item(menu.get_item("Caesar salad"))

  print(order.calculate_total(True))
