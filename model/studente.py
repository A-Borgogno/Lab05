class Studente:
    def __init__(self, matricola, cognome, nome, CDS):
        self.matricola = matricola
        self.cognome = cognome
        self.nome = nome
        self.CorsoDiStudi = CDS

    def __str__(self):
        return f"{self.nome.upper()} {self.cognome.upper()} ({self.matricola})"

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getMatricola(self):
        return self.matricola

    def getCorsoDiStudi(self):
        return self.CorsoDiStudi