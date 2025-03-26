import flet as ft
from flet_core import MainAxisAlignment, page


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._lv = None
        self._btnIscrivi = None
        self._btnCorsi = None
        self._btnStudente = None
        self._txtCognome = None
        self._txtNome = None
        self._txtMatricola = None
        self._btnIscritti = None
        self._dd = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("Gestione studenti e corsi", color="blue", size=24)
        self._page.controls.append(self._title)

        self._dd = ft.Dropdown(label="Corso", width=800)
        self._controller.setDd()
        self._btnIscritti = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handleIscritti, tooltip="Cerca gli studenti iscritti al corso selezionato")
        row1 = ft.Row([self._dd, self._btnIscritti], alignment=MainAxisAlignment.CENTER)

        self._txtMatricola = ft.TextField(label="Matricola")
        self._txtNome = ft.TextField(label="Nome")
        self._txtCognome = ft.TextField(label="Cognome")
        row2 = ft.Row([self._txtMatricola, self._txtNome, self._txtCognome], alignment=MainAxisAlignment.CENTER)

        self._btnStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handleCercaStudente, tooltip="Verifica se c'è uno studente con la matricola inserita")
        self._btnCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handleCercaCorsi)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handleIscrivi)
        row3 = ft.Row([self._btnStudente, self._btnCorsi, self._btnIscrivi], alignment=MainAxisAlignment.CENTER)
        
        self._lv = ft.ListView(expand=True, auto_scroll=True)
        self._page.add(row1, row2, row3, self._lv)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update(self):
        self._page.update()
