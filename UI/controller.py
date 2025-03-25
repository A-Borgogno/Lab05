import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def setDd(self):
        corsi = self._model.setDd()
        for c in corsi:
            self._view._dd.options.append(ft.dropdown.Option(f"{c.getNome()} ({c.getCodice()})"))
        self._view.update()

    def handleIscritti(self, e):
        iscritti = self._model.getIscrittiCorso(self._view._dd.value[-8:-1:1])
        self._view._lv.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti:"))
        for i in iscritti:
            self._view._lv.controls.append(ft.Text(f"{self._model.Studente(i)}"))
        self._view.update()

    def handleCercaCorsi(self, e):
        pass

    def handleCercaStudente(self, e):
        pass

    def handleIscrivi(self, e):
        pass