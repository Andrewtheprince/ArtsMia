from database.DB_connect import DBConnect
from model.arco import Arco
from model.artObject import ArtObject


class DAO:

    @staticmethod
    def getAllNodes():
        conn= DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query= """SELECT * FROM objects o"""
        cursor.execute(query)
        for row in cursor:
            result.append(ArtObject(**row))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllArchi(idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT eo.object_id as o1, eo2.object_id as o2, count(*) as peso
                   FROM exhibition_objects eo, exhibition_objects eo2
                   WHERE eo.exhibition_id = eo2.exhibition_id
                   and eo.object_id < eo2.object_id
                   GROUP BY eo.object_id, eo2.object_id
                   order by peso desc"""
        cursor.execute(query)
        for row in cursor:
            result.append(Arco(idMap[row["o1"]], idMap[row["o2"]], row["peso"]))
        cursor.close()
        conn.close()
        return result