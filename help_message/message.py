from PyQt5 import QtCore, QtGui, QtWidgets
from twilio.rest import Client
import speech_recognition as sr

class Ui_EmergencyApp(object):

    def setupUi(self, EmergencyApp):
        EmergencyApp.setObjectName("EmergencyApp")
        EmergencyApp.resize(534, 436)
        self.centralwidget = QtWidgets.QWidget(EmergencyApp)
        self.centralwidget.setObjectName("centralwidget")
        self.sos = QtWidgets.QTextEdit(self.centralwidget)
        self.sos.setGeometry(QtCore.QRect(190, 20, 181, 51))
        self.sos.setReadOnly(True)
        self.sos.setObjectName("sos")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(140, 290, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.help.setFont(font)
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
        self.help.setText(_translate("EmergencyApp", "HELP"))
        self.inst.setHtml(_translate("EmergencyApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">In case of emergency</span><span style=\" font-size:10pt; font-weight:600;\">, you can click on the help button to get </span><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">SOS help</span><span style=\" font-size:10pt; font-weight:600;\"> from your close ones as well as</span><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\"> police helpline</span><span style=\" font-size:10pt; font-weight:600;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

    def help_me(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print("Sorry could not recognize your voice")

        self.account_sid = 'ACb40c642c131701f34eb51e96eef82224'
        self.auth_token = 'e67f5f56f57bad00f0c989df587e8712'
        self.myPhone = '+918860707633'
        self.TwilioNumber = '+14159039903'

        self.client = Client('ACb40c642c131701f34eb51e96eef82224', 'e67f5f56f57bad00f0c989df587e8712')
        #text= text
        self.client.messages.create(
            to='+918860707633',
            from_='+14159039903',
            body= "{}".format(text) + u'\U0001f685')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmergencyApp = QtWidgets.QMainWindow()
    ui = Ui_EmergencyApp()
    ui.setupUi(EmergencyApp)
    EmergencyApp.show()
    sys.exit(app.exec_())
