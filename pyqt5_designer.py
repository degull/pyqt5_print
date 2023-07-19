from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 1101)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.groupBox_1 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 1091, 51))
        self.groupBox_1.setTitle("")
        self.groupBox_1.setObjectName("groupBox_1")
        self.label_1 = QtWidgets.QLabel(self.groupBox_1)
        self.label_1.setGeometry(QtCore.QRect(30, 10, 591, 31))
        self.label_1.setObjectName("label_1")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_1.setGeometry(QtCore.QRect(810, 10, 271, 31))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setObjectName("pushButton_1")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 560, 1091, 431))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 70, 1091, 431))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 510, 1091, 51))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 591, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(810, 10, 271, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 1091, 71))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 10, 181, 51))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableView_1 = QtWidgets.QTableView(self.tab_2)
        self.tableView_1.setGeometry(QtCore.QRect(10, 150, 371, 741))
        self.tableView_1.setObjectName("tableView_1")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(390, 100, 711, 781))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 681, 761))
        self.label_6.setObjectName("label_6")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 80, 371, 71))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_1.setGeometry(QtCore.QRect(120, 30, 113, 31))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 30, 112, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_3.setObjectName("tab_3")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 1101, 81))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 0, 1081, 81))
        self.groupBox_9.setObjectName("groupBox_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 40, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 40, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_7.setGeometry(QtCore.QRect(370, 30, 112, 34))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_9)
        self.label_7.setGeometry(QtCore.QRect(160, 40, 21, 18))
        self.label_7.setObjectName("label_7")
        self.tableView_2 = QtWidgets.QTableView(self.tab_3)
        self.tableView_2.setGeometry(QtCore.QRect(10, 100, 1081, 901))
        self.tableView_2.setObjectName("tableView_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.tab_3)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1070, 101, 20, 899))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "파일을 첨부하세요"))
        self.pushButton_1.setText(_translate("MainWindow", "파일 첨부하기1"))
        self.groupBox_4.setTitle(_translate("MainWindow", "그래프"))
        self.label_5.setText(_translate("MainWindow", "그래프 1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "그래프"))
        self.label_2.setText(_translate("MainWindow", "그래프 1"))
        self.label_3.setText(_translate("MainWindow", "파일을 첨부하세요"))
        self.pushButton_2.setText(_translate("MainWindow", "파일 첨부하기2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "그래프 출력"))
        self.pushButton_3.setText(_translate("MainWindow", "파일 첨부하기1"))
        self.pushButton_4.setText(_translate("MainWindow", "파일 첨부하기2"))
        self.groupBox_7.setTitle(_translate("MainWindow", "그래프"))
        self.label_6.setText(_translate("MainWindow", "그래프 표시"))
        self.groupBox_6.setTitle(_translate("MainWindow", "변화 값 검색"))
        self.pushButton_5.setText(_translate("MainWindow", "검색"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "그래프 비교"))
        self.groupBox_9.setTitle(_translate("MainWindow", "파수 구간 입력"))
        self.pushButton_7.setText(_translate("MainWindow", "검색"))
        self.label_7.setText(_translate("MainWindow", "~"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "파수별 성분 검색"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

