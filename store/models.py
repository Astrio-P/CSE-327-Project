from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Suggestions(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.first_name


class Customer(models.Model):
    """
    This class is used to create the Customers/Users.
    
    This class is extended from the Model class so it has all the functionality
    of the model class.
    
    This class is used to create objects for database entry
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    This class is used to create Categories of the product. It has only one field "Name" and it 
    and each object has it's own assigned id from django.
    
    This class is extended from the Model class so it has all the functionality
    of the model class.
    
    this class is used to create objects for database entry has only one field called 'name'
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    """
    This class is used to create items or products.

    This class is extended from the Model class so it has all the functionality
    of the model class.
    
    this class is used to create objects for database entry has fields called name,price,digital(Shipping needed or not),image(Picture of the products),category
    """

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default=True ) 
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        """
        This Function is to fetch the respective product image without gettting an error
        :param: self
        :return: url 
        """
        try:
            url = self.image.url
        except:
            url = ''
        return url

    
class Order(models.Model):
    """
    This class is used to create Orders per user/customer. It has customer as it's foreign key.

    this class is used to create objects for database entry has fields named customer,date_ordered,complete,transaction_id
    """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def getCartTotal(self):
        """
        ---
        Returns the total amount for the cart total bill.

        Parameters
        ----------
        self : the object itself

        Returns
        --------
        total
            The sum amount or the total amount of bill for all the items in the cart.
        """
        orderitems = self.orderitem_set.all()
        total = sum([item.getTotal for item in orderitems])
        return total

    @property
    def getCartItems(self):
        """
        This Function is to get the number of items that are added in the cart by the user
        :param: self
        :return: 'total' number of items in the cart
        """
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping=True
        return shipping

class OrderItem(models.Model):
    """
    This class is used to create The order list. It has product and order as it's foreign key

    This class is extended from the Model class so it has all the functionality
    of the model class.

    this class is used to create objects for database entry
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)     
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def getTotal(self):
        """
        This Function is to get the total bill of each individual items that are added in the cart by the user regarding their quantity
        :param: self
        :return: 'total' amount of money to be charged for the purchase
        """
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    """
    This class is used to store the shipping address inputted by the user after checkout

    This class is extended from the Model class so it has all the functionality
    of the model class.

    this class is used to create objects for database entry
    """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
        
    