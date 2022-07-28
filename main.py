# importing from packages fromPyQt5
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

def MainWindow():
    window = QWidget()
    window.setWindowTitle("IP Subnet Calculator")



    # Window is hidden by default that is why we are shoeing it
    window.show()
MainWindow()

# starting up the event loop
app.exec()
