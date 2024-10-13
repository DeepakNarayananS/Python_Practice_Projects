### Code snippet for a simple Contact Management System

# Added json library as we are appending and store contacts in a separate json file and linking it to this program
import json

# Function for Adding contact
# strip() function is added to avoid empty spaces that are entered by the user mistakenly.
def add_contact():
    name = input("name : ").strip()
    age = input("age : ").strip()
    email = input("email : ").strip()

    try:
        age = int(age)
        if age < 0:
            print("Invalid age. Please enter a non-negative number.")
            return
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    person = {"name": name, "age": age, "email": email}
    return person

# Function for displaying contact list
def display_contact(people):
    for i , person in enumerate(people): 
        # When you use enumerate(), it automatically provides both the index and the value for each item in the list .
        # By using enumerate(), you eliminate the need for manually initializing and updating the index i. 
        # It simplifies your code and makes it cleaner. You can just focus on the loop and the values you're iterating over!
        print(i+1 , "-" , person["name"] , "|" , person["age"] , "|" , person["email"])


# Function for deleting contact
def del_contact(people):
    display_contact(people)
    
    while True:
        number = input("Enter a number to delete : ").strip()
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range...")
            else:
                break
        except ValueError:
            print("Wrong input format, enter numbers...")
    people.pop(number - 1)

# Fundtion for searching contact
def search_contact(people):
    search_name = input("Search for the name: ").strip().lower()
    results = []

    for person in people:
        if search_name in person["name"].lower():
            results.append(person)
    
    if not results:
        print("No contacts found.")
    else:
        display_contact(results)

# Main Program
print(" Hi Welcome to my contact management system where you can save your contact list...")
print()

with open("contacts.json","r") as f:
    people=json.load(f) ["contacts"]

while True:
    print()
    print("contact list size : ",len(people))
    command=input("What do you want to do? (add , delete , search) or press q to Quit the system : ").lower()
    

    if command=="add":
        person=add_contact()
        people.append(person)
        print("New Contact Added...")
    elif command=="delete":
        del_contact(people)
        print("Mentioned Contact Deleted Successfully...")
    elif command=="search":
        search_contact(people)
    elif command=="q":
        print("Exiting the system...")
        break
    else:
        print("Invalid Command . Try again!!!")

# Only after quiting the program data will get appended on the json file.
with open("contacts.json","w") as f:
    json.dump({"contacts":people},f)