class Product: #creating product class
  def __init__(self,product_id,name,price,quantity):
    self.product_id=product_id #adding attributes to the class
    self.name=name
    self.price=price
    self.quantity=quantity

  def update_quantity(self,new_quantity): #creating method to update product quantity
    if new_quantity>=0:
      self.quantity=new_quantity #if quantity is greater than zero update the quantity
    else:
      print("Quantity cannot be negative")#otherwise print this message

  def get_product_info(self): #creating method to obtain the info for the product
    return{"Product_ID": self.product_id, "Name": self.name, "Price": self.price, "Quantity": self.quantity} #returns the info

class DigitalProduct(Product): #creating class derived from the product class
    def __init__(self, product_id, name, price, quantity, file_size, download_link):
      super().__init__(product_id, name, price, quantity) #inheriting product class attributes
      self.file_size = file_size #adding attributes to the class
      self.download_link = download_link

    def get_product_info(self): #creating method to obtain info for a digital product
      info = super().get_product_info() #getting the product info
      info["File Size"] = self.file_size #adding info for digital product
      info["Download Link"] = self.download_link
      return info

class PhysicalProduct(Product): #creating class derived from the product class
    def __init__(self, product_id, name, price, quantity, weight, dimensions, shipping_cost):
        super().__init__(product_id, name, price, quantity) #inheriting product class attributes
        self.weight = weight #adding attributes to the class
        self.dimensions = dimensions
        self.shipping_cost = shipping_cost

    def get_product_info(self): #creating method to get product info for a physical product
        info = super().get_product_info() #getting the product info
        info["Weight"] = self.weight #adding info for physical product
        info["Dimensions"] = self.dimensions
        info["Shipping Cost"] = self.shipping_cost
        return info

class Cart: #creating cart class
  def __init__(self):
    self.__cart_items=[] #making a private list of the products in the cart

  def add_product(self, product): #method to add product to the cart
        self.__cart_items.append(product)

  def remove_product(self, product_id): #method to remove a product from the cart using the product id
        self.__cart_items = [product for product in self.__cart_items if product.product_id != product_id]

  def view_cart(self): #method to view the items in the cart
        return [product.name for product in self.__cart_items]

  def calculate_total(self): #method to calculate the price of the products in the cart
        return sum(product.price for product in self.__cart_items)

class User: #creating user class
  def __init__(self, user_id,name):
    self.user_id=user_id #adding attributes to the class
    self.name=name
    self.cart=Cart()

  def add_to_cart(self,product): #method to add a product to the user's cart
    self.cart.add_product(product)

  def remove_from_cart(self,product_id): #method to remove a product from the user's cart
    self.cart.remove_product(product_id)

  def checkout(self): #method to calculate total price in the cart and clear the cart afterward
    total = self.cart.calculate_total()
    if total == 0:
      print("The cart is empty!")
    else:
      print(f"Total amount: ${total}")
      self.cart = Cart()

class Discount: #creating discount class which is an abstract class being used as a base for other discount classes
    def apply_discount(self, total_amount):
      pass


class PercentageDiscount(Discount): #creating the percentage discount class
    def __init__(self, percentage):
      self.percentage = percentage #adding attributes to the class

    def apply_discount(self, total): #method to apply the percentage discount to the total
      discount = (self.percentage / 100) * total
      calculated_discount=total-discount
      return(f"${calculated_discount:.2f}")


class FixedAmountDiscount(Discount): #creating the fixed amount discount class
    def __init__(self, amount):
      self.amount = amount #adding attributes to the class

    def apply_discount(self, total): #method to apply the fixed amount discount to the total
      calculated_discount=total-self.amount
      return(f"${calculated_discount:.2f}")

