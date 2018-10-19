from PyQt5 import QtWidgets
from main_msg import Ui_EmergencyApp


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    EmergencyApp = QtWidgets.QMainWindow()
    ui = Ui_EmergencyApp()
    ui.setupUi(EmergencyApp)
    EmergencyApp.show()
    sys.exit(app.exec_())
