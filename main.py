# importing from packages fromPyQt5
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

class MainWindow():
    window = QWidget()
    window.setWindowTitle("IP Subnet Calculator")
    win_width = 1500
    win_height = 900
    
    window.setGeometry(100, 100, win_width, win_height)

    # Window is hidden by default that is why we are shoeing it
    window.show()
    


# starting up the event loop
app.exec()
