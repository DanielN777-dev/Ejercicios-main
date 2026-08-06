from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


import json


app = QApplication([])

'''Notas in json'''
notes = {
    "!Bienvenido¡" : {
        "testo" : "!Esta es la mejor app para tpmar las notasdel mundo¡",
        "etiquetas" : ["Bien", "instrucciones"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file, ensure_ascii=False)    

''' interfas de la aplicasion '''
notes_win = QWidget()

notes_win.setWindowTitle('Notas inteligentes')
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_Label = QLabel('Lista de notas') 

button_note_create = QPushButton('Crear nota')
button_note_del = QPushButton('Eliminar nota')
button_note_save = QPushButton('Guardar nota')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('ingresar etiqueta')
field_text = QTextEdit()
button_add = QPushButton('Añadir a nota')
button_del = QPushButton('Eliminar de nota')
button_search = QPushButton('Buscar notas por etiqueta')
list_tags = QListWidget()
list_tags_label = QLabel('Etiquetas de la nota')

layout_note = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_Label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_note.addLayout(col_1, stretch=2)
layout_note.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_note)
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["testo"])
    list_tags.clear()
    list_tags.addItems(notes[key]["etiquetas"])

'''ajectar la aplicasión'''
list_notes.itemClicked.connect(show_note)
notes_win.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)
notes_win.show()
app.exec_()
