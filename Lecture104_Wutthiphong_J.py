class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastname,"'s Cart")

customer1 =Customer()
customer1.name = "Alan"
customer1.lastname = "Shearer"
customer1.age = 50
customer1.addCart()

customer2 =Customer()
customer2.name = "Leonel"
customer2.lastname = "Messi"
customer2.age = 33
customer2.addCart()

customer3 =Customer()
customer3.name = "Cristiano"
customer3.lastname = "Ronaldo"
customer3.age = 36
customer3.addCart()

customer4 =Customer()
customer4.name = "Robert"
customer4.lastname = "Lawandowski"
customer4.age = 32
customer4.addCart()