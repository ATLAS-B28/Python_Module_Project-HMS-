#here we will be doing all the operations
#a main function with menu driven capablity
from customer import Customer
from booking import Booking
from datetime import datetime
print('''
1) Customer data
      1. Add customer
      2. Update customer
      3. Get customer info
      4. Delete customer
2) Booking rooms
      1. Book rooms
      2. Update booking
      3. Add service
      4. Get booking info
      5. Cancel booking
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
            no_of_guests=int(input("Enter no. of guests: "))
            if no_of_guests>0:
                pass
            else:
                print("Invalid no. of guests")
                break
            customer=Customer(None,phone,email,address,no_of_guests)
            customer.save_or_update()
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
        no_of_guests=int(input("Enter no. of guests: "))
        if no_of_guests>0:
            pass
        else:
            print("Invalid no. of guests")
            return
        customer=Customer(id,phone,email,address,no_of_guests)
        customer.save_or_update()
        return f"Customer id: {id} was updated"

    elif choice==3:
        #Get customer info
        choice_3=int(input("Enter 1 to get one customer, 2 to get all customers: "))
        if choice_3==1:
            id=int(input("Enter customer\'s id: "))
            result=Customer.get_by_id(id)
            return f"Customer {id} details\n"+result
        elif choice_3==2:
            result=Customer.get_all()
            return f"Details of all customers:\n"+result
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
          2. Update booking
          3. Add service
          4. Get booking info
          5. Cancel booking
''')

    choice=int(input("Enter your choice: "))
    if choice==1:
        #Book rooms
        customer_id=int(input("Enter customer\'s id: "))
        room_id=int(input("Enter room id: "))
        check_in_date=input("Enter check in date: ")
        check_in_date=datetime.strptime(check_in_date, "%Y-%m-%d").date()
        check_out_date=input("Enter check out date: ")
        check_out_date=datetime.strptime(check_out_date, "%Y-%m-%d").date()
        booking=Booking(None,customer_id,room_id,check_in_date,check_out_date,None,None)
        booking.save_or_update()
        booking_id=booking.booking_id
        return f"Room was successfully booked. Booking id: {booking_id}"
    elif choice==2:
        #Update booking
        booking_id=int(input("Enter booking id you want to update in : "))
        customer_id=int(input("Enter customer\'s id: "))
        room_id=int(input("Enter room id: "))
        check_in_date=input("Enter check in date: ")
        check_in_date=datetime.strptime(check_in_date, "%Y-%m-%d").date()
        check_out_date=input("Enter check out date: ")
        check_out_date=datetime.strptime(check_out_date, "%Y-%m-%d").date()
        booking=Booking(booking_id,customer_id,room_id,check_in_date,check_out_date,None,None)
        return "Booking updated successfully"
    elif choice==3:
        #Add service
        service_id=int(input("Enter service id: "))
        quantity=int(input("Enter quantity: "))
        # Can be added in update
    elif choice==4:
        #Get booking info
        choice_4=int(input("Enter 1 to get one booking info, 2 to get all booking info: "))
        if choice_4==1:
            id=int(input("Enter booking id: "))
            result=Booking.get_by_id(id)
            return f"Booking {id} details:\n"+result
        elif choice_4==2:
            result=Booking.get_all()
            return f"Details of all bookings:\n"+result
        else:
            return "Invalid choice"
    elif choice==5:
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
        print("Exiting from application.......")
        break
    else:
        print("Invalid choice")
        continue