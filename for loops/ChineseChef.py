from chefClass import chef # we imported the original chef class 

class ChineseChef(chef):
    # we had our Chinese chef. INHERIT all of the traits of the original chef class

       def make_fried_rice(self): #here we added our own function to the chinese chef class that the original will not have
           print("The chef made some fried rice")

           #you can also overide functions from the inheritance by changing it here.
       def make_soup(self):
           print("we made  onion broth soup")

       def make_chicken(self):
           print("The Chef made sweet and sour chicken")