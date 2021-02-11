from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import string
import webbrowser
import pymysql

main = QApplication([])

'''
WARNA RINDANG.IN    = color : #079e4f rgb(7, 158, 79)
FONT KONTEN         = Comic Sans MS
FONT DESKRIPSI      = sans serif
'''

################################################## Enkrip Dekrip #######################################################

class caesar():
    def __init__(self):
        super(caesar, self).__init__()

    def enkripsi(self,pesan):
        global abjad
        abjad = string.ascii_letters+string.digits
        self.pesan = pesan
        self.key = len(self.pesan)
        self.cipher = ''
        for i in self.pesan:
            if i in abjad:
                self.k = abjad.find(i)
                self.k = (self.k+self.key)%62
                self.cipher += abjad[self.k]
            else:
                self.cipher += i
        return self.cipher

    def dekripsi(self,cipher):
        global abjad
        abjad = string.ascii_letters+string.digits
        self.cipher = cipher
        self.key = len(self.cipher)
        self.pesan = ''
        for i in self.cipher:
            if i in abjad:
                self.k = abjad.find(i)
                self.k = (self.k-self.key)%62
                self.pesan += abjad[self.k]
            else:
                self.pesan += i
        return self.pesan

################################################### StyleSheet #########################################################

class style():
    def __init__(self):
        self.btn = """QPushButton:hover{background-color:rgb(172, 255, 127, 50%);}
                            QPushButton:pressed{background-color:rgb(172, 255, 127);}
                            QPushButton{font-weight:500;
                                    font-size: 16px;
                                    background-color: white;
                                    border-radius:20px;
                                    border-style: solid;
                                    border-width:3px;
                                    border-color:green;}"""


        self.btn_login = """QPushButton:hover{border-color:green;}
                            QPushButton:pressed{background-color:green;}
                            QPushButton{color: white;
                                    font-weight:500;
                                    font-size:16px;
                                    background-color: #079e4f;
                                    border-radius:15px;
                                    border-style: solid;
                                    border-width:2px;}"""


        self.le_login = """QLineEdit{border-width:2px;
                                    font-size:16px;
                                    border-style: solid;
                                    border-bottom-color:rgb(109, 109, 109, 25%);
                                    border-top-color: white;
                                    border-left-color: white;
                                    border-right-color: white;}
                            QLineEdit:focus{border-bottom-color:#079e4f;
                                            background-color: rgb(172, 255, 127, 10%);
                                            border-radius: 5px}"""


        self.sa_konten = """QScrollArea{border-width:2px;
                                    border-style: solid;
                                    border-top-color: white;
                                    border-left-color: white;
                                    border-bottom-color: white;
                                    border-right-color: white;}"""

        self.sb_konten = """QScrollBar:vertical{border: 1px solid rgb(172, 255, 127, 50%);
                                                width:10px;
                                                background:white;
                                                margin: 0px 0px 0px 0px;}
                            QScrollBar::handle:vertical{background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0 rgb(7, 158, 79,50%), stop: 0.5 rgb(7, 158, 79,50%), stop:1 rgb(7, 158, 79,50%));
                                                        min-height: 0px;}
                            QScrollBar::add-line:vertical{background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0 rgb(7, 158, 79,50%), stop: 0.5 rgb(7, 158, 79,50%),  stop:1 rgb(7, 158, 79,50%));
                                                            height: 0px;
                                                            subcontrol-position: bottom;
                                                            subcontrol-origin: margin;}
                            QScrollBar::sub-line:vertical{background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop: 0  rgb(7, 158, 79,50%), stop: 0.5 rgb(7, 158, 79,50%),  stop:1 rgb(7, 158, 79,50%));
                                                            height: 0 px;
                                                            subcontrol-position: top;
                                                            subcontrol-origin: margin;}"""

        self.btn_kontak = """QPushButton:hover{background-color:rgb(172, 255, 127, 50%)}
                            QPushButton:pressed{background-color:rgb(7, 158, 79, 25%)}
                            QPushButton{qproperty-icon: url(logo/pesan.png);
                                        background-color:rgb(163, 163, 163, 0%);
                                        border-radius:5px;
                                        border-style: solid;
                                        border-width:2px;}"""

        self.btn_alamat = """QPushButton:hover{background-color:rgb(255, 116, 116,50%);}
                            QPushButton:pressed{background-color:rgb(255, 116, 116);}
                            QPushButton{border-image: url(logo/maps.png);
                                        background-repeat: no-repeat;
                                        background-color:rgb(163, 163, 163, 0%);
                                        border-radius:5px;
                                        width: 50px;
                                        height: 50px;}"""

        self.lbl_user = """QLabel{border-image: url(logo/username.png);
                                        background-repeat: no-repeat;
                                        background-color:match parent;
                                        border-radius:5px;
                                        width: 30px;
                                        height: 30px;}"""

        self.lbl_pass = """QLabel{border-image: url(logo/password.png);
                                        background-repeat: no-repeat;
                                        background-color:match parent;
                                        border-radius:5px;
                                        width: 30px;
                                        height: 30px;}"""

        self.lbl_nama = """QLabel{border-image: url(logo/nama.png);
                                        background-repeat: no-repeat;
                                        background-color:match parent;
                                        border-radius:5px;
                                        width: 30px;
                                        height: 30px;}"""

        self.btn_thias = """QPushButton:hover{background-color:rgb(172, 255, 127, 50%);}
                            QPushButton:pressed{background-color:rgb(172, 255, 127);}
                            QPushButton{qproperty-icon: url(logo/thias.png);
                                    qproperty-iconSize: 100px 100px;
                                    font-size:20px;
                                    font-weight:500;
                                    background-color: white;
                                    border-radius:75px;
                                    border-style: solid;
                                    border-width:3px;
                                    border-color:green;}"""

        self.btn_tobat = """QPushButton:hover{background-color:rgb(172, 255, 127, 50%);}
                            QPushButton:pressed{background-color:rgb(172, 255, 127);}
                            QPushButton{qproperty-icon: url(logo/tobat.png);
                                    qproperty-iconSize: 100px 100px;
                                    font-size:20px;
                                    font-weight:500;
                                    background-color: white;
                                    border-radius:75px;
                                    border-style: solid;
                                    border-width:3px;
                                    border-color:green;}"""

        self.btn_alat = """QPushButton:hover{background-color:rgb(172, 255, 127, 50%);}
                            QPushButton:pressed{background-color:rgb(172, 255, 127);}
                            QPushButton{qproperty-icon: url(logo/alat.png);
                                    qproperty-iconSize: 100px 100px;
                                    font-size:20px;
                                    font-weight:500;
                                    background-color: white;
                                    border-radius:75px;
                                    border-style: solid;
                                    border-width:3px;
                                    border-color:green;}"""

        self.btn_pubit = """QPushButton:hover{background-color:rgb(172, 255, 127, 50%);}
                            QPushButton:pressed{background-color:rgb(172, 255, 127);}
                            QPushButton{qproperty-icon: url(logo/pubit.png);
                                    qproperty-iconSize: 100px 100px;
                                    font-size:20px;
                                    font-weight:500;
                                    background-color: white;
                                    border-radius:75px;
                                    border-style: solid;
                                    border-width:3px;
                                    border-color:green;}"""

################################################## WINDOW LOGIN ########################################################

class tlogin(QMainWindow):
    def __init__(self):
        super(tlogin, self).__init__()
        self.setWindowIcon(QIcon("logo/logo.png"))
        self.setWindowTitle('Rindang.In')
        self.setFixedSize(500, 400)
        self.setGeometry(0, 0, 500,400) #x,y,width,height
        self.setStyleSheet("background-color:white;")

        self.welcome = QLabel(self)
        self.welcome.setText('LOGIN')
        self.welcome.setStyleSheet("color : #079e4f;;font-weight:700;")
        self.welcome.setFont(QFont('Terminus', 20))
        self.welcome.adjustSize()
        self.welcome.setGeometry(195,10,300,40)

        self.userLabel = QLabel(self)
        self.userLabel.setStyleSheet(style().lbl_user)
        self.userLabel.setGeometry(60,100,30,30)

        self.userInput = QLineEdit(self)
        self.userInput.setGeometry(100,100,300,30)
        self.userInput.setPlaceholderText("Masukkan Username")

        self.passLabel = QLabel(self)
        self.passLabel.setStyleSheet(style().lbl_pass)
        self.passLabel.setGeometry(60,150,30,30)

        self.passInput = QLineEdit(self)
        self.passInput.setGeometry(100,150,300,30)
        self.passInput.setEchoMode(QLineEdit.Password)
        self.passInput.setPlaceholderText("Masukkan Password")

        self.penjualButton = QPushButton(self)
        self.penjualButton.setText("Login Sebagai Member")
        self.penjualButton.setGeometry(100,200,300,30)
        self.penjualButton.clicked.connect(lambda: self.btn_fungsi('penjual'))

        self.pembeliButton = QPushButton(self)
        self.pembeliButton.setText("Login Sebagai Tamu")
        self.pembeliButton.setGeometry(100,250,300,30)
        self.pembeliButton.clicked.connect(lambda: self.btn_fungsi('pembeli'))

        self.daftarButton = QPushButton(self)
        self.daftarButton.setText("Daftar Sebagai Member")
        self.daftarButton.setGeometry(100,300,300,30)
        self.daftarButton.clicked.connect(self.btn_daftar)

        ################################################### STYLESHEET #################################################
        self.passInput.setStyleSheet(style().le_login)
        self.userInput.setStyleSheet(style().le_login)
        self.penjualButton.setStyleSheet(style().btn_login)
        self.pembeliButton.setStyleSheet(style().btn_login)
        self.daftarButton.setStyleSheet(style().btn_login)
        ################################################################################################################

    def btn_fungsi(self, sebagai):
        self.sebagai = sebagai
        if self.sebagai == 'penjual':
            li = [self.userInput.text(), self.passInput.text()]
            mydb = pymysql.connect(
            host="localhost",
            user = "root",
            passwd = "",
            database = "RindangIn"
            )
            myqursor = mydb.cursor()
            myqursor.execute(f"select password from anggota where username = '{li[0]}' ")
            data = myqursor.fetchone()
            if data == None:
                self.userInput.setText('')
                self.passInput.setText('')
                QMessageBox.warning(self,"Failed", "Username atau Password yang Anda Masukkan Salah")
            else:
                passwd = caesar.dekripsi(caesar,data[0])
                if li[1] == passwd:
                    self.userInput.setText('')
                    self.passInput.setText('')
                    self.hide()
                    wutama.win.insert.show()
                    wutama.win.show()
                else:
                    self.userInput.setText('')
                    self.passInput.setText('')
                    QMessageBox.warning(self,"Failed", "Username atau Password yang Anda Masukkan Salah")
        elif self.sebagai == 'pembeli':
            self.userInput.setText('')
            self.passInput.setText('')
            self.hide()
            wutama.win.insert.hide()
            wutama.win.show()
    def btn_daftar(self):
        self.userInput.setText('')
        self.passInput.setText('')
        self.hide()
        wdaftar.win.show()

################################################## WINDOW DAFTAR #######################################################

class tdaftar(QMainWindow):
    def __init__(self):
        super(tdaftar, self).__init__()
        self.setWindowIcon(QIcon("logo/logo.png"))
        self.setWindowTitle('Rindang.In/Daftar Member')
        self.setFixedSize(500, 400)
        self.setGeometry(0, 0, 500,400) #x,y,width,height
        self.setStyleSheet("background-color:white;")

        self.welcome = QLabel(self)
        self.welcome.setText('DAFTAR MEMBER')
        self.welcome.setStyleSheet("color : #079e4f;font-weight:500;")
        self.welcome.setFont(QFont('Terminus', 20))
        self.welcome.adjustSize()
        self.welcome.setGeometry(100,10,300,40)

        self.namaLabel = QLabel(self)
        self.namaLabel.setStyleSheet(style().lbl_nama)
        self.namaLabel.setGeometry(60,100,30,30)

        self.namaInput = QLineEdit(self)
        self.namaInput.setGeometry(100,100,300,30)
        self.namaInput.setPlaceholderText("Masukkan Nama")

        self.userLabel = QLabel(self)
        self.userLabel.setStyleSheet(style().lbl_user)
        self.userLabel.setGeometry(60,150,30,30)

        self.userInput = QLineEdit(self)
        self.userInput.setGeometry(100,150,300,30)
        self.userInput.setPlaceholderText("Masukkan Username")
        self.passInput = QLineEdit(self)

        self.passLabel = QLabel(self)
        self.passLabel.setStyleSheet(style().lbl_pass)
        self.passLabel.setGeometry(60,200,30,30)

        self.passInput.setGeometry(100,200,300,30)
        self.passInput.setEchoMode(QLineEdit.Password)
        self.passInput.setPlaceholderText("Masukkan Password Minimal 6 Digit")

        self.daftarButton = QPushButton(self)
        self.daftarButton.setText("Daftar Menjadi Member")
        self.daftarButton.setGeometry(100,250,300,30)
        self.daftarButton.clicked.connect(self.btn_fungsi)

        self.back = QPushButton(self)
        self.back.setText('Kembali')
        self.back.setGeometry(380,335,100,40)
        self.back.clicked.connect(self.btn_back)

        ################################################### STYLESHEET #################################################
        self.namaInput.setStyleSheet(style().le_login)
        self.userInput.setStyleSheet(style().le_login)
        self.passInput.setStyleSheet(style().le_login)
        self.daftarButton.setStyleSheet(style().btn_login)
        self.back.setStyleSheet(style().btn)
        ################################################################################################################

    def btn_back(self):
        self.namaInput.setText('')
        self.userInput.setText('')
        self.passInput.setText('')
        self.hide()
        wlogin.win.show()

    def btn_fungsi(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user = "root",
            passwd = "",
            database = "RindangIn"
            )
        self.myqursor = self.mydb.cursor()
        nama = self.namaInput.text()
        username = self.userInput.text()
        pasword = caesar.enkripsi(caesar,self.passInput.text())
        if nama == '' or username == '' or pasword == '':
            QMessageBox.warning(self,"Gagal Memasukkan Data", "Periksa Data yang Anda Masukkan Dengan Tepat")
        elif len(pasword) < 6:
            self.passInput.setText('')
            QMessageBox.warning(self,"Gagal Memasukkan Data", "Masukkan Password Minimal 6 Digit")
        else:
            self.myqursor.execute(f"select username from anggota where username = '{username}'")
            self.data = self.myqursor.fetchone()
            if self.data == None:
                sql = "insert into anggota(nama,username,password) values (%s,%s,%s);"
                val = (nama,username,pasword)
                self.myqursor.execute(sql,val)
                self.mydb.commit()
                self.myqursor.close()
                self.mydb.close()
                QMessageBox.information(self,"Berhasil", "Berhasil Mendaftar Menjadi Member")
                self.namaInput.setText('')
                self.userInput.setText('')
                self.passInput.setText('')
            else:
                QMessageBox.warning(self,"Gagal", "Username yang Anda Masukkan Telah Digunakan")
                self.userInput.setText('')
                self.passInput.setText('')

################################################## WINDOW UTAMA ########################################################

class tutama(QMainWindow):
    def __init__(self):
        super(tutama, self).__init__()
        self.setWindowIcon(QIcon("logo/logo.png"))
        self.setWindowTitle('Rindang.In')
        self.setFixedSize(1000, 700)
        self.setGeometry(0, 0, 1000, 700) #x,y,width,height
        self.setStyleSheet("background-color:white")

        self.logo = QLabel(self)
        self.logo.pixmap = QPixmap('logo/logo.png')
        self.logo.setPixmap(self.logo.pixmap)
        self.logo.adjustSize()
        self.logo.move(250,-50)#x,y

        self.welcome = QLabel(self)
        self.welcome.setText('Selamat Datang di Rindang.In')
        self.welcome.setStyleSheet("color : #079e4f")
        self.welcome.setFont(QFont('Terminus', 25))
        self.welcome.adjustSize()
        self.welcome.move(230,225)

        self.fiturLabel = QLabel(self)
        self.fiturLabel.setText('Pilih Menu')
        self.fiturLabel.setStyleSheet("color : rgb(7, 158, 79);font-weight:500")
        self.fiturLabel.setFont(QFont('Terminus', 20))
        self.fiturLabel.setGeometry(420,300,500,30)

        self.btn()

    def btn(self):
        self.thias = QPushButton(self)
        self.thiasLabel = QLabel(self)
        self.thiasLabel.setText("Tanaman Hias")
        self.thiasLabel.setGeometry(135,505,165,30)
        self.thiasLabel.setStyleSheet("QLabel{font-weight:400;color:green;}")
        self.thiasLabel.setFont(QFont('Terminus', 14))

        self.tobat = QPushButton(self)
        self.tobatLabel = QLabel(self)
        self.tobatLabel.setText("Tanaman Obat")
        self.tobatLabel.setGeometry(135+190,505,165,30)
        self.tobatLabel.setStyleSheet("QLabel{font-weight:400;color:green;}")
        self.tobatLabel.setFont(QFont('Terminus', 14))

        self.alat = QPushButton(self)
        self.alatLabel = QLabel(self)
        self.alatLabel.setText("Alat Berkebun")
        self.alatLabel.setGeometry(135+190+195,505,165,30)
        self.alatLabel.setStyleSheet("QLabel{font-weight:400;color:green;}")
        self.alatLabel.setFont(QFont('Terminus', 14))

        self.pubit = QPushButton(self)
        self.pubitLabel = QLabel(self)
        self.pubitLabel.setText("Pupuk dan Bibit")
        self.pubitLabel.setGeometry(135+190+190+185,505,170,30)
        self.pubitLabel.setStyleSheet("QLabel{font-weight:400;color:green;}")
        self.pubitLabel.setFont(QFont('Terminus', 14))

        self.thias.setGeometry(140,350,150,150)
        self.tobat.setGeometry(330,350,150,150)
        self.alat.setGeometry(520,350,150,150)
        self.pubit.setGeometry(710,350,150,150)

        self.insert = QPushButton(self)
        self.insert.setText('Insert Data')
        self.insert.setGeometry(395,550,200,50)

        self.logout = QPushButton(self)
        self.logout.setText('Logout')
        self.logout.setGeometry(880,630,100,50)

        self.about = QPushButton(self)
        self.about.setText('About Us')
        self.about.setGeometry(445,630,100,50)

        ################################################## STYLESHEET ##################################################
        self.thias.setStyleSheet(style().btn_thias)
        self.tobat.setStyleSheet(style().btn_tobat)
        self.alat.setStyleSheet(style().btn_alat)
        self.pubit.setStyleSheet(style().btn_pubit)
        self.insert.setStyleSheet(style().btn)
        self.logout.setStyleSheet(style().btn)
        self.about.setStyleSheet(style().btn_login)
        ################################################################################################################

        chrome_path = 'C:/Users/user/AppData/Local/Google/Chrome/Application/chrome.exe %s'
        self.about.clicked.connect(lambda: webbrowser.get(chrome_path).open_new_tab('http://149.129.223.63/wiki/index.php/Rindang.in'))
        
##################################################### WINDOW INSERT DATA ###############################################

class tinsert(QMainWindow):
    def __init__(self):
        super(tinsert, self).__init__()
        self.setGeometry(0,0,600,410)
        self.setFixedSize(600,410)
        self.setWindowIcon(QIcon("logo/logo.png"))
        self.setWindowTitle('Rindang.In/Insert Data')
        self.setStyleSheet("background-color:white;")

        self.back = QPushButton(self)
        self.back.setText('Kembali')
        self.back.setGeometry(450,355,100,40)
        self.back.clicked.connect(self.btn_back)
        self.back.raise_()

        self.initUI()

    def initUI(self):
        self.judulLabel = QLabel(self)
        self.judulLabel.setText("Tanaman Hias")
        self.judulLabel.setFont(QFont('Comic Sans MS', 25))
        self.judulLabel.setStyleSheet("color : #079e4f")
        self.judulLabel.setGeometry(10,10,500,40)

        ################################################## RADIO BUTTON ################################################
        self.rb_thias = QRadioButton(self)
        self.rb_thias.setText("Tanaman Hias")
        self.rb_tobat = QRadioButton(self)
        self.rb_tobat.setText("Tanaman Obat")
        self.rb_alat = QRadioButton(self)
        self.rb_alat.setText("Peralatan Berkebun")
        self.rb_pubit = QRadioButton(self)
        self.rb_pubit.setText("Pupuk dan Bibit")

        self.rb_thias.setGeometry(10,60,200,20)
        self.rb_tobat.setGeometry(160,60,200,20)
        self.rb_alat.setGeometry(310,60,200,20)
        self.rb_pubit.setGeometry(460,60,200,20)

        ################################################## FORM ########################################################
        self.namaLabel = QLabel(self)
        self.namaInput = QLineEdit(self)
        self.namaLabel.setGeometry(10,100,200,50)
        self.namaInput.setGeometry(200,110,200,30)
        self.namaInput.setPlaceholderText("Cth : Kaktus Organik")

        self.gambarLabel = QLabel(self)
        self.gambarInput = QLineEdit(self)
        self.gambarButton = QPushButton(self)
        self.gambarButton.setText("Browse File")
        self.gambarButton.clicked.connect(self.browse)

        self.gambarLabel.setGeometry(10,140,200,50)
        self.gambarInput.setPlaceholderText("Click Browse File")
        self.gambarInput.setGeometry(200,150,200,30)
        self.gambarButton.setGeometry(400,150,170,30)
        self.gambarInput.setReadOnly(True)

        self.hargaLabel = QLabel(self)
        self.hargaInput = QLineEdit(self)
        self.hargaLabel.setText(f"Harga")
        self.hargaLabel.setGeometry(10,180,200,50)
        self.hargaInput.setGeometry(200,190,200,30)
        self.hargaInput.setPlaceholderText("Cth : 25000")

        self.alamatLabel = QLabel(self)
        self.alamatInput = QLineEdit(self)
        self.alamatLabel.setText(f"Alamat")
        self.alamatLabel.setGeometry(10,220,200,50)
        self.alamatInput.setGeometry(200,230,200,30)
        self.alamatInput.setPlaceholderText("Cth : Bontang, Jl. Ahmad Yani")

        self.kontakLabel = QLabel(self)
        self.kontakInput = QLineEdit(self)
        self.kontakLabel.setText(f"Kontak")
        self.kontakLabel.setGeometry(10,260,200,50)
        self.kontakInput.setGeometry(200,270,200,30)
        self.kontakInput.setPlaceholderText("Cth : +628123456789")

        self.deskripsiLabel = QLabel(self)
        self.deskripsiInput = QLineEdit(self)
        self.deskripsiLabel.setText("Deskripsi")
        self.deskripsiLabel.setGeometry(10,300,200,50)
        self.deskripsiInput.setGeometry(200,310,200,30)
        self.deskripsiInput.setPlaceholderText("Cth : Kaktus adalah tanaman hias yang mudah untuk dirawat . . .")

        self.insertButton = QPushButton(self)
        self.insertButton.setText("Insert Data")
        self.insertButton.setGeometry(200,360,200,30)

        #################################################### STYLESHEET ################################################
        self.namaInput.setStyleSheet(style().le_login)
        self.namaInput.setStyleSheet(style().le_login)
        self.gambarInput.setStyleSheet(style().le_login)
        self.hargaInput.setStyleSheet(style().le_login)
        self.alamatInput.setStyleSheet(style().le_login)
        self.kontakInput.setStyleSheet(style().le_login)
        self.deskripsiInput.setStyleSheet(style().le_login)
        self.gambarButton.setStyleSheet(style().btn)
        self.insertButton.setStyleSheet(style().btn_login)
        self.back.setStyleSheet(style().btn)
        ################################################################################################################

        ######################################################### COMMAND ##############################################
        self.insertButton.clicked.connect(self.insertDB)
        self.rb_thias.setChecked(True)
        self.fungsi("Tanaman Hias", 'thias')

        self.rb_thias.clicked.connect(lambda : self.fungsi("Tanaman Hias", 'thias'))
        self.rb_tobat.clicked.connect(lambda : self.fungsi("Tanaman Obat", 'tobat'))
        self.rb_alat.clicked.connect(lambda : self.fungsi("Peralatan Berkebun", 'alat'))
        self.rb_pubit.clicked.connect(lambda : self.fungsi("Pupuk dan Bibit", 'pubit'))

    def btn_back(self):
        self.namaInput.setText('')
        self.gambarInput.setText('')
        self.hargaInput.setText('')
        self.alamatInput.setText('')
        self.kontakInput.setText('')
        self.deskripsiInput.setText('')
        self.hide()
        wutama.win.show()

    def fungsi(self, laman, tabel):
        self.laman = laman
        self.tabel = tabel
        self.judulLabel.setText(self.laman)
        self.namaLabel.setText(f"Nama {self.laman}")
        self.gambarLabel.setText(f"Gambar {self.laman}")

    def browse(self):
        gambarBrowse = QFileDialog.getOpenFileName(self, 'open file', 'D:/File Kuliah/Materi Perkuliahan S3/Pemrograman Berbasis Objek/Tubes QTDesign/Image', 'Images (*.jpeg *.jpg *.png)')
        self.gambarInput.setText(gambarBrowse[0])

    def insertDB(self):
        li = [self.gambarInput.text(),self.namaInput.text(),self.hargaInput.text(),self.alamatInput.text(),self.kontakInput.text(),self.deskripsiInput.text()]
        if li[0] == '' or li[1] == ''or li[2] == '' or li[3] == '' or li[4] == '' or li[5] == '' or ' ' in li[2] or ' ' in li[4]:
            QMessageBox.warning(self,"Failed", "Periksa Data yang Anda Masukkan Dengan Tepat")
        else:
            try:
                int(li[2])
                int(li[4])
            except:
                QMessageBox.warning(self,"Gagal Memasukkan Data", "Periksa Data yang Anda Masukkan Dengan Tepat")
            else:
                self.mydb = pymysql.connect(
                    host="localhost",
                    user = "root",
                    passwd = "",
                    database = "RindangIn"
                )
                self.myqursor = self.mydb.cursor()
                sql = f"insert into {self.tabel}(gambar,nama_{self.tabel},harga,alamat,no_telp,deskripsi) values (%s,%s,%s,%s,%s,%s)"

                val = (li[0],li[1],li[2],li[3],li[4],li[5])
                self.myqursor.execute(sql,val)
                QMessageBox.information(self,"Berhasil Memasukkan Data", f"Sukses Menambahkan Item ke Dalam {self.laman}")
                self.mydb.commit()
                self.myqursor.close()
                self.mydb.close()

                self.gambarInput.setText('')
                self.namaInput.setText('')
                self.hargaInput.setText('')
                self.alamatInput.setText('')
                self.kontakInput.setText('')
                self.deskripsiInput.setText('')

############################################ WINDOW TAMPILAN FITUR - FITUR #############################################

class tampilan(QMainWindow):
    def __init__(self, nama):
        super(tampilan, self).__init__()
        self.nama = nama
        self.setWindowIcon(QIcon("logo/logo.png"))
        self.setWindowTitle(f'Rindang.In/{self.nama}')
        self.setFixedSize(1000, 700)
        self.setStyleSheet("background-color:white;")
        self.setGeometry(0, 0, 1000, 700) #x,y,width,height

        self.initUI()
        self.Layoutt()
        self.btn()

    def btn(self):
        self.back = QPushButton(self)
        self.back.setText('Kembali')
        self.back.setStyleSheet(style().btn)
        self.back.setGeometry(875,655,100,40)
        self.back.clicked.connect(self.btn_back)

    def btn_back(self):
        self.hide()
        wutama.win.show()

    def initUI(self):
        self.labelJudul = QLabel(self)
        self.labelJudul.setText(f"{self.nama}")
        self.labelJudul.setStyleSheet("color : #079e4f")
        self.labelJudul.setFont(QFont('Comic Sans MS', 25))
        self.labelJudul.setGeometry(300,40,500,50)

        self.logo = QLabel(self)
        self.logo.setStyleSheet("image: url(logo/logosqr.png);")
        self.logo.setGeometry(10,10,100,100)

        self.bghead = QLabel(self)
        self.bghead.setStyleSheet("background-color: #079e4f;")
        self.bghead.setGeometry(0,120,1000,5)
        self.bghead.lower()
        self.bghead1 = QLabel(self)
        self.bghead1.setStyleSheet("background-color: #079e4f;")
        self.bghead1.setGeometry(0,0,1000,5)

    def db(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user = "root",
            passwd = "",
            database = "RindangIn"
        )

    def konten(self, fitur):
        self.db()
        self.myqursor = self.mydb.cursor()
        self.fitur = fitur
        xgbr = 10
        ygbr = 10
        self.x = 240
        self.y = 5
        self.myqursor.execute(f"select * from {self.fitur}")
        self.data = self.myqursor.fetchall()
        for i in self.data:
            self.gambar = QLabel(self.widget)
            self.nama = QLabel(self.widget)
            self.harga = QLabel(self.widget)
            self.alamat = QLabel(self.widget)
            self.deskripsi = QLabel(self.widget)
            self.bgkonten = QLabel(self.widget)
            self.chrome_path = 'C:/Users/user/AppData/Local/Google/Chrome/Application/chrome.exe %s'

            self.gambar.setStyleSheet(f"image: url({i[1]});")
            self.gambar.setGeometry(xgbr,ygbr,200,200)

            self.nama.setText(i[2])
            self.nama.setGeometry(self.x,self.y,1000,45)
            self.nama.setFont(QFont('Comic Sans MS', 20))

            self.line = QLabel(self.widget)
            self.line.setStyleSheet("background-color: #079e4f;")
            self.line.setGeometry(self.x,self.y+45,500,2)
            self.line.lower()

            self.hargaLabel = QLabel(self.widget)
            self.hargaLabel.setText("Harga :")
            self.hargaLabel.setGeometry(self.x,self.y+160,100,30)
            self.hargaLabel.setFont(QFont('Comic Sans MS', 14))
            self.harga.setText(f"Rp.{str(i[3])}")
            self.harga.setGeometry(self.x+100,self.y+160,1000,30)
            self.harga.setFont(QFont('Comic Sans MS', 14))

            self.urlA = f"https://www.google.com/maps/place/{i[4]}"
            self.alamatBtn(self.urlA)

            self.alamat.setText(i[4])
            self.alamat.setGeometry(self.x+280,self.y+155,220,45)
            self.alamat.setWordWrap(True)
            self.alamat.setAlignment(Qt.AlignJustify)
            self.alamat.setFont(QFont('Comic Sans MS', 8))

            self.urlK = f"https://wa.me/{i[5]}?text=Halo%20saya%20melihat%20jualan%20anda%20di%20Rindang.in%0ASaya%20ingin%20bertanya%20apakah%20barang%20yang%20anda%20jual%20masih%20tersedia?"
            self.kontakBtn(self.urlK)

            self.kontakLabel = QLabel(self.widget)
            self.kontakLabel.setText("Pesan Disini")
            self.kontakLabel.setGeometry(self.x+540,self.y+100,200,30)
            self.kontakLabel.setFont(QFont('Comic Sans MS', 12))

            #DESKRIPSI
            self.deskripsi.setText(i[6])
            self.deskripsi.setGeometry(self.x,self.y+50,500,100)
            self.deskripsi.setWordWrap(True)
            self.deskripsi.setAlignment(Qt.AlignJustify)
            self.deskripsi.setFont(QFont('Comic Sans MS',9))
            self.deskripsi.setStyleSheet("font-weight:300;")

            self.bgkonten.setGeometry(xgbr,ygbr,920,200)
            self.bgkonten.lower()

            self.bgkonten.setStyleSheet("background-color :rgb(163, 163, 163, 5%);")
            self.nama.setStyleSheet("background-color :match parent")
            self.deskripsi.setStyleSheet("background-color :match parent")
            self.hargaLabel.setStyleSheet("background-color :match parent")
            self.harga.setStyleSheet("background-color :match parent")
            self.alamat.setStyleSheet("background-color :match parent")
            self.kontakLabel.setStyleSheet("background-color :match parent")

            self.y += 210
            ygbr += 210
        self.widget.setFixedHeight(ygbr)

    def Layoutt(self):
        self.scroll = QScrollArea(self)
        self.scroll.setStyleSheet(style().sa_konten)
        self.scroll.setWidgetResizable(True)
        self.scroll.setGeometry(25,150,950,500)

        verticalScrollBar = QScrollBar(Qt.Vertical, self.scroll)
        verticalScrollBar.setStyleSheet(style().sb_konten)
        self.scroll.setVerticalScrollBar(verticalScrollBar)

        self.widget = QWidget()
        self.scroll.setWidget(self.widget)

    def alamatBtn(self, url):
        self.alamatButton = QPushButton(self.widget)
        self.alamatButton.setGeometry(self.x+230,self.y+155,40,40)
        self.alamatButton.setStyleSheet(style().btn_alamat)
        self.alamatButton.setToolTip("Cek Alamat Penjual di Google Maps")
        self.alamatButton.setIconSize(QSize(40, 40))
        self.alamatButton.clicked.connect(lambda: webbrowser.get(self.chrome_path).open_new_tab(url))

    def kontakBtn(self, url):
        self.kontak = QPushButton(self.widget)
        self.kontak.setStyleSheet(style().btn_kontak)
        self.kontak.setToolTip("Pesan Sekarang VIA WhatsApp")
        self.kontak.setGeometry(self.x+570,self.y+140,50,50)
        self.kontak.setIconSize(QSize(50, 50))
        self.kontak.clicked.connect(lambda: webbrowser.get(self.chrome_path).open_new_tab(url))

##################################################### INISIASI WINDOW ##################################################

class wlogin():
    win = tlogin()

class wdaftar():
    win = tdaftar()

class wutama():
    win = tutama()

class wthias():
    win = tampilan("Tanaman Hias")

class wtobat():
    win = tampilan("Tanaman Obat")

class walat():
    win = tampilan("Peralatan Berkebun")

class wpubit():
    win = tampilan("Pupuk dan Bibit")

class winsert():
    win = tinsert()

##################################################### PINDAH WINDOW ####################################################

class switch_window():
    def sthias(self):
        wutama.win.hide()
        wthias.win.konten('thias')
        wthias.win.show()
    def stobat(self):
        wutama.win.hide()
        wtobat.win.konten('tobat')
        wtobat.win.show()
    def salat(self):
        wutama.win.hide()
        walat.win.konten('alat')
        walat.win.show()
    def spubit(self):
        wutama.win.hide()
        wpubit.win.konten('pubit')
        wpubit.win.show()
    def sinsert(self):
        wutama.win.hide()
        winsert.win.show()
    def slogin(self):
        wutama.win.hide()
        wlogin.win.show()

################################################## BUTTON ACTION #######################################################

class btn_act():
    wutama.win.thias.clicked.connect(switch_window.sthias)
    wutama.win.tobat.clicked.connect(switch_window.stobat)
    wutama.win.alat.clicked.connect(switch_window.salat)
    wutama.win.pubit.clicked.connect(switch_window.spubit)
    wutama.win.insert.clicked.connect(switch_window.sinsert)
    wutama.win.logout.clicked.connect(switch_window.slogin)

###################################################### RUN #############################################################

wlogin.win.show()
main.exec_()

############################################### SAMPAH #################################################################
    # window.setStyleSheet("background-color : green")

    # head = QLabel(window)
    # head.pixmap = QPixmap('gambar/head.png')
    # head.setPixmap(head.pixmap)
    # head.adjustSize()
    # head.move(0,0)#x,y
    # head.setFixedHeight(20)
    # head.setFixedWidth(1000)


    # bghead = QLabel(window)
    # bghead.setStyleSheet("background-color: rgb(16, 255, 168);")
    # bghead.setGeometry(0,0,1000,100)
    # bghead.lower()


# class wtobat():
    # window = QMainWindow()
    # window.setWindowTitle('Rindang.In')
    # window.setGeometry(0, 0, 1000, 700) #x,y,width,height
    #
    # logo = QLabel(window)
    # logo.pixmap = QPixmap('gambar/logo.png')
    # logo.setPixmap(logo.pixmap)
    # logo.adjustSize()
    # logo.move(250,-50)#x,y



        # self.labelJudul = QLabel(self.widget)
        # self.labelJudul.setText(f"{self.nama}")
        # self.labelJudul.setStyleSheet("color : #079e4f")
        # self.labelJudul.setFont(QFont('Comic Sans MS', 25))
        # self.labelJudul.setGeometry(0,0,500,50)

#
# class btn():
#     thias = QPushButton(wutama.win)
#     thias.setText('Tanaman Hias')
#     tobat = QPushButton(wutama.win)
#     tobat.setText('Tanaman Obat')
#     alat = QPushButton(wutama.win)
#     alat.setText('Alat Berkebun')
#     pubit = QPushButton(wutama.win)
#     pubit.setText('Pupuk dan Bibit')
#
#     thias.setGeometry(30,350,220,50)
#     tobat.setGeometry(270,350,220,50)
#     alat.setGeometry(510,350,220,50)
#     pubit.setGeometry(750,350,220,50)
#
#     insert = QPushButton(wutama.win)
#     insert.setText('Insert Data')
#     insert.setGeometry(400,500,200,50)
#
#     logout = QPushButton(wutama.win)
#     logout.setText('Logout')
#     logout.setGeometry(880,630,100,50)

        # verticalScrollBar = QScrollBar(Qt.Vertical, self.scroll)
        # verticalScrollBar.setStyleSheet(my_stylesheet)
        # self.scroll.setVerticalScrollBar(verticalScrollBar)

        # self.scroll.setStyleSheet("background : transparant;")


 #        self.about.setStyleSheet(""" background-color: white;
 # border-style: solid;
 # border-width:1px;
 # border-radius:50px;
 # border-color: red;
 # max-width:100px;
 # max-height:100px;
 # min-width:100px;
 # min-height:100px;""")





# qproperty-icon:url(logo/thias.png);
#                                     qproperty-icon-position: top center;
#                                     text-align:left;
#                                     qproperty-iconSize: 50px 50px;
