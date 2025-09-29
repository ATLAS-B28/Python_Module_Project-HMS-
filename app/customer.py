from dbconfig import connect_to_mysql

class Customer:
    def __init__(self, phone=None, email=None, address=None, customer_id=None):
        self.customer_id = customer_id
        self.phone = phone
        self.email = email
        self.address = address
    
    def save(self):
        connection, cursor = connect_to_mysql()
        try:
            query = "INSERT INTO customer (address, phone, email) VALUES (%s, %s, %s)"
            values = (self.address, self.phone, self.email)
            cursor.execute(query, values)
            self.customer_id = cursor.lastrowid
            connection.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def update(self, customer_id):
        connection, cursor = connect_to_mysql()
        try:
            query = "UPDATE customer SET phone=%s, email=%s, address=%s WHERE customer_id=%s"
            values = (self.phone, self.email, self.address, customer_id)
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
                return cls(phone=result[2], email=result[3],address=result[1], customer_id=result[0])
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
            return [cls(phone=result[2], email=result[3], address=result[1], customer_id=result[0]) for result in results]
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

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"
