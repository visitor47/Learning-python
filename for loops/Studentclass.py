#student class

class Student:
    
    #initialized function
    def __init__(self, name, major, GPA, is_on_probation): #initializing or creating the class of student, Everything in parenthesis are the parameters each student will have
                
                self.name = name
                self.major = major
                self.GPA = GPA
                self.is_on_probation = is_on_probation

                # class is defining what a student is ( the data type and what it has) overview of data type
                # an object is creating the actual student.  
        
                #self always has to be the first paramater in a class 
    def on_honor_roll(self):
        if self.GPA >= 3.5:
            return True
        else:
            return False

    