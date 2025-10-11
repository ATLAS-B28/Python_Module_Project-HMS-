#here we will be doing all the operations
#a main function with menu driven capablity
from customer import Customer
from booking import Booking
from room import Room
from dbconfig import close_db_connection
from datetime import datetime
print("\t\t\t\t\t\t\t\tWelcome to Hotel Management System")
print('''
1) Customer data
      1. Add customer
      2. Update customer
      3. Get customer info
      4. Delete customer
2) Booking rooms
      1. Book rooms
      2. Get booking info
      3. Cancel booking
3) Exit
''')
# Customer
def customer_operations():
    print('''
            1. Add customer
            2. Update customer
            3. Get customer info
            4. Delete customer
        ''')
    choice=int(input("Enter your choice: "))
    if choice==1:
        #Add customer
        while True:
            email=input("Enter customer\'s email: ")
            phone=int(input("Enter customer\'s phone no.: "))
            if phone>0:
                pass
            else:
                print("Invalid phone no.")
                break
            address=input("Enter customer\'s address: ")
            customer=Customer(phone,email,address)
            customer.save()
            id= customer.customer_id
            print(f"Customer with id: {id} was added")
            print("Do you want to add more customers?")
            y=input("Enter y\\yes to add more customers: ").strip().lower()
            if y=='y' or y=='yes':
                continue
            else:
                break
        return "All customers were added successfully"

    elif choice==2:
        #Update customer
        id=int(input("Enter customer\'s id that you want to update in: "))
        email=input("Enter customer\'s email: ")
        phone=int(input("Enter customer\'s phone no.: "))
        if phone>0:
            pass
        else:
            print("Invalid phone no.")
            return
        address=input("Enter customer\'s address: ")
        customer=Customer(id,phone,email,address)
        customer.update()
        return f"Customer id: {id} was updated"

    elif choice==3:
        #Get customer info
        choice_3=int(input("Enter 1 to get one customer, 2 to get all customers: "))
        if choice_3==1:
            id=int(input("Enter customer\'s id: "))
            result=Customer.get_by_id(id)
            if result:
                return f"Customer {id} details\n"+str(result)
            else:
                return f"Customer with id {id} not found"
        
        elif choice_3==2:
            result=Customer.get_all()
            if result:
             customers_str = "\n".join([str(customer) for customer in result])
             return f"Details of all customers:\n"+customers_str
            else:
             return "No customers found"
        else:
            return "Invalid choice"

    elif choice==4:
        #Delete customer
        id=int(input("Enter customer\'s id that you want to delete: "))
        Customer.delete(id)
        return f"Customer with id: {id} was deleted"   
    else:
        return "Invalid choice"

def booking_operations():
    print('''
          1. Book rooms
          2. Get booking info
          3. Cancel booking
        ''')

    choice=int(input("Enter your choice: "))
    if choice==1:
        #Book rooms
        customer_id=int(input("Enter customer\'s id: "))
        customer = Customer.get_by_id(customer_id)
        if not customer:
            return f"Customer with id {customer_id} does not exist. Please add the customer first."
        
        check_in_date=input("Enter check in date: ")
        check_out_date=input("Enter check out date: ")
        room_list=Room.get_available_rooms(check_in_date, check_out_date)
        if not room_list:
            return "No rooms available for the given dates. Please try different dates."
        print("Available rooms:")
        for i, room in enumerate(room_list, 1):
            print(f"{i}. {room}")
       
        room_id=int(input("Enter room id: "))
        room = Room.get_room_by_id(room_id)
        if not room:
            return f"Room with id {room_id} does not exist. Please choose a valid room."
        
        
        no_of_guests=int(input("Enter number of guests: "))
        if no_of_guests <= 0:
            return "Number of guests must be a positive integer."
        room_capacity=Room.get_room_capacity(room_id)
        if room_capacity < no_of_guests:
            return f"Room with id {room_id} does not have enough capacity for {no_of_guests} guests."
        
        room_price=Room.get_cost(room_id)
        if not room_price:
            return f"Could not retrieve price for room id {room_id}."
        room_name=Room.get_room_by_id(room_id)

        print(f"Room name: {room_name.room_type}")
        print(f"Room price: {room_price}")
        y=input("Enter y\\yes to confirm booking: ").strip().lower()
        if y!='y' and y!='yes':
            return "Booking cancelled by user."

        booking=Booking(customer_id,room_id,check_in_date,check_out_date, room_price, no_of_guests)
        booking.save()

        booking_id=booking.booking_id
        return f"Room was successfully booked. Booking id: {booking_id}"

    elif choice==2:
        #Get booking info
        choice_4=int(input("Enter 1 to get one booking info, 2 to get all booking info: "))
        if choice_4==1:
            id=int(input("Enter booking id: "))
            result=Booking.get_by_id(id)
            if result:
             return f"Booking {id} details:\n"+str(result)
            else:
             return f"Booking with id {id} not found"
        elif choice_4==2:
            result=Booking.get_all()
            if result:
             bookings_str = "\n".join([str(booking) for booking in result])
             return f"Details of all bookings:\n"+bookings_str
            else:
              return "No bookings found"
        else:
            return "Invalid choice"
    elif choice==3:
        #Cancel booking
        id=int(input("Enter booking id you want to delete: "))
        Booking.delete(id)
        return f"Booking {id} was deleted"
    else:
        return "Invalid choice"

while True:
    choice_main=int(input("Select 1 to for updating customer data, 2 for booking data, 3 for exiting: "))
    if choice_main==1:
        #Customer
        print(customer_operations())
    elif choice_main==2:
        #Booking
        print(booking_operations())
    elif choice_main==3:
        close_db_connection()
        print("Exiting from application.......")
        break
    else:
        print("Invalid choice")
        continue