# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class studente_DAO:
    def __init__(self):
        pass

    def getStudentiCorso(self, cod):
        matricole = []
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iscrizione WHERE codins = %s", (cod,))
        for row in cursor.fetchall():
            matricole.append(row[0])
        conn.close()
        return matricole

    def getStudente(self, matricola):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM studente WHERE matricola = %s", (matricola,))
        for row in cursor.fetchall():
            s = Studente(row[0], row[1], row[2], row[3])
        conn.close()
        return s