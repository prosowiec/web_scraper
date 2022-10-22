
import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

from webscraper import summing_everything_up_pl,scrap_images ,find_url_and_prettify_PL, summing_everything_up_de, find_url_and_prettify_DE,\
summing_everything_up_fr, find_url_and_prettify_FR

                      
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Amazon webscraper")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 29, 1200, 800))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.text_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.text_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.text_layout.setContentsMargins(0, 0, 0, 0)
        self.text_layout.setSpacing(0)
        self.text_layout.setObjectName("text_layout")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalScrollBar.sizePolicy().hasHeightForWidth())
        self.verticalScrollBar.setSizePolicy(sizePolicy)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.text_layout.addWidget(self.verticalScrollBar, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setBaseSize(QtCore.QSize(0, 1))
        self.textBrowser.setTabletTracking(False)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.text_layout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 0, 1061, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # ADD_ASIN line
        self.ADD_ASIN = QtWidgets.QLineEdit(self.layoutWidget)
        self.ADD_ASIN.setInputMask("")
        self.ADD_ASIN.setText("")
        self.ADD_ASIN.setObjectName("ADD_ASIN")
        self.horizontalLayout.addWidget(self.ADD_ASIN)

        #BUTTON ASSIN LINE
        self.BUTTON_ASSIN = QtWidgets.QPushButton(self.layoutWidget)
        self.BUTTON_ASSIN.setObjectName("BUTTON_ASSIN")
        self.horizontalLayout.addWidget(self.BUTTON_ASSIN)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        #download button 
        self.download_button = QtWidgets.QPushButton(self.layoutWidget)
        self.download_button.setIconSize(QtCore.QSize(32, 16))
        self.download_button.setObjectName("download_button")
        self.horizontalLayout.addWidget(self.download_button)

        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.copy = QtWidgets.QPushButton(self.layoutWidget)
        self.copy.setObjectName("copy")
        self.horizontalLayout.addWidget(self.copy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.copy.clicked.connect(self.copy_text) 

        #asin button
        self.BUTTON_ASSIN.clicked.connect(self.text_function)
        #download button
        soup_pl = find_url_and_prettify_PL(str(self.ADD_ASIN.text()))
        self.download_button.clicked.connect(self.download_images)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Amazon webscraper"))
        self.label.setText(_translate("MainWindow", "PODAJ ASIN"))
        self.BUTTON_ASSIN.setText(_translate("MainWindow", "ZNAJDZ PO ASIN"))
        self.download_button.setText(_translate("MainWindow", "POBIERZ ZDJĘCIA"))
        self.copy.setText(_translate("MainWindow", "KOPIUJ TEKST"))

    def text_function(self):
        ASIN = str(self.ADD_ASIN.text())
        soup_pl = find_url_and_prettify_PL(ASIN)
        final_description_PL = summing_everything_up_pl(soup_pl)

        soup_de = find_url_and_prettify_DE(ASIN)
        final_description_PL_DE = summing_everything_up_de(soup_de)

        soup_fr = find_url_and_prettify_FR(ASIN)
        final_description_FR = summing_everything_up_fr(soup_fr)

        full_description = final_description_PL + final_description_PL_DE + final_description_FR
        self.textBrowser.setText(full_description)


    def download_images(self):
        ASIN = str(self.ADD_ASIN.text())
        soup_de = find_url_and_prettify_DE(ASIN)
        scrap_images(soup_de,ASIN)
        

    def copy_text(self):
        self.textBrowser.selectAll()
        self.textBrowser.copy()


        
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


