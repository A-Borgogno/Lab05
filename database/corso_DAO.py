# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


class corso_DAO:
    def __init__(self):
        pass

    def getCorsi(self):
        corsi = []
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM corso")
        for row in cursor.fetchall():
            c = Corso(row[0], row[1], row[2], row[3])
            corsi.append(c)
        conn.close()
        return corsi

    def getCorsiStudente(self, matricola):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT c.codins, c.nome FROM iscrizione i, corso c WHERE i.codins = c.codins AND i.matricola = %s", (matricola,))
        corsi = []
        for row in cursor.fetchall():
            corsi.append(f"{row[1]} ({row[0]})")
        conn.close()
        return corsi