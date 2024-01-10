import datetime
import json
users = []
parcel_counter=[10000003]
consignment_number=[10000002]
prices = {}

consignments = {    }


role_checker=None
def login(): #login menu 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open('userlist.json', 'r') as users_list:
        users=json.load(users_list)
    
    if username in users and users[username][password]==password:
        print ("login successful")
        if users[username]["role"] == "Admin":
            print(f"Welcome Admin {username}")
            role_checker=1
            return role_checker
            
        else:
            print(f"Welcome Operator {username}")
            login_operator()
            role_checker=0
            return role_checker
def login_admin(): #menu for admin user
    while True:
        print("\nMenu:")
        print("1. Add a user")
        print("2. View Users")
        print("3. Delete a user")
        print("4. Update Role")
        print("5. Modify prices")
        print("0. Save and Logout")

        Menu_choice = input("Enter your choice: ")

        if Menu_choice == '1':
            add_user()
        elif Menu_choice == '2':
            view_users()
        elif Menu_choice == '3':
            delete_user()
        elif Menu_choice == '4':
            Update_Role()
        elif Menu_choice == '5':
            modify_prices_menu()
        elif Menu_choice == '0':
            print('Successfully saved and logout.')
            break
        else:
            print("Invalid choice. Please choose a valid option.")
def login_operator(): #finished this
    while True:
        print ("\nMenu:")
        print ("1. Add customer details")
        print ("2. Modify customer details")
        print ("3. View list of customers")
        print ("4. Check price")
        print ("5. Modify parcel")
        print ("6. Open bill menu")
        print ("0. Save and Logout")

        Menu_choice= input("Enter your choice: ")

        if Menu_choice == '1':
            add_customer()
        elif Menu_choice == '2':
            modify_customer_details_input()
        elif Menu_choice == '3':
            show_bills()
        elif Menu_choice == '4':
            operator_check_price()
        elif Menu_choice == '5':
            give_parcellist()
        elif Menu_choice == '6':
            bill_menu()
        elif Menu_choice == "0":
            print('Successfully saved and logout. ')
            break
        else:
            print ("Invalid choice. Please choose a valid option.")

def calculate_parcel_price(weight,destination):
    with open('pricelist.json', 'r') as price_list:
        prices = json.load(customer_list)

    if destination in prices and weight <= 3:
        if weight <= 1:
            price= prices[destination]['below_1kg']
            return price
        elif 1 < weight <= 3:#<=3 in order to avoid errors when dealing with parcels of value 3
            price= prices[destination]['1kg_to_3kg']
            return price
        elif weight>3:
            if prices[destination]["above 3kg"]== None:
                print("Price for parcels above 3kg has not been set yet contact an admin")#aks to contact an admin 
            price= prices[destination]["above 3kg", None]
            return price
            
    else:
        return None  # Invalid zone or weight
def modify_prices_menu():#menu for modifying prices
    while True:
        print("\nModify Prices Menu:")
        print("1. View Price")
        print("2. Add Price")
        print("3. Update Price")
        print("4. Delete Price")
        print("5. Check Price")
        print("0. Back to Main Menu")

        price_choice = input("Enter your choice: ")
        if price_choice == '1':
            view_all_price_list()
        elif price_choice == '2':
            add_price()
        elif price_choice == '3':
            update_price()
        elif price_choice == '4':
            delete_price()
        elif price_choice == '5':
            admin_check_price()
        elif price_choice == '0':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def bill_menu():
    while True:
        print ("\nBill menu")
        print ("1. Create bill")
        print ("2. Calculate parcel price")
        print ("3. Modify Parcel details")
        print ("4. Delete parcel")
        print ("5. Search bill")
        print ("6. View customer bills")
        print ("0. Back to Main Menu")

        bill_choice = input("Enter your choice: ")
        if bill_choice == '1':
            create_new_bill()
        elif bill_choice == '2':
            operator_check_price()
        elif bill_choice == '3':
            modify_prices_menu()
        elif bill_choice == '4':
            delete_parcel()
        elif bill_choice == '5':
            customer_bills()
        elif bill_choice == '6':
            date_bills()
        elif bill_choice == '0':
            break
        else:
            print ("Invalid choice. Please choose a valid option")

def add_user(): #adds username and password which will be saved in variables
        with open('userlist.json', 'r') as users_list:
            users=json.load(users_list)
        new_username = input("Enter new username: ")
        new_password = input("Enter password for the new user: ")

        while new_username in users:
            print(f"Username '{new_username}' already exists. Please choose another username.")
            new_username = input("Enter new username: ")
            
        users[new_username] = {"password": new_password, "role":"Operator"}
        json_object = json.dumps(users, indent=4)
        with open("userslist.json", "w") as outfile:
            outfile.write(json_object)
        print(f"User '{new_username}' added successfully with default role operator.")
    
def Update_Role(): #updates role for a user and outputs an error if it is not present in userlist
    with open('userlist.json', 'r') as users_list:
        users=json.load(users_list)
    while True:
        username_to_update = input("Enter the username to update role: ")
        if username_to_update in users:
            if users[username_to_update]['role'] == 'Administrator':
                users[username_to_update]['role'] = 'Operator'
                print(f"User'{username_to_update}' has been updated")
                users[username_to_update]['role'].append(users)
                json_object = json.dumps(users, indent=4)
                with open("userslist.json", "w") as outfile:
                    outfile.write(json_object)
                break
            elif users[username_to_update]['role'] == 'Operator':
                users[username_to_update]['role'] = 'Administrator'
                print(f"User '{username_to_update}' has been updated")
                users[username_to_update]['role'].append(users)
                json_object = json.dumps(users, indent=4)
                with open("userslist.json", "w") as outfile:
                    outfile.write(json_object)
                break
        else:
            print(f"User '{username_to_update}' does not exist. Please enter again.")
                
def view_users(): #prints a list of users in user list using a for loop including user role
        with open('userlist.json', 'r') as users_list:
            users=json.load(users_list)
        print("Users in the system:")
        for username, user_info in users.items():
            print(f"Username: {username}, Role: {user_info['role']}")
#delete user function checks if the user is an admin which cannot be deleted
def delete_user():
    with open('userlist.json', 'r') as users_list:
        users=json.load(users_list)
    while True:
        username_to_delete = input("Enter the username to delete: ")
        if username_to_delete in users:
            if users[username_to_delete]['role'] == 'Administrator': #checks whether user to be deleted is an admin which cannot be deleted
                print(f"Can't delete this admin.")
            else:    
                del users[username_to_delete]
                print(f"User '{username_to_delete}' deleted successfully.")
                json_object = json.dumps(users, indent=4)
                with open("userslist.json", "w") as outfile:
                    outfile.write(json_object)
                break
        else:
            print(f"User '{username_to_delete}' does not exist") #outputs an error if the username is not found

def view_list_users(): #gives an option to see a list of viewers
    with open('userlist.json', 'r') as users_list:
        users=json.load(users_list)
    option=""
    print("\nUser list menu")
    print("1. Admin users")
    print("2. Operators")
    print("3. All users")
    option=str(input(option))
    if option=='1':
        for user in users:
            if user["role"]=="admin":
                print (user["username"], "\tRole:", user["role"])
    if option=='2':
        for user in users:
            if user['role']=="operator":
                print(user['username'], "\tRole:", user["role"])
    if option =="3":
        for user in users:
            print(user["username"], "\tRole:", user["role"])
    
def add_price(): #sets price to parcels above 3kg to a destination
    with open('pricelist.json', 'r') as price_list:
        prices = json.load(customer_list)
    while True:
        destination = input("Please enter your destination: ")
        new_price="{:.2f}".format(float(input("Enter new price:  ")))
        if destination in prices:
            if "above 3 kg" in prices[destination]:
                print(f"Price for {destination} has already been added :)")#if price for destination has already been added
                break
            else:
                prices[destination]["above 3kg"]= new_price
                print(f"Price for parcels over 3kg to {destination} set to RM{new_price}")#destination set and output
                json_object = json.dumps(prices, indent=4)
                with open("pricelist.json", "w") as outfile:
                    outfile.write(json_object)
        else:
            print("destination not found")#error message if destination is not found
        break

def update_price():#updates price for an existing entry
    with open('pricelist.json', 'r') as price_list:
        prices = json.load(customer_list)
    while True:
        destination= input("Please enter your destination:  ")
        if destination not in prices:
            print("Please input a valid destination eg. Zone A")#outputs error if it doesn't find anything
        else:
            break
    new_price=("{:.2f}".format(float(input("Enter new price for you destination:  "))))
    if destination in prices:
        if "above 3kg" in prices[destination]:
            prices[destination]['above 3kg']=new_price
            print(f"Price for {destination} has been updated to RM{new_price}")
            json_object = json.dumps(prices, indent=4)
            with open("pricelist.json", "w") as outfile:
                    outfile.write(json_object)
        else:
            print(f"Price for {destination} has not been added yet")#gives an error if price has not been added yet
    else:
        print ("Invalid destination")#error if it has not been found

def delete_price():
    with open('pricelist.json', 'r') as price_list:
        prices = json.load(customer_list)
    while True:
        destination=input("Enter destination of price you want to delete >3kg")
        if destination not in prices:
            print("destination not found please enter a valid destination")
        else:
            break
    if "above 3 kg" in prices[destination]:
        del prices[destination]["above 3 kg"]
        print(f"Price for {destination} has been deleted")
        json_object = json.dumps(prices, indent=4)
        with open("pricelist.json", "w") as outfile:
            outfile.write(json_object)
    else:
        print("price has not been added yet for destination yet")

#checks price of a parcel using weight and destination with simple logic checks
def admin_check_price():
    with open('pricelist.json', 'r') as price_list:
        prices = json.load(customer_list)
    weight=int(input("Enter weight of parcel:  "))
    while True:
        if weight<0 and weight>1000:
            print("Please enter a valid weight greather than 0 and less than 1000")
            weight=int(input("Enter weight of parcel:  "))
        else:
            break
    destination=str(input("Enter destination of parcel:   "))
    while True:
        if destination not in prices:
            print("Enter a valid destination Eg. Zone E")
            destination=str(input("Enter destination of parcel:   "))
        else:
            break
    if weight<1:
        print(f"Price of parcel of weight {weight} and destination {destination} is: RM{prices[destination]['below_1kg']}")
    elif 1<weight<3:
        print(f"Price of parcel of weight {weight} and destination {destination} is: RM{prices[destination]['1kg_to_3kg']}")
    else:
        if weight>=3:
            if "above 3kg" in prices[destination]:
                print(f"Price of parcel of weight {weight} and destination {destination} is: RM{prices[destination]['above 3kg']}")
            else:
                print(f"price has not been added for {destination} yet")
                pass
        pass

    
       
def view_all_price_list():
    with open('pricelist.json', 'r') as price_list:
        prices = json.load(customer_list)
    Z=["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"] #all zone names to be added in for loop assuming new zones will not be added
    for letters in Z:
        print(f"Prices for parcels going to {letters} \t")
        print(f"Price for parcels below 1kg is {prices[letters]['below_1kg']}\t Price for parcels between 1kg and 3kg is {prices[letters]['1kg_to_3kg']}")
        print(f"Price for parcels between 1kg and 3kg is {prices[letters]['1kg_to_3kg']}")#incredibly messed up typing but code works and i cant be bothered to fix it
        if "above 3kg" in prices[letters]:
            print(f"Price for parceks between 1kg and 3kg is {prices[letters]['above 3kg']}")
        else:
            print(f"Price for parcels going to {Z} above 3kg has not been added yet")#outputs when price for a zone has not been added yet


customer_list=[
   {   
        "id": "C000001",
        "name":"Sender1",
        "address":"S_Address1",
        "number":"111111111"
    },
   {
        "id": "C000002",
        "name":"Sender2",
        "address":"S_Address",
        "number":"111111113"
    }
]

# Initialize variables


# Define functions for customer management
def add_customer():
    with open('customerlist.json', 'r') as customer_list:
        customer_list = json.load(customer_list)

    "Adds a new customer to the database."
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    phone_number = input("Enter customer phone number: ")

    # Generate unique customer ID
    customer_id_generator = len(customer_list) + 1
    new_customer_id = f'C{customer_id_generator:06}'
    customer_data = {"id":new_customer_id, "name": name, "address": address, "phone_number": phone_number}
    customer_list.append(customer_data)

    print(f"Customer added successfully! ID: {new_customer_id}")
    json_object = json.dumps(prices, indent=4)
    with open("customerlist.json", "w") as outfile:
        outfile.write(json_object)
    
    return name, address, phone_number


def modify_customer_details(customer_list, customer_id, new_name=None, new_address=None, new_number=None):
    with open('customerlist.json', 'r') as customer_list:
        customer_list = json.load(customer_list)

    for customer in customer_list:
        if customer["id"] == customer_id:
            if new_name is not None:
                new_name=input("Update customer name Leave blank to pass: ")
                if new_name=="":
                    pass
                else:
                    customer["name"] = new_name
                    change_sender_name_for_customer(consignments, customer_id, new_name)
                    json_object = json.dumps(prices, indent=4)
                    with open("customerlist.json", "w") as outfile:
                        outfile.write(json_object)

            if new_address is not None:
                new_address=input("Update customer address Leave blank to pass: ")
                if new_address=="":
                    pass 
                else:
                    customer["address"] = new_address
                    json_object = json.dumps(prices, indent=4)
                    with open("customerlist.json", "w") as outfile:
                        outfile.write(json_object)
            if new_number is not None:
                new_number=input("Update customer number Leave blank to pass: ")
                if new_number=="":
                    pass 
                else:
                    customer["number"] = new_number
                    json_object = json.dumps(prices, indent=4)
                    with open("customerlist.json", "w") as outfile:
                            outfile.write(json_object)
            return True  # Customer found and modified successfully
    return False  # Customer with the given ID not found

def modify_customer_details_input():
    with open('customerlist.json', 'r') as customer_list:
        customer_list = json.load(customer_list)

    while True:
        customer_id_to_modify = str(input("Enter customer details to input eg.C000001:   "))
        success = modify_customer_details(customer_list, customer_id_to_modify, new_name="NewSenderName", new_address="NewAddress", new_number="999999999")

        if success:
            print("Customer information modified successfully.")
            json_object = json.dumps(prices, indent=4)
            with open("customerlist.json", "w") as outfile:
                outfile.write(json_object)
            break
        else:
            print(f"Customer with ID {customer_id_to_modify} not found. \n List of customers\n{customer_list}")

        # Print the updated customer_list
        print("Customer List update")
   

def change_sender_name_for_customer(consignments, customer_id, new_sender_name):
    with open('customerlist.json', 'r') as customer_list:
        customer_list = json.load(customer_list)

    for consignment_id, consignment_data in consignments.items():
        if consignment_data["CustomerID"] == customer_id:
            for parcel_id, parcel_data in consignment_data["Parcel"].items():
                parcel_data["SenderName"] = new_sender_name
                json_object = json.dumps(prices, indent=4)
                with open("customerlist.json", "w") as outfile:
                    outfile.write(json_object)
                

def get_parcels_received(consignments, input_date, destination):
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    received_parcels = []

    for consignment_id, consignment_data in consignments.items():
        consignment_date = consignment_data["DateTime"]
        if consignment_date == input_date:
            for parcel_id, parcel_data in consignment_data["Parcel"].items():
                parcel_destination = parcel_data["ReceiverAddress"]
                if parcel_destination == destination:
                    received_parcels.append({
                        "ConsignmentID": consignment_id,
                        "ParcelID": parcel_id,
                        "SenderName": parcel_data["SenderName"],
                        "ReceiverName": parcel_data["ReceiverName"],
                        "ParcelWeight (kg)": parcel_data["ParcelWeight (kg)"],
                        "ParcelZone": parcel_data["ParcelZone"],
                        "ParcelPrice (RM)": parcel_data["ParcelPrice (RM)"]
                    })
                        

    return received_parcels

def get_parcels_operator():
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    while True:
        date=input("Please enter date DD/MM/YYYY: ")
        if is_date_present(consignments, date):
            break
        else:
            print("Date not found, enter in DD/MM/YYYY format")
            
            

    while True:
        destination = input("Please enter destination to check")
        if find_parcel_in_zone(consignments, destination):
            parcel_in_zone = find_parcel_in_zone(consignments, destination)
            print(f"Parcel found in Zone {destination}:\n{parcel_in_zone}")
        else:
            print(f"No parcels found in Zone {destination} in the consignments. With given date")
        

    


    # Print the list of received parcels

def is_date_present(consignments, input_date):
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    for consignment_data in consignments.values():
        consignment_date = consignment_data.get("DateTime")
        if consignment_date == input_date:
            return True
    return False

def find_parcel_in_zone(consignments, input_zone):
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    for consignment_id, consignment_data in consignments.items():
        for parcel_id, parcel_data in consignment_data.get("Parcel", {}).items():
            if parcel_data.get("ParcelZone") == input_zone:
                return {
                    "ConsignmentID": consignment_id,
                    "ParcelID": parcel_id,
                    "SenderName": parcel_data["SenderName"],
                    "ReceiverName": parcel_data["ReceiverName"],
                    "ParcelWeight (kg)": parcel_data["ParcelWeight (kg)"],
                    "ParcelZone": parcel_data["ParcelZone"],
                    "ParcelPrice (RM)": parcel_data["ParcelPrice (RM)"]
                }
    return None


        
def is_valid_customer_in_list(customer_ID,customer_list):
    with open('customerlist.json', 'r') as customer_list:
        customer_list = json.load(customer_list)
    for customer_ID in customer_list:
        if customer_ID == customer_list.get("id"):
            return True
    return False


def is_valid_customer_in_cosignment(consignments, customer_ID):
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)

    for consignment_data in consignments.values():
        consignment_customer=consignment_data.get("CustomerID")
        if consignment_customer==customer_ID:
            return True
    return False

def is_valid_customer():
    if (is_valid_customer_in_cosignment and is_valid_customer_in_list)==True:
        return True
    else:
        return False

bill_ledger = []


def create_new_bill(customer_name, consignment_number):
    """Creates a new bill for a customer."""
    if is_valid_customer(customer_name):
        new_bill = {
            'customer_name': customer_name,
            'consignment_number': consignment_number,
            'parcels': []
        }
        bill_ledger.append(new_bill)
        return new_bill
    else:
        return "Customer details are invalid or not added."


# -- Parcel Management --
    
def add_parcel_to_cosignment():
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    address=""
    name=""
    phone_number=""
    price=0
    add_customer()
    parcel_counter+=1
    weight=int(input("Enter parcel weight: "))
    destination=str(input("Please enter parcel destination eg Zone A: "))
    calculate_parcel_price(weight, destination)
    consignments[consignment_number]["Parcel"][parcel_counter]={

            "SenderName": name,
            "SenderAddress": address,
            "SenderPhoneNo": phone_number,
            "ReceiverName": "To be added",
            "ReceiverAddress": "To be added",
            "ReceiverPhoneNo": "To be added",
            "ParcelWeight (kg)": "To be added",
            "ParcelZone": destination,
            "ParcelPrice (RM)": price

    }
    json_object = json.dumps(consignments, indent=4)
    with open("cosignment_data.json", "w") as outfile:
        outfile.write(json_object)
    return consignments

def add_parcel_to_bill():
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    ID=int(input("Please enter consignment number"))
    if ID in consignments:
        add_parcel_to_cosignment()
    else:
        consignment_number+=1
        add_parcel_to_cosignment
    return consignments

def modify_parcels_details():
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    option=None
    
    ID=input("Enter Cosignment number: ")
    if ID in consignments:
        while True:
            parcel_ID=input("Enter parcel number: ")
            if parcel_ID in consignments[ID]:
                while True:
                    print("1. Change name")
                    print("2. Change address")
                    print("3. Change phone number")
                    print("0. Leave the menu")
                    option==int(input("Please enter an option"))
                    if option==1:
                        name=input("Please enter new name of customer: ")
                        name=name
                    elif option==2:
                        address=input("Enter new address of customer: ")
                        address=address
                    elif option==3:
                        number=input("Please enter new phone number of customer: ")
                        number=number
                    elif option==0:
                        break
                    else:
                        print("Invalid option")
                consignments[ID]["Parcel"][parcel_ID].update({

                            "SenderName": name,
                            "SenderAddress": address,
                            "SenderPhoneNo": number
                    }
                    )
                json_object = json.dumps(consignments, indent=4)
                with open("cosignment_data.json", "w") as outfile:
                    outfile.write(json_object)
                
            else:
                print("Parcel ID not found in cosignment")\
    
    else:
        print("Cosignment ID not found")
            

def modify_parcel_zone():
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    option=None
    ID=input("Enter Cosignment number: ")
    if ID in consignments:
        while True:
            parcel_ID=input("Enter parcel number: ")
            if parcel_ID in consignments[ID]:
                while True:
                    print("1. Change destination")
                    print("2. Change weight")
                    print("0. Exit menu")
                    if option==1:
                        destination=input("Enter destination of the parcel Eg. Zone C")
                        while True:
                            if destination in prices:
                                break
                            else:
                                destination=input("Enter a valid destination Eg, Zone B")
                           
                    elif option==2:
                        weight=input("Please enter parcel weight in kg")
                        weight=weight

                    elif option==0:
                        break
                    else:
                        print("enter a valid option")
                consignments[ID]["Parcel"][parcel_ID].update({

                                "ParcelWeight (kg)": weight,
                                "ParcelZone": destination
                                
                        })
                json_object = json.dumps(consignments, indent=4)
                with open("cosignment_data.json", "w") as outfile:
                    outfile.write(json_object)
            else:
                print(f"Parcel ID: {parcel_ID} not found in consignment{ID}")   
    else:
        print ("Cosignment ID not found")

def give_parcellist():
    option=None
    while option!=0:
        print("1.Modify Parcel details")
        print("2.Modify Parcel price")
        print("0.EXIT")
        option=int(input("enter an option"))
        if option ==1:
            modify_parcels_details()
        elif option ==2: 
            modify_parcel_zone()
        else:
            print("Enter a valid option")


                
def delete_parcel():
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    consignment_number=input("Enter consignment number")
    if consignment_number in consignments:
        parcel_number=input("Enter parcel number")
        if parcel_number in consignments[consignment_number]["Parcel"]:
            del consignments[consignment_number]["Parcel"][parcel_number]
            print(f"Parcel {parcel_number} deleted from consignment {consignment_number}.")
            json_object = json.dumps(consignments, indent=4)
            with open("cosignment_data.json", "w") as outfile:
                outfile.write(json_object)
        else:
            print(f"Parcel number {parcel_number} not found in consignment {consignment_number}.")
    else:
        print(f"Consignment number {consignment_number} not found.")
                    

def show_bills():
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    while True:
        consignment_number_to_search = input("Enter Cosignment number")

        if consignment_number_to_search in consignments:
            consignment_details = consignments[consignment_number_to_search]
            print(f"Consignment Number: {consignment_number_to_search}")
            print(f"DateTime: {consignment_details['DateTime']}")
            print(f"CustomerID: {consignment_details['CustomerID']}")

            print("Parcels:")
            for parcel_number, parcel_details in consignment_details["Parcel"].items():
                print(f"  Parcel Number: {parcel_number}")
                print(f"    Sender Name: {parcel_details['SenderName']}")
                print(f"    Sender Address: {parcel_details['SenderAddress']}")
                print(f"    Sender Phone No: {parcel_details['SenderPhoneNo']}")
                print(f"    Receiver Name: {parcel_details['ReceiverName']}")
                print(f"    Receiver Address: {parcel_details['ReceiverAddress']}")
                print(f"    Receiver Phone No: {parcel_details['ReceiverPhoneNo']}")
                print(f"    Parcel Weight (kg): {parcel_details['ParcelWeight (kg)']}")
                print(f"    Parcel Zone: {parcel_details['ParcelZone']}")
                print(f"    Parcel Price (RM): {parcel_details['ParcelPrice (RM)']}")
                print()

            print("=" * 50)
            break
        else:
            print(f"Consignment number {consignment_number_to_search} not found.")

def customer_bills(): 
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)
    
    customer_to_search = input("Please enter customer id")
    total_price=0
    found_bills = []

    for consignment_number, consignment_details in consignments.items():
        if consignment_details["CustomerID"] == customer_to_search:
            found_bills.append({
                "ConsignmentNumber": consignment_number,
                "DateTime": consignment_details["DateTime"],
                "Parcels": consignment_details["Parcel"]
            })

    if found_bills:
        print(f"Bills for Customer ID: {customer_to_search}")
        for bill in found_bills:
            print("=" * 50)
            print(f"Consignment Number: {bill['ConsignmentNumber']}")
            print(f"DateTime: {bill['DateTime']}")
            print("Parcels:")
            for parcel_number, parcel_details in bill["Parcels"].items():
                print(f"  Parcel Number: {parcel_number}")
                print(f"    Sender Name: {parcel_details['SenderName']}")
                print(f"    Sender Address: {parcel_details['SenderAddress']}")
                print(f"    Sender Phone No: {parcel_details['SenderPhoneNo']}")
                print(f"    Receiver Name: {parcel_details['ReceiverName']}")
                print(f"    Receiver Address: {parcel_details['ReceiverAddress']}")
                print(f"    Receiver Phone No: {parcel_details['ReceiverPhoneNo']}")
                print(f"    Parcel Weight (kg): {parcel_details['ParcelWeight (kg)']}")
                print(f"    Parcel Zone: {parcel_details['ParcelZone']}")
                print(f"    Parcel Price (RM): {parcel_details['ParcelPrice (RM)']}")
                total_price+={parcel_details['ParcelPrice (RM)']}
                print()
        print(f"Total price for customer with ID{customer_to_search} is {total_price}")
    else:
        print(f"No bills found for Customer ID: {customer_to_search}")

def is_within_date_range(date_str, start_date, end_date):
    date = datetime.strptime(date_str, "%d/%m/%Y")
    return start_date <= date <= end_date


def date_bills():
    with open('consignment_data.json','r') as consignment_list:
        consignments=json.load(consignment_list)

    customer_to_search = input("Enter customer ID")
    start_date_str = input("enter date starting date in dd/mm/yy format")
    end_date_str = input("enter end date in dd/mm/yyyy format")

    start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y")

    found_bills = []

    for consignment_number, consignment_details in consignments.items():
        if consignment_details["CustomerID"] == customer_to_search and \
                is_within_date_range(consignment_details["DateTime"], start_date, end_date):
            found_bills.append({
                "ConsignmentNumber": consignment_number,
                "DateTime": consignment_details["DateTime"],
                "Parcels": consignment_details["Parcel"]
            })

    for consignment_number, consignment_details in consignments.items():
        if consignment_details["CustomerID"] == customer_to_search and \
            is_within_date_range(consignment_details["DateTime"], start_date, end_date):
            found_bills.append({
            "ConsignmentNumber": consignment_number,
            "DateTime": consignment_details["DateTime"],
            "Parcels": consignment_details["Parcel"]
        })

    if found_bills:
        print(f"Bills for Customer ID: {customer_to_search} between {start_date_str} and {end_date_str}")
        for bill in found_bills:
            print("=" * 50)
            print(f"Consignment Number: {bill['ConsignmentNumber']}")
            print(f"DateTime: {bill['DateTime']}")
            print("Parcels:")
            for parcel_number, parcel_details in bill["Parcels"].items():
                print(f"  Parcel Number: {parcel_number}")
                print(f"    Sender Name: {parcel_details['SenderName']}")
                print(f"    Sender Address: {parcel_details['SenderAddress']}")
                print(f"    Sender Phone No: {parcel_details['SenderPhoneNo']}")
                print(f"    Receiver Name: {parcel_details['ReceiverName']}")
                print(f"    Receiver Address: {parcel_details['ReceiverAddress']}")
                print(f"    Receiver Phone No: {parcel_details['ReceiverPhoneNo']}")
                print(f"    Parcel Weight (kg): {parcel_details['ParcelWeight (kg)']}")
                print(f"    Parcel Zone: {parcel_details['ParcelZone']}")
                print(f"    Parcel Price (RM): {parcel_details['ParcelPrice (RM)']}")
                print()
    else:
        print(f"No bills found for Customer ID: {customer_to_search} between {start_date_str} and {end_date_str}")




        
def operator_check_price():
    with open('pricelist.json', 'r') as price_list:
        prices = json.load(customer_list)
    weight=int(input("Enter weight of parcel:  "))
    while True:
        if weight<0 and weight>1000:
            print("Please enter a valid weight greather than 0 and less than 1000")
            weight=int(input("Enter weight of parcel:  "))
        else:
            break
    destination=str(input("Enter destination of parcel:   "))
    while True:
        if destination not in prices:
            print("Enter a valid destination Eg. Zone E")
            destination=str(input("Enter destination of parcel:   "))
        else:
            break
    if weight<1:
        print(f"Price of parcel of weight {weight} and destination {destination} is: RM{prices[destination]['below_1kg']}")
    elif 1<weight<3:
        print(f"Price of parcel of weight {weight} and destination {destination} is: RM{prices[destination]['1kg_to_3kg']}")
    else:
        if weight>=3:
            if "above 3kg" in prices[destination]:
                print(f"Price of parcel of weight {weight} and destination {destination} is: RM{prices[destination]['above 3kg']}")
            else:
                print(f"price has not been added for {destination} yet, please contact and admin to set a price")
                pass
        pass

# -- Bill Retrieval and Modifications --




login()
if role_checker==1:
    login_admin()
else:
    login_operator()

