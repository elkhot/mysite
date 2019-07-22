from django.urls import path
from . import views

app_name = 'home'

urlpatterns =[
    path('', views.home, name='home')
]

#import unittest


#class MyTestCase(unittest.TestCase):
#   def test_something(self):
  #      self.assertEqual(True, False)


#if __name__ == '__main__':
#    unittest.main()
