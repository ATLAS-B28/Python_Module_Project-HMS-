from dbconfig import connect_to_mysql

class Room:
    def __init__(self, room_id, room_type, price, capacity):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
    
    def __str__(self):
        return f"Room ID: {self.room_id}, Room Type: {self.room_type}, Price: {self.price}"
    
    @classmethod
    def get_room_name(cls,room_id):
        connection, cursor = connect_to_mysql()
        try:
            query = "SELECT room_name FROM room WHERE room_id = %s"
            cursor.execute(query, (room_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            return None
        except Exception as e:
            connection.rollback()
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    @classmethod
    def get_cost(cls, room_id):
        connection, cursor = connect_to_mysql()
        try:
            query = "SELECT price FROM room WHERE room_id = %s"
            cursor.execute(query, (room_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            return None
        except Exception as e:
            connection.rollback()
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    @classmethod
    def get_room_by_id(cls, room_id):
        connection, cursor = connect_to_mysql()
        try:
            query = "SELECT * FROM room WHERE room_id = %s"
            cursor.execute(query, (room_id, ))
            result = cursor.fetchone()
            if result:
                return Room(*result)
            return None
        except Exception as e:
            connection.rollback()
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    @classmethod
    def get_room_capacity(cls, room_id):
        connection, cursor = connect_to_mysql()
        try:
            query = "SELECT capacity FROM room WHERE room_id = %s"
            cursor.execute(query, (room_id, ))
            result = cursor.fetchone()
            if result:
                return result[0]
            return None
        except Exception as e:
            connection.rollback()
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
    
    @classmethod
    def get_available_rooms(cls, check_in_date, check_out_date):
        connection, cursor = connect_to_mysql()
        try:
            query = """
            SELECT * FROM room 
            WHERE room_id NOT IN (
                SELECT room_id FROM booking 
                WHERE NOT (check_in <= %s OR check_out >= %s)
            )
            """
            cursor.execute(query, (check_out_date, check_in_date))
            results = cursor.fetchall()
            return [cls(*result) for result in results]
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def count_available_rooms(cls, check_in_date, check_out_date):
 
        connection, cursor = connect_to_mysql()
        try:
            query = """
            SELECT COUNT(*) FROM room 
            WHERE room_id NOT IN (
                SELECT room_id FROM booking 
                WHERE NOT (check_in <= %s OR check_out >= %s)
            )
            """
            cursor.execute(query, (check_out_date, check_in_date))
            return cursor.fetchone()[0]
        except Exception as e:
            print(f"Error: {e}")
            return 0
        finally:
            cursor.close()
            connection.close()
