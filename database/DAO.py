from database.DB_connect import DBConnect
from model.artObject import ArtObject


class DAO:

    @staticmethod
    def getAllNodes():
        conn= DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query= """SELECT * FROM object o"""
        cursor.execute(query)
        for row in cursor:
            result.append(ArtObject(**row))
        cursor.close()
        conn.close()
        return result
