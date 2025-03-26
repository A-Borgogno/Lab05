from database.corso_DAO import corso_DAO
from database.studente_DAO import studente_DAO


class Model:
    def __init__(self):
        self._DAOCorsi = corso_DAO()
        self._DAOStudenti = studente_DAO()

    def setDd(self):
        return self._DAOCorsi.getCorsi()

    def getIscrittiCorso(self, cod):
        return self._DAOStudenti.getStudentiCorso(cod)

    def getStudente(self, matricola):
        return self._DAOStudenti.getStudente(matricola)

    def getCorsiStudente(self, studente):
        return self._DAOCorsi.getCorsiStudente(studente.getMatricola())