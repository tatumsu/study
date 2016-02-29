from order import place_order
import os, sys

class website_api(object):
    def __init__(self):
        self.user_name = ''
        self.Gender = 'male'
        #comment in wrong ident
        self.active =False

    def login(self, Person):
        self.user_name=Person.user_name
        not_used_var = 0
        return True

    def Logout(self):
        self.active =False

    def place_order(self):
        place_order()

def action():
    Client_a = website_api()
    Client_a.login()
    Client_a.place_order()
    Client_a.Logout()
