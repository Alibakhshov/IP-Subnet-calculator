from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import ipaddress

class IPSubnetCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('IP Subnet Calculator')
        self.setGeometry(100, 100, 400, 300)

        self.ip_label = QLabel('Enter IP Address:', self)
        self.ip_input = QLineEdit(self)
        self.ip_input.setPlaceholderText('e.g., 192.168.1.1')

        self.subnet_label = QLabel('Enter Subnet Mask:', self)
        self.subnet_input = QLineEdit(self)
        self.subnet_input.setPlaceholderText('e.g., 255.255.255.0')

        self.result_label = QLabel('Subnet Information:', self)
        self.result_display = QLabel(self)

        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.clicked.connect(self.calculate_subnet)

        layout = QVBoxLayout(self)
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)
        layout.addWidget(self.subnet_label)
        layout.addWidget(self.subnet_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)

    def calculate_subnet(self):
        ip_address = self.ip_input.text()
        subnet_mask = self.subnet_input.text()

        try:
            network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
            network_address = network.network_address
            broadcast_address = network.broadcast_address
            num_hosts = network.num_addresses - 2  # Subtracting network and broadcast addresses
            ip_class = network.network_address._version

            if ip_class == 4:
                ip_class_type = "IPv4"
            elif ip_class == 6:
                ip_class_type = "IPv6"
            else:
                ip_class_type = "Unknown"

            result_text = f"Network Address: {network_address}\n" \
                          f"Broadcast Address: {broadcast_address}\n" \
                          f"Number of Hosts: {num_hosts}\n" \
                          f"IP Class: {ip_class_type}"

            self.result_display.setText(result_text)

        except ipaddress.AddressValueError:
            self.result_display.setText("Invalid IP Address or Subnet Mask")


if __name__ == '__main__':
    app = QApplication([])
    window = IPSubnetCalculator()
    window.show()
    app.exec()
