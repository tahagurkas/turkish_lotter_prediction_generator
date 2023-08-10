import math, random
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from numpy import sort
from sayısal_python import Ui_Form


class lotoPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.sayısalfrom = Ui_Form()
        self.sayısalfrom.setupUi(self)
        self.sayısalfrom.pushButton_oyna.clicked.connect(self.ButonOyna)

    def ButonOyna(self):
        kolonSayısı = int(self.sayısalfrom.comboBox_adet.currentText())

        if self.sayısalfrom.radioButton_sayisalLoto.isChecked():
            self.sayısalLoto(kolonSayısı)

        if self.sayısalfrom.radioButton_superLoto.isChecked():
            self.superLoto(kolonSayısı)

        if self.sayısalfrom.radioButton_sansTopu.isChecked():
            self.sansTopu(kolonSayısı)

        if self.sayısalfrom.radioButton_onNumara.isChecked():
            self.onNumara(kolonSayısı)

    def sayısalLoto(self, kolon):
        self.clear()
        for i in range(1, kolon + 1):
            sayısallotoList = []
            j = 1
            while j <= 6:
                number = math.ceil(random.random() * 90)
                if number not in sayısallotoList:
                    sayısallotoList.append(number)
                    j += 1
            self.sayısalfrom.lineEdit.setText(f"Toplam Tutar = {kolon*6} TL")
            sayısallotoList = sort(sayısallotoList)
            mesaj = f"Sayısal Loto : {i}. Kolon = {sayısallotoList}" + "\n\n"
            self.sayısalfrom.textEdit.insertPlainText(mesaj)

    def superLoto(self, kolon):
        self.clear()
        for i in range(1, kolon + 1):
            superlotoList = []
            j = 1
            while j <= 6:
                number = math.ceil(random.random() * 60)
                if number not in superlotoList:
                    superlotoList.append(number)
                    j += 1
            self.sayısalfrom.lineEdit.setText(f"Toplam Tutar = {kolon*6} TL")
            superlotoList = sort(superlotoList)
            mesaj = f"Süper Loto : {i}. Kolon = {superlotoList}" + "\n\n"
            self.sayısalfrom.textEdit.insertPlainText(mesaj)

    def sansTopu(self, kolon):
        self.clear()
        for i in range(1, kolon + 1):
            sanstopuList = []
            sanstopuList_alt = []
            j = 1
            while j <= 5:
                number = math.ceil(random.random() * 34)
                if number not in sanstopuList:
                    sanstopuList.append(number)
                    j += 1
            self.sayısalfrom.lineEdit.setText(f"Toplam Tutar = {kolon*4} TL")
            sanstopuList_alt.append(math.ceil(random.random() * 14))
            sanstopuList = sort(sanstopuList)
            mesaj = (
                f"Şans Topu : {i}. Kolon = {sanstopuList} + {sanstopuList_alt}"
                + "\n\n"
            )
            self.sayısalfrom.textEdit.insertPlainText(mesaj)

    def onNumara(self, kolon):
        self.clear()
        for i in range(1, kolon + 1):
            onNumaraList = []
            j = 1
            while j <= 10:
                number = math.ceil(random.random() * 80)
                if number not in onNumaraList:
                    onNumaraList.append(number)
                    j += 1
            self.sayısalfrom.lineEdit.setText(f"Toplam Tutar = {kolon*4} TL")
            onNumaraList = sort(onNumaraList)
            mesaj = f"Şans Topu : {i}. Kolon = {onNumaraList} " + "\n\n"
            self.sayısalfrom.textEdit.insertPlainText(mesaj)

    def clear(self):
        self.sayısalfrom.textEdit.clear()
