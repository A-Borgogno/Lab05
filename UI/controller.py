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
            self._view._dd.options.append(ft.dropdown.Option(key=c.getCodice(), text=f"{c.getNome()} ({c.getCodice()})"))
        self._view.update()

    def handleIscritti(self, e):
        self._view._lv.controls.clear()
        if self._view._dd.value is None:
            self._view.create_alert("Selezionare un corso!")
            return
        iscritti = self._model.getIscrittiCorso(self._view._dd.value)
        self._view._lv.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti:", italic=True, size=20, weight=ft.FontWeight.BOLD))
        for i in iscritti:
            self._view._lv.controls.append(ft.Text(i))
        self._view.update()

    def handleCercaStudente(self, e):
        if self._view._txtMatricola.value == "":
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.getStudente(self._view._txtMatricola.value)
        if studente is None:
            self._view._lv.controls.clear()
            self._view._lv.controls.append(ft.Text("Matricola non presente!", size=20, color='red'))
            self._view.update()
            return
        self._view._txtNome.value = studente.getNome()
        self._view._txtCognome.value = studente.getCognome()
        self._view.update()

    def handleCercaCorsi(self, e):
        self._view._lv.controls.clear()
        self.handleCercaStudente(e)
        if len(self._view._lv.controls) == 1:
            return
        studente = self._model.getStudente(self._view._txtMatricola.value)
        corsi = self._model.getCorsiStudente(studente)
        self._view._lv.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:", italic=True, weight=ft.FontWeight.BOLD))
        for c in corsi:
            self._view._lv.controls.append(ft.Text(c))
        self._view.update()

    def handleIscrivi(self, e):
        pass