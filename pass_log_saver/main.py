from cryptography.fernet import Fernet


# basic crypt class
class Crypt:

    def __init__(self):
        self.cipher_first_key = bytes  # first cipher key
        # self.cipher_second_key = 0  # second cipher key

        self.once_enc_mail = bytes
        self.once_enc_pass = bytes

    # Func convert entered mail and pass into bytes
    # input -> split/convert to bytes -> gen key -> cipher
    def crypt(self):
        print("Введите почту и пароль:")
        mail_pass = str(input()).split(" ")

        # encoding mail/pass into bytes
        mail = str(mail_pass[0]).encode('utf-8')
        password = str(mail_pass[1]).encode('utf-8')

        # first cipher
        # use cipher_key to cipher mail/pass
        # type mail/pass - bytes
        self.cipher_first_key = Fernet.generate_key()  # first cipher key
        self.cipher_first = Fernet(self.cipher_first_key)  # first cipher
        self.once_enc_mail = self.cipher_first.encrypt(mail)
        self.once_enc_pass = self.cipher_first.encrypt(password)

        print('\n-- Successful crypt --')

        # # second cipher
        # self.cipher_second_key = Fernet.generate_key()          # second cipher key
        # self.cipher_second = Fernet(self.cipher_second_key)     # second cipher
        # self.twice_enc_mail = self.cipher_second.encrypt(once_enc_mail)
        # self.twice_enc_pass = self.cipher_second.encrypt(once_enc_pass)

    # Func add mail, pass, cipher_key into txt file
    # data convert from bytes to str -> writes in file
    def addCryptInFile(self):
        f = open('C:\\Users\\vladw\PycharmProjects\python_tests\pass_log_saver\pass_logs', 'a')  # w <--> a

        f.write(
            self.once_enc_mail.decode('utf-8') + ' ' + self.once_enc_pass.decode(
                'utf-8') + ' ' + self.cipher_first_key.decode('utf-8') + '\n'
        )
        f.close()
        print('-- Successful adding --\n')

    # Func printed all data in txt file (can be taken out from class)
    # read file -> convert to bytes -> decrypt -> convert to str
    def selectCryptInFile(self):
        f = open('C:\\Users\\vladw\PycharmProjects\python_tests\pass_log_saver\pass_logs', 'r')

        for line in f:
            # split and print data 1 line in file
            decrypted_text = line.split(' ')
            enc_mail = decrypted_text[0].encode('utf-8')
            enc_pass = decrypted_text[1].encode('utf-8')
            cipher_first_key = decrypted_text[2].encode('utf-8')

            # create decrypter cipher
            dec_cipher = Fernet(cipher_first_key)

            # decrypt data
            dec_mail = dec_cipher.decrypt(enc_mail).decode('utf-8')
            dec_pass = dec_cipher.decrypt(enc_pass).decode('utf-8')

            print(dec_mail, dec_pass)

# print("Сколько данных хотите внести?")
# num = int(input())
#
# for i in range(num):
#     user = Crypt()
#     user.crypt()
#     user.addCryptInFile()

showAll = Crypt()
showAll.selectCryptInFile()


