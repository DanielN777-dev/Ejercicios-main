from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
 
app = QApplication([])
 
# ventana principal:
my_win = QWidget()
my_win.setWindowTitle('Identificador del ganador')
my_win.move(100, 100)
my_win.resize(400, 200)


#widgets de la ventana: botón y etiqueta
button = QPushButton('Generar')
text = QLabel('Haz click para conocer al ganador')
winner = QLabel('?')


#layout de los widgets
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)


#función que genera y muestra un número
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Ganador:')
 
#procesamiento del click del botón
button.clicked.connect(show_winner)


my_win.show()
app.exec_()
