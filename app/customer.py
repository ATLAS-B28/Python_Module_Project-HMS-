from dbconfig import connect_to_mysql

class Customer:
    def __init__(self, customer_id=None, phone=None, email=None, address=None, no_of_guests=None):
        self.customer_id = customer_id
        self.phone = phone
        self.email = email
        self.address = address
        self.no_of_guests = no_of_guests
    
    def save_or_update(self):
        connection, cursor = connect_to_mysql()
        try:
            if self.customer_id is None:
                query = "INSERT INTO customer (address, phone, email, no_of_guests) VALUES (%s, %s, %s, %s)"
                values = (self.address, self.phone, self.email, self.no_of_guests)
                cursor.execute(query, values)
                self.customer_id = cursor.lastrowid
            else:
                query = "UPDATE customer SET address=%s, phone=%s, email=%s, no_of_guests=%s WHERE customer_id=%s"
                values = (self.address, self.phone, self.email, self.no_of_guests, self.customer_id)
                cursor.execute(query, values)
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    
    @classmethod
    def get_by_id(cls, customer_id):
        connection, cursor = connect_to_mysql()
        try:
            query = "SELECT * FROM customer WHERE customer_id = %s"
            cursor.execute(query, (customer_id,))
            result = cursor.fetchone()
            if result:
                return cls(*result)
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
            query = "SELECT * FROM customer"
            cursor.execute(query)
            results = cursor.fetchall()
            return [cls(*result) for result in results]
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    @classmethod
    def delete(cls,customer_id):
        if customer_id:
            connection, cursor = connect_to_mysql()
            try:
                query = "DELETE FROM customer WHERE customer_id = %s"
                cursor.execute(query, (customer_id,))
                connection.commit()
            except Exception as e:
                print(f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
