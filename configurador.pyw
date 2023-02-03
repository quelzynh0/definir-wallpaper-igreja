import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import configparser
import datetime


hoje = datetime.datetime.now()
ano = hoje.strftime("%Y")
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
img_qua = config['img_culto']['img_qua']
img_sex = config['img_culto']['img_sex']
img_sab = config['img_culto']['img_sab']
img_dom = config['img_culto']['img_dom']
img_ebd = config['img_culto']['img_ebd']
img_padrao = config['img_culto']['img_padrao']
local_imagens = config['img_culto']['local_imgs']
imgs_permitidas = config['img_culto']['imgs_permitidas']


class mainWindow(QDialog):
    def __init__(self):
        super(mainWindow, self).__init__()
        loadUi("gui.ui", self)
        self.copyright.setText(f'Copyright © '+ano+' Ezequiel Marinho')
        self.line_qua.setText(img_qua)
        self.line_sex.setText(img_sex)
        self.line_sab.setText(img_sab)
        self.line_dom.setText(img_dom)
        self.line_ebd.setText(img_ebd)
        self.line_padrao.setText(img_padrao)
        self.line_pastaPadrao.setText(local_imagens)
        self.textBrowser.setText(imgs_permitidas)
        self.btn_qua.clicked.connect(self.btnQua)
        self.btn_sex.clicked.connect(self.btnSex)
        self.btn_sab.clicked.connect(self.btnSab)
        self.btn_dom.clicked.connect(self.btnDom)
        self.btn_ebd.clicked.connect(self.btnEbd)
        self.btn_padrao.clicked.connect(self.btnPadrao)
        self.btn_pastaPadrao.clicked.connect(self.btnPastaPadrao)

    def btnQua(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Selecione o Wallpaper', local_imagens, imgs_permitidas)
        self.line_qua.setText(fname[0])
        config.set('img_culto', 'img_qua', fname[0])
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def btnSex(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Selecione o Wallpaper', local_imagens, imgs_permitidas)
        self.line_sex.setText(fname[0])
        config.set('img_culto', 'img_sex', fname[0])
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def btnSab(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Selecione o Wallpaper', local_imagens, imgs_permitidas)
        self.line_sab.setText(fname[0])
        config.set('img_culto', 'img_sab', fname[0])
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def btnDom(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Selecione o Wallpaper', local_imagens, imgs_permitidas)
        self.line_dom.setText(fname[0])
        config.set('img_culto', 'img_dom', fname[0])
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def btnEbd(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Selecione o Wallpaper', local_imagens, imgs_permitidas)
        self.line_ebd.setText(fname[0])
        config.set('img_culto', 'img_ebd', fname[0])
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def btnPadrao(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Selecione o Wallpaper', local_imagens, imgs_permitidas)
        self.line_padrao.setText(fname[0])
        config.set('img_culto', 'img_padrao', fname[0])
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def btnPastaPadrao(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open file')
        self.line_pastaPadrao.setText(fname)
        config.set('img_culto', 'local_imgs', fname)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = mainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainWindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(340)
    widget.show()

    try:
        sys.exit(app.exec())

    except SystemExit:
        print('Fechando janela')
