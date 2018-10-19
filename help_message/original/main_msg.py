from PyQt5 import QtCore, QtGui, QtWidgets
from twilio.rest import Client
import speech_recognition as sr
from save_contacts import Saviour
r = sr.Recognizer()
p = Saviour()


class Ui_EmergencyApp(Saviour):

    def setupUi(self, EmergencyApp):
        super().__init__()
        EmergencyApp.setObjectName("EmergencyApp")
        EmergencyApp.resize(534, 436)
        self.centralwidget = QtWidgets.QWidget(EmergencyApp)
        self.centralwidget.setObjectName("centralwidget")
        self.sos = QtWidgets.QTextEdit(self.centralwidget)
        self.sos.setGeometry(QtCore.QRect(190, 20, 181, 51))
        self.sos.setReadOnly(True)
        self.sos.setObjectName("sos")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(140, 260, 271, 51))
        self.textmsg = QtWidgets.QPushButton(self.centralwidget)
        self.textmsg.setGeometry(QtCore.QRect(140, 310, 271, 51))
        self.textmsg.clicked.connect(self.help_me2)
        self.contacts = QtWidgets.QPushButton(self.centralwidget)
        self.contacts.setGeometry(QtCore.QRect(140, 360, 271, 51))
        self.contacts.clicked.connect()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.help.setFont(font)
        self.contacts.setFont(font)
        self.textmsg.setFont(font)
        self.help.setObjectName("help")
        self.help.clicked.connect(self.help_me)
        self.inst = QtWidgets.QTextEdit(self.centralwidget)
        self.inst.setGeometry(QtCore.QRect(30, 120, 471, 111))
        self.inst.setReadOnly(True)
        self.inst.setObjectName("inst")
        EmergencyApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmergencyApp)
        QtCore.QMetaObject.connectSlotsByName(EmergencyApp)

    def retranslateUi(self, EmergencyApp):
        _translate = QtCore.QCoreApplication.translate

        EmergencyApp.setWindowTitle(_translate("EmergencyApp", "SOS APP"))
        self.sos.setHtml(_translate("EmergencyApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">SOS APP</span></p></body></html>"))
        self.help.setText(_translate("EmergencyApp", "VOICE MESSAGE"))
        self.inst.setHtml(_translate("EmergencyApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">In case of emergency</span><span style=\" font-size:10pt; font-weight:600;\">, you can click on the help button to get </span><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">SOS help</span><span style=\" font-size:10pt; font-weight:600;\"> from your close ones as well as</span><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\"> police helpline</span><span style=\" font-size:10pt; font-weight:600;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textmsg.setText(_translate("EmergencyApp", "TEXT MESSAGE"))
        self.contacts.setText(_translate("EmergencyApp", "SAVE CONTACTS"))

    def help_me(self):
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                self.text = r.recognize_google(audio)
                print("You said : {}".format(self.text))
            except:
                print("Sorry could not recognize your voice")

        self.account_sid = 'AC3429b5954be149d209fd8e7c0eae2c05'
        self.auth_token = 'd769ee90ff871fec43d7a3bde69dd1f3'
        self.myPhone = '+919810901053'
        self.TwilioNumber = '+18649773897'

        self.client = Client('AC3429b5954be149d209fd8e7c0eae2c05', 'd769ee90ff871fec43d7a3bde69dd1f3')

        self.client.messages.create(
            to='+919810901053',
            from_='+18649773897',
            body='{}'.format(self.text) + u'\U0001f685')

    def help_me2(self):
        self.account_sid = 'AC3429b5954be149d209fd8e7c0eae2c05'
        self.auth_token = 'd769ee90ff871fec43d7a3bde69dd1f3'
        self.myPhone = '+919810901053'
        self.TwilioNumber = '+18649773897'

        self.client = Client('AC3429b5954be149d209fd8e7c0eae2c05', 'd769ee90ff871fec43d7a3bde69dd1f3')

        self.client.messages.create(
            to='+919810901053',
            from_='+18649773897',
            body='How are you' + u'\U0001f685')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmergencyApp = QtWidgets.QMainWindow()
    ui = Ui_EmergencyApp()
    ui.setupUi(EmergencyApp)
    EmergencyApp.show()
    sys.exit(app.exec_())





