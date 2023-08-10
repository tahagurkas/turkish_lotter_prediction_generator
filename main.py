from PyQt5.QtWidgets import QApplication
from sayısal import lotoPage

app = QApplication([])

pencere = lotoPage()
pencere.show()

app.exec_()