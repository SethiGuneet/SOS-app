from tkinter import *
import backend


class Saviour(object):

    def __init__(self):
        window.mainloop()

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



