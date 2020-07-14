
#7.51 Dictionary loop and String formating
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

#another way:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
    

#replace 
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))
    
# != isdifferent


#sample program
def sentence_maker (phrase):
    question_words = ("how","what","why","when","which")
    capitalized = phrase.capitalize()
    if phrase.startswith(question_words):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join((results)))
    
    
#Infinite number of arguments in a function
def processed_strings(*args):
    args = [i.upper() for i in args] 
    return sorted (args)
    
# keyword arguments
def find_sum(**kwargs):
return sum(kwargs.values())
    
print(find_sum(a=3, b=3, c=3))

#72
#processing texts

#open and print a file:
myfile = open("fruits.txt")
print(myfile.read())

#better method:
with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)

#processing file inside a function:
def foo(char, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(char)
    
#open and write a text:
with open("vegetables.txt", "w") as myfile:
    content = myfile.write("tomato\ncucumber")

with open("vegetables.txt") as myfile2:
    r_content = myfile2.read()
print (r_content) 

#append and read:
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
    
#look for builtin module
sys.builtin_module_names

# python modules
import time
import os

#v1.1 with title()
import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
 
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    
#v1.1_lam
import jsonimport difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    
    #check if a value is in a dictionary:
    if w in data:
        return data[w]
    else:
        w = w.capitalize()
        if w in data:
            return data[w]
        else:
            w = w.lower() 
            if len(get_close_matches(w, data.keys())) > 0:
                yn = input("Did you mean %s instead?: " % get_close_matches(w, data.keys())[0])
                if yn == "Y":
                    return data[get_close_matches(w, data.keys())[0]]
                elif yn == "N":
                    return "Please check"
            else:
                return("word not in dictionary")

word = input("Insert a word: ") 

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

#pip install mysql_connector
py -3 -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org mysql-connector-python

# mysql app 
import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter w word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    for results in results:
        print(results[1])
else:   
    print("No word found")


