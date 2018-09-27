import math
import array
import random 

Team_one = ["munoz", "bibb", "kelly", "chambers", "olson"]

for value in range(len(Team_one)):
    print(Team_one[value])
    #this prints out the following
   #Team_one[0]
   #Team_one[1]
   #Team_one[2]



for value in range(5):
    if value == 0:
        print("im first")

    else: 
        print("damn i aint first")


# making a function that does exponential notation
#this one uses a for loop that will multiply the number by itself 
#for as long as this loop runs. we take in base_num and its going to be
# taken to the power of Pow_num


def power_of(base_num, pow_num):
    result = 1
    for x in range(pow_num):
        result = result * base_num
    
    return result

print(power_of(7,8))

# a secondary way of making a power of function
#this one uses simple ** notation to denote the power of 
def alt_powerof(base_num, pow_num):
    x = base_num ** pow_num
    return x


print (alt_powerof(7,8))


#printing every letter in this list grid.
gridrow = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 12, 10],
    [22, 23, 24, 25, 26],
    [100, 11, 66, 0, 81]
]

for row in gridrow: # for every number in our list "gridrow"
    for col in row: # we are then going to look at every number in each 
        print(col) # we then pr int out every number for each list and ti will go through every array to print one


 # translator

def translator(phrase): #we are defining a function called translation that will take a paramater we called phrase
    translation = "" # translation is = to a blank input since its going to be user input
    for letter in phrase: # for every letter or x or thing in the injected paramater ( in this case "phrase")
        if letter.lower() in "aeiou": # now this is IF the letter/x/etc THAT WE ARE LOOKING AT is in the string  of 'AEIOUaeiou' 
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g" # We are going to change it or switch it to the letter "g"
        else: #otherwise
            translation = translation + letter #add whatever letter it was on to the end of the translation
    return translation #this function will return our new translation


print(translator(input("Enter your phrase: ")))


'''
try except statements
'''

# if you have code that is giving you an error and you are singling out pieces of code. try commenting the code out so the program 
# ignores it. that way u can see if its that single line of code fucking your program up

#try throw

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # add 25/0 as an int and then run the program again for what this is.
    print(err)
except ValueError:
    print("Invalid value. Please enter a number")


#reading files

# r - read: i only want to read information inside the file id ont want to modify or change just read it and use the info
# w - write : i can change the file however i want 
# a - append: i want to add information onto the end of the file without modifying any of the information already in there.
# r+ - read and write : all the power of reading and writing
random_file = open("TextFile1.txt", "rt")

for employee in random_file.readlines():
    print(employee)

random_file.close()






