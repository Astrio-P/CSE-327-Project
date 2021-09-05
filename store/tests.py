from django.test import SimpleTestCase
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from store.views import *
from store.models import *
import json
# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_store_url_is_resolved(self):
        url = reverse('store')
        print(resolve(url))
        self.assertEquals(resolve(url).func, store)

    def test_cart_url_is_resolved(self):
        url = reverse('cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cart)
    
    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

    def test_viewall_url_is_resolved(self):
        url = reverse('viewall')
        print(resolve(url))
        self.assertEquals(resolve(url).func, viewall)

    def test_update_item_url_is_resolved(self):
        url = reverse('update_item')
        print(resolve(url))
        self.assertEquals(resolve(url).func, updateItem)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, searchBar)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, registerPage)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, loginPage)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logoutUser)
    
    def test_process_order_url_is_resolved(self):
        url = reverse('process_order')
        print(resolve(url))
        self.assertEquals(resolve(url).func, processOrder)


class TestViews(TestCase):

    def setUp(self):
        User(username="blabla",password="blablabla123",email="blabla@hotmail.com").save()
        user = User.objects.get(username="blabla")
        Customer(id=user.id,name=user.username,email=user.email).save()
        self.client = Client()

    def test_viewall_GET(self):
        client = Client()
        response = client.get(reverse('viewall'))
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/viewall.html')

    def test_store_GET(self):
        client = Client()
        response = client.get(reverse('store'))
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/store.html')
    
    def test_cart_GET(self):
        client = Client()
        response = client.get(reverse('cart'))
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/cart.html')

    def test_checkout_GET(self):
        client = Client()
        response = client.get(reverse('checkout'))
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'store/checkout.html')
    
    def test_register_POST(self):
        rv = self.client.post("register",{
            "username":"",
            "email":"",
            "password":""
        })
        return rv

    def test_login_POST(self):
        rv = self.client.post("login",{
            "username":"",
            "password":""
        })
        return rv



    
    # def test_updateItem_GET(self):
    #     client = Client()
    #     response = client.get(reverse('updateItem'))
        
    #     self.assertEquals(response.status_code,200)
    #     self.assertTemplateUsed(response, 'store/checkout.html')

    
class TestModels(TestCase):
    def setUp(self):
        self.person1 = Customer.objects.create(name='Person1',email='Person@gmail.com')
        self.category1 = Category.objects.create(name='category1')
        self.product1= Product.objects.create(name="",price=599,digital='True',image='null')
    def test_Customer(self):
        customer1 = Customer.objects.create(
            name=self.person1,

        )
    def test_Category(self):
        category1 = Category.objects.create(
            name=self.category1,
        )

    # def  test_Product(self):
    #     product1 = Product.objects.create(
    #         name=self.product1,
    #         price=self.product1,
    #         digital=self.product1,
    #         image=self.product1,
    #         category=self.product1,
    #     )