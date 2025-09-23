#here create bookings, get by id, delete by id, get all
from dbconfig import connect_to_mysql
from datetime import datetime

class Booking:
    def __init__(self, booking_id=None, customer_id=None, room_id=None, check_in_date=None, check_out_date=None, total_price=None, services=None):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.room_id = room_id
        self.check_in_date = datetime.strptime(check_in_date, "%Y-%m-%d").day
        self.check_out_date = datetime.strptime(check_out_date, "%Y-%m-%d").day
        self.total_price = total_price
        self.total_days = self.check_out_date - self.check_in_date
        self.services = services or []

    def save_or_update(self):
        connection, cursor = connect_to_mysql()
        try:
            if self.booking_id is None:
                query = "INSERT INTO booking (total_price, check_in_date, check_out_date, total_days, customer_id, room_id) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (self.total_price, self.check_in_date, self.check_out_date, self.total_days, self.customer_id, self.room_id)
                cursor.execute(query, values)
                self.booking_id = cursor.lastrowid

                for service_id, qunatity in self.services:
                    cursor.execute("INSERT INTO booking_service (booking_id, service_id, quantity) VALUES (%s, %s, %s)", (self.booking_id, service_id, qunatity))
            else:
                query = "UPDATE booking SET total_price=%s, check_in_date=%s, check_out_date=%s, total_days=%s, customer_id=%s, room_id=%s WHERE booking_id=%s"
                values = (self.total_price, self.check_in_date, self.check_out_date, self.total_days, self.customer_id, self.room_id, self.booking_id)
                cursor.execute(query, values)
                cursor.execute("DELETE FROM booking_service WHERE booking_id = %s", (self.booking_id, ))
                for service_id, qunatity in self.services:
                    cursor.execute("INSERT INTO booking_service (booking_id, service_id, quantity) VALUES (%s, %s, %s)", (self.booking_id, service_id, qunatity))
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def add_service(self, service_id, quantity):
        connection, cursor = connect_to_mysql()
        try:
            cursor.execute("INSERT INTO booking_service (booking_id, service_id, quantity) VALUES (%s, %s, %s)", 
                         (self.booking_id, service_id, quantity))
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def get_by_id(cls, booking_id):
        connection, cursor = connect_to_mysql()
        try:
            query = "SELECT * FROM booking WHERE booking_id = %s"
            cursor.execute(query, (booking_id,))
            res = cursor.fetchone()
            if res:
                return cls(*res)
            return None
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def get_all(cls):
        connection, cursor = connect_to_mysql()
        try:
            query = "SELECT * FROM booking"
            cursor.execute(query)
            res = cursor.fetchall()
            return [cls(*result) for result in res]
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    
    def delete(self, booking_id):
        if booking_id:
            connection, cursor = connect_to_mysql()
            try:
                query = "DELETE FROM booking WHERE booking_id = %s"
                cursor.execute(query, (booking_id, ))
                connection.commit()
            except Exception as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()