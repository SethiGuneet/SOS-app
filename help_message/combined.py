from PyQt5 import QtWidgets
from save_contacts import Ui_EmergencyApp


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    EmergencyApp = QtWidgets.QMainWindow()
    ui = Ui_EmergencyApp()
    ui.setupUi(EmergencyApp)
    EmergencyApp.show()
    sys.exit(app.exec_())

# THE DATABASE ISN'T LINKED WITH THE MAIN APP YET AND THE MESSAGE SERVICE IS JUST LINKED TO ONE MOBILE NUMBER ONLY