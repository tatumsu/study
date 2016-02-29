class User:
     def __init__(self, name, age, email):
          self.name = name
          self.age = age
          self.email = email
          self.father = None
          self.mother = None

     def __str__(self):
         str = "User: Name=%s; Age=%s, Email=%s" % (self.name, self.age, self.email)
         if (self.father != None):
             str = str + "\nFather: Name=%s; Age=%s, Email=%s" % (self.father.name, self.father.age, self.father.email)
         if (self.mother != None):
             str = str + "\nMother: Name=%s; Age=%s, Email=%s" % (self.mother.name, self.mother.age, self.mother.email)
         return str
