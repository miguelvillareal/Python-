'#Phone Contacts'
'# Miguel Villareal'
'#10/11/17'

'#Define the main function'
'#Create an empty dictionary and call it contacts'
def main():

    contacts = {}

    create_contact(contacts, "Katie", "Katz", "katie.katz@nau.edu",
                25, "857-294-2758")
    create_contact(contacts, "Jim", "Jones", "jim.jones@nau.edu", 19,
                "525-866-2749")
    create_contact(contacts, "Sarah", "Sanders",
                "sarah.sanders@nau.edu", 18, "593-026-2532")

    '#Print the contacts that have been created'
    print("Creation of Jim Jones: {}".format(
     "Passed" if contains_contact(contacts, "jim", "Jones")
     else "Failed"))

    print("Creation of Katie Katz: {}".format(
     "Passed" if contains_contact(contacts, "Katie", "kaTz") else
     "Failed"))

    print("Creation of Sarah Sanders: {}".format(
     "Passed" if contains_contact(contacts, "Sarah", "Sanders") else
     "Failed"))
    update_contact_age(contacts, "Sarah", "Sanders", 19)

    print("Updating Sarah Sanders age to 19: {}".format(
     "Passed" if get_contact_age(contacts, "sarah", "sanDers") == 19
     else "Failed"))
    update_contact_email(contacts, "Jim", "Jones",
                      "jim.jones@gmail.com")

    print("Updating Jim Jones's email: {}".format(
     "Passed" if get_contact_email(contacts, "jim", "jones") ==
                 "jim.jones@gmail.com" else "Failed"))
    update_contact_number(contacts, "Katie", "Katz", "907-536-2946")

    print("Updating Katie Katz's number: {}".format(
     "Passed" if get_contact_number(contacts, "Katie", "Katz") ==
                 "907-536-2946" else "Failed"))
    display(contacts, "Katie", "Katz")
    display(contacts, "George", "Shaw")

'#Create a function that defines the phone contacts'
def create_contact(contacts, first, last, email, age, phone):
 name = (first + last).upper()
 info = [email, age, phone]
 contacts[name] = info

'#Create a function that updates the phone number'
def update_contact_number(contacts, first, last, phone):

 contacts[(first+last).upper()][2] = phone

'#Create a function that updates the email'
def update_contact_email(contacts, first, last, email):

 contacts[(first + last).upper()][0] = email

'#Create a function that updates the age'
def update_contact_age(contacts, first, last, age):

 contacts[(first + last).upper()][1] = age

'#Create a function that calls for the updated email'
def get_contact_email(contacts, first, last):

  return contacts[(first + last).upper()][0]

'#Create a function that calls for the updated age'
def get_contact_age(contacts, first, last):

 return contacts[(first + last).upper()][1]

'#Create a function that calls for the updated phoen number'
def get_contact_number(contacts, first, last):

 return contacts[(first + last).upper()][2]

'#Create a function that contains the contact and calls upon it'
def contains_contact(contacts,first,last):
  name = (first + last).upper()
  if name in contacts:
      return True

  else:
      return False


'#Display contacts by utilizing print statements'
def display(contacts, first, last):

    if contains_contact(contacts,first,last) == True:
      print(((first).capitalize() + " " + (last).capitalize()))
      print(" The Email is: ", contacts[(first+last).upper()][0])
      print(" The phone is: ", contacts[(first + last).upper()][2])
      print(" The age is: ", contacts[(first + last).upper()][1])

    else:
      print("That contact does not exist in your contacts.")
'#Call the main function'
main()
