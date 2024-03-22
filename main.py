contact={
    "08937462534":"Etom",
    "08937462534":"Danny",
    "08937462534":"Salvador"
}

def show_app_menu():
    """
    show_app_menu This Function will display the app menu
    """

    print("1. View contacts")
    print("2. Add contacts")
    print("3. Search contacts")
    print("4. Exit")


    def select_app_menu():
        repeat=True
        while repeat== True:
            try:
                option =int(input("Choose[1-4]: "))
            except ValueError:
                print("Please input number. ")
                #fill the option with value so the program wont error
                option =0
            if option > 0 and option <6: repeat= False
            if option==1:
                showContact()
                show_app_menu()
            elif option==2:
                contact_str=str(input("Provide Contact Name and Number separated by a comma (eg Myne ega,0890393)"))
                addContacts(contact_str=contact_str)
                show_app_menu()
            elif option==3:
                contact_number=str(input("Provide Contact Name and Number separated by a comma (eg Myne ega,0890393)5"))
                addContacts(number=contact_number)
                show_app_menu()
            elif option ==4:
                print("Good bye!")
                break
            else:
                print("Option unavailable")

def showContact():
    """
    This function is used to view all contact in a list format, it also has an option for deleting or editing any of them.
    """

    num=1
    print('===================================================================')
    print("|No.| Name                              |Number                   |")     
    print('===================================================================')
    for key, val in contact.item():
        # format to left-align and give some spacing
        print("|{no} .| {name:<15} | {number<:15} |".format(no =num, name=val, number =key))
        num += 1
    print('===================================================================')

def addContacts(contact_str: str):
    """
    addContacts this function is used to add new contacts into our dictionary

    Args:
        contact_str(str): Contact Name and Number Separated by

    """
    name, number =contact_str.split(",")
    contact[number] = name
    print("========= Contact Added Succecssfully ==========")

def updateContact(number):
    if number in contact:
        new_name = input("Enter the new name for the contact: ")
        contact[number] = new_name
        print("========= Contact Updated Successfully ==========")
    else:
        print("Contact does not exist in our contact book")

def deleteContact(number):
    if number in contact:
        del contact[number]
        print("========= Contact Deleted Successfully ==========")
    else:
        print("Contact does not exist in our contact book")
        
def searchContacts(number:str):
    record= contact.get(number,None)
    if not record:
        print("======== Contact does not exist in our contact book")
    else:
        num =1
        print('===============================================================')
        print("|No.| Name                              |Number                   |")     
        print('===================================================================')
        print("|{no} .| {name:<15} | {number:<15} |".format(no=num, name= number))
        print('===================================================================')

show_app_menu()

