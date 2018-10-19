from tkinter import *
import backend
from PyQt5 import QtCore, QtGui, QtWidgets
from twilio.rest import Client
import speech_recognition as sr
import geocoder
r = sr.Recognizer()


class Saviour(object):

    def get_selected_row(self):
        global selected_tuple
        index = self.list1.curselection()[0]
        selected_tuple = self.list1.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, selected_tuple[2])

    def view_command(self):
        self.list1.delete(0, END)
        for row in backend.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in backend.search(self.contact_name.get(), self.contact_number.get()):
            self.list1.insert(END, row)

    def add_command(self):
        backend.insert(self.contact_name.get(), self.contact_number.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.contact_name.get(), self.contact_number.get()))

    def delete_command(self):
        backend.delete(selected_tuple[0])

    def update_command(self):
        backend.update(selected_tuple[0], self.contact_name.get(), self.contact_number.get())


window = Tk()
p = Saviour()
window.wm_title("Contacts")

p.l1 = Label(window, text="Contact Name")
p.l1.grid(row=0, column=0)

p.l2 = Label(window, text="Contact Number")
p.l2.grid(row=0, column=2)

p.contact_name = StringVar()
p.e1 = Entry(window, textvariable=p.contact_name)
p.e1.grid(row=0, column=1)

p.contact_number = StringVar()
p.e2 = Entry(window, textvariable=p.contact_number)
p.e2.grid(row=0, column=3)

p.list1 = Listbox(window, height=8, width=35)
p.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

p.sb1 = Scrollbar(window)
p.sb1.grid(row=2, column=2, rowspan=6)

p.list1.configure(yscrollcommand=p.sb1.set)
p.sb1.configure(command=p.list1.yview)

p.list1.bind('<<ListboxSelect>>', p.get_selected_row)

p.b1 = Button(window, text="View all", width=12, command=p.view_command)
p.b1.grid(row=2, column=3)

p.b2 = Button(window, text="Search entry", width=12, command=p.search_command)
p.b2.grid(row=3, column=3)

p.b3 = Button(window, text="Add entry", width=12, command=p.add_command)
p.b3.grid(row=4, column=3)

p.b4 = Button(window, text="Update selected", width=12, command=p.update_command)
p.b4.grid(row=5, column=3)

p.b5 = Button(window, text="Delete selected", width=12, command=p.delete_command)
p.b5.grid(row=6, column=3)

p.b6 = Button(window, text="Ok", width=12, command=window.destroy)
p.b6.grid(row=7, column=3)



class Ui_EmergencyApp(Saviour):

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
        self.help.setGeometry(QtCore.QRect(140, 260, 271, 51))
        self.textmsg = QtWidgets.QPushButton(self.centralwidget)
        self.textmsg.setGeometry(QtCore.QRect(140, 310, 271, 51))
        self.textmsg.clicked.connect(self.help_me2)
        self.contacts = QtWidgets.QPushButton(self.centralwidget)
        self.contacts.setGeometry(QtCore.QRect(140, 360, 271, 51))
        self.contacts.clicked.connect(self.call)
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

    window = Tk()

    def call(self):
        self.window.mainloop()

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

        # self.account_sid = 'YOUR ACCOUNT ID'
        # self.auth_token = 'YOUR SELF AUTHORISATION TOKEN'
        # self.myPhone = 'YOUR TARGET MOBILE NO.'
        # self.TwilioNumber = 'NO. GENERATED BY TWILIO'

        # client = Client('YOUR ACCOUNT ID', 'YOUR SELF AUTHORISATION TOKEN')

         # client.messages.create(
         #    to='TARGET NO.',
         #    from_='NO. GENERATED BY TWILIO',
         #    body='{}'.format(self.text) + u'\U0001f680')

    def help_me2(self):
        # self.account_sid = 'YOUR ACCOUNT ID'
        # self.auth_token = 'YOUR SELF AUTHORISATION TOKEN'
        # self.myPhone = 'YOUR TARGET MOBILE NO.'
        # self.TwilioNumber = 'NO. GENERATED BY TWILIO'

        # client = Client('YOUR ACCOUNT ID', 'YOUR AUTHORISATION TOKEN')

        self.g = geocoder.ip('me')
        self.x = self.g.lat
        self.y = self.g.lng

        # client.messages.create(
            # to='THE NO. ON WHICH MESSAGE IS TO BE SENT',
            # from_='NO. GENERATED BY TWILIO',
            # body='Help me bro'
            #     'MY LOCATION IS =https://www.google.co.in/maps/@{},{},15z'.format(self.x, self.y) + u'\U0001f680')


        # https://www.latlong.net/c/?lat=self.x&long=self.y



