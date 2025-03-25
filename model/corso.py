class Corso:
    def __init__(self, codice, crediti, nome, pd):
        self.codice = codice
        self.crediti = crediti
        self.nome = nome
        self.periodoDidattico = pd

    def getNome(self):
        return self.nome

    def getCodice(self):
        return self.codice