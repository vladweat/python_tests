from tkinter import *
from tkinter import messagebox

from cryptography.fernet import Fernet


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        super().__init__(master)

        self.initUI()

    def initUI(self):
        self.master.title("Data saver")
        self.pack(fill=BOTH, expand=1)

        self.create_widgets()
        self.resize()

    def create_widgets(self):
        self.label_font = "Courier 14"
        self.label_font_1 = "Courier 12"

        self.welc_label = Label(self,
                                text="Login Saver",
                                font=self.label_font)
        self.welc_label.pack(fill=X, ipady=5)

        self.frame0 = Frame(self)
        self.frame0.pack(fill=X)

        self.name_lbl = Label(self.frame0,
                              text="Name",
                              font=self.label_font,
                              width=10)
        self.name_lbl.pack(side=LEFT, padx=5, pady=1)

        self.name_ent = Entry(self.frame0,
                              font=self.label_font_1,
                              width=35)
        self.name_ent.pack(padx=5, ipady=1, expand=True)

        self.frame1 = Frame(self)
        self.frame1.pack(fill=X)

        self.mail_lbl = Label(self.frame1,
                              text="Mail",
                              font=self.label_font,
                              width=10)
        self.mail_lbl.pack(side=LEFT, padx=5, pady=1)

        self.mail_ent = Entry(self.frame1,
                              font=self.label_font_1,
                              width=35)
        self.mail_ent.pack(padx=5, ipady=1, expand=True)

        self.frame2 = Frame(self)
        self.frame2.pack(fill=X)

        self.pass_lbl = Label(self.frame2,
                              text="Password",
                              font=self.label_font,
                              width=10)
        self.pass_lbl.pack(side=LEFT, padx=5, pady=1)

        self.pass_ent = Entry(self.frame2, width=35)
        self.pass_ent["font"] = self.label_font_1
        self.pass_ent.pack(padx=5, ipady=1, expand=True)

        self.frame3 = Frame(self)
        self.frame3.pack(fill=X)

        self.add_button = Button(self.frame3,
                                 text="Add data",
                                 width=10,
                                 height=2,
                                 font=self.label_font_1,
                                 command=self.crypt_data)
        self.add_button.grid(row=1, column=1, pady=10, padx=30)

        self.clear_button = Button(self.frame3,
                                   text="Clear",
                                   width=10,
                                   height=2,
                                   font=self.label_font_1,
                                   command=self.clear_entry)
        self.clear_button.grid(row=1, column=2, pady=10, padx=25)

        self.dop_button = Button(self.frame3,
                                 text="Dop btn",
                                 width=10,
                                 height=2,
                                 font=self.label_font_1,
                                 command=self.resize)
        self.dop_button.grid(row=1, column=3, pady=10, padx=30)

        self.frame4 = Frame(self)
        self.frame4.pack(fill=BOTH, pady=5)

        self.text_box = Text(self.frame4, width=48)

        self.text_box["font"] = self.label_font_1
        self.text_box["state"] = "normal"
        self.text_box["background"] = "#F0F0F0"

        name = '{:<12}'.format('Name')
        mail = '{:<24}'.format('Mail')
        password = '{:<10}'.format('Password \n')
        str = name + mail + password

        self.text_box.insert(INSERT, str)

        self.text_box["state"] = "disabled"

        self.decrypt_data()

        self.text_box.pack(fill=Y)

    def clear_entry(self):
        self.name_ent.delete(0, END)
        self.mail_ent.delete(0, END)
        self.pass_ent.delete(0, END)
        self.resize()

    def crypt_data(self):
        self.cip_name = str(self.name_ent.get()).encode('utf-8')
        self.cip_mail = str(self.mail_ent.get()).encode('utf-8')
        self.cip_password = str(self.pass_ent.get()).encode('utf-8')

        self.name = str(self.name_ent.get())

        self.cipher_key = Fernet.generate_key()
        self.cipher = Fernet(self.cipher_key)

        self.crypt_name = self.cipher.encrypt(self.cip_name)
        self.crypt_mail = self.cipher.encrypt(self.cip_mail)
        self.crypt_pass = self.cipher.encrypt(self.cip_password)

        self.add_data_in_file()

    def add_data_in_file(self):
        f = open('C:\\Users\\vladw\\PycharmProjects\\python_tests\\pass_log_saver\\name_mail_pass', 'a')

        f.write(self.crypt_name.decode('utf-8') + ' ' +
                self.crypt_mail.decode('utf-8') + ' ' +
                self.crypt_pass.decode('utf-8') + ' ' +
                self.cipher_key.decode('utf-8') + '\n')
        f.close()

        self.text_box["state"] = "normal"

        name = '{:<12}'.format(self.name_ent.get())
        mail = '{:<24}'.format(self.mail_ent.get())
        password = '{:<10}'.format(self.pass_ent.get())

        str = name + mail + password + "\n"

        self.text_box.insert(INSERT, str)
        self.text_box["state"] = "disabled"

        messagebox.showinfo("Successful", "Data added in file successfully!")
        self.resize()

    def decrypt_data(self):
        f = open('C:\\Users\\vladw\\PycharmProjects\\python_tests\\pass_log_saver\\name_mail_pass', 'r')

        for line in f:
            self.decrypted_text = line.split(' ')
            self.enc_name = self.decrypted_text[0].encode('utf-8')
            self.enc_mail = self.decrypted_text[1].encode('utf-8')
            self.enc_pass = self.decrypted_text[2].encode('utf-8')
            self.enc_cipher_key = self.decrypted_text[3].encode('utf-8')

            self.dec_cipehr = Fernet(self.enc_cipher_key)

            self.dec_name = self.dec_cipehr.decrypt(self.enc_name)
            self.dec_mail = self.dec_cipehr.decrypt(self.enc_mail)
            self.dec_pass = self.dec_cipehr.decrypt(self.enc_pass)

            name = '{:<12}'.format(self.dec_name.decode('utf-8'))
            mail = '{:<24}'.format(self.dec_mail.decode('utf-8'))
            password = '{:<10}'.format(self.dec_pass.decode('utf-8'))

            self.text_box["state"] = "normal"

            str = name + mail + password + "\n"

            self.text_box.insert(INSERT, str)
            self.text_box["state"] = "disabled"

    def resize(self):
        f = open('C:\\Users\\vladw\\PycharmProjects\\python_tests\\pass_log_saver\\name_mail_pass', 'r')

        self.height_num = 0

        for line in f:
            self.height_num += 1

        self.height = 300 + self.height_num * 15

        if self.height < 600:
            self.master.geometry(f"500x{self.height}")
        else:
            self.master.geometry("500x600")


def create_app():
    root = Tk()
    root.geometry("500x500")
    root.resizable(False, True)
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    create_app()
