# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CountryApplication.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_choose_country = QtWidgets.QLabel(self.centralwidget)
        self.label_choose_country.setGeometry(QtCore.QRect(10, 20, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_choose_country.setFont(font)
        self.label_choose_country.setObjectName("label_choose_country")
        self.listWidget_country_lists = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_country_lists.setGeometry(QtCore.QRect(10, 50, 201, 411))
        self.listWidget_country_lists.setObjectName("listWidget_country_lists")
        self.label_country_name = QtWidgets.QLabel(self.centralwidget)
        self.label_country_name.setGeometry(QtCore.QRect(230, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_country_name.setFont(font)
        self.label_country_name.setText("")
        self.label_country_name.setObjectName("label_country_name")
        self.label_flags = QtWidgets.QLabel(self.centralwidget)
        self.label_flags.setGeometry(QtCore.QRect(240, 80, 241, 161))
        self.label_flags.setText("")
        self.label_flags.setObjectName("label_flags")
        self.label_population = QtWidgets.QLabel(self.centralwidget)
        self.label_population.setGeometry(QtCore.QRect(320, 290, 61, 21))
        self.label_population.setObjectName("label_population")
        self.label_total_area = QtWidgets.QLabel(self.centralwidget)
        self.label_total_area.setGeometry(QtCore.QRect(250, 330, 61, 16))
        self.label_total_area.setObjectName("label_total_area")
        self.comboBox_choose_way = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_choose_way.setGeometry(QtCore.QRect(320, 330, 61, 21))
        self.comboBox_choose_way.setObjectName("comboBox_choose_way")
        self.comboBox_choose_way.addItem("")
        self.comboBox_choose_way.addItem("")
        self.lineEdit_population = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_population.setGeometry(QtCore.QRect(380, 290, 113, 20))
        self.lineEdit_population.setObjectName("lineEdit_population")
        self.label_density_per_mi = QtWidgets.QLabel(self.centralwidget)
        self.label_density_per_mi.setGeometry(QtCore.QRect(230, 370, 151, 31))
        self.label_density_per_mi.setObjectName("label_density_per_mi")
        self.label_percentage_world_population = QtWidgets.QLabel(self.centralwidget)
        self.label_percentage_world_population.setGeometry(QtCore.QRect(220, 410, 161, 31))
        self.label_percentage_world_population.setObjectName("label_percentage_world_population")
        self.label_total_area_result = QtWidgets.QLabel(self.centralwidget)
        self.label_total_area_result.setGeometry(QtCore.QRect(390, 330, 101, 21))
        self.label_total_area_result.setText("")
        self.label_total_area_result.setObjectName("label_total_area_result")
        self.label_density_per_mi_result = QtWidgets.QLabel(self.centralwidget)
        self.label_density_per_mi_result.setGeometry(QtCore.QRect(390, 380, 91, 16))
        self.label_density_per_mi_result.setText("")
        self.label_density_per_mi_result.setObjectName("label_density_per_mi_result")
        self.label_percentage_world_population_result = QtWidgets.QLabel(self.centralwidget)
        self.label_percentage_world_population_result.setGeometry(QtCore.QRect(390, 420, 101, 16))
        self.label_percentage_world_population_result.setText("")
        self.label_percentage_world_population_result.setObjectName("label_percentage_world_population_result")
        self.pushButton_update_population = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update_population.setGeometry(QtCore.QRect(370, 460, 111, 31))
        self.pushButton_update_population.setObjectName("pushButton_update_population")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Load_Countries = QtWidgets.QAction(MainWindow)
        self.action_Load_Countries.setObjectName("action_Load_Countries")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Load_Countries)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Exit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Countries of the World"))
        self.label_choose_country.setText(_translate("MainWindow", "Choose a country from the list:"))
        self.label_population.setText(_translate("MainWindow", "Population:"))
        self.label_total_area.setText(_translate("MainWindow", "Total Area in"))
        self.comboBox_choose_way.setItemText(0, _translate("MainWindow", "Sq. Mi."))
        self.comboBox_choose_way.setItemText(1, _translate("MainWindow", "Sq. KM."))
        self.label_density_per_mi.setText(_translate("MainWindow", "Population Density per Sq. Mi.:"))
        self.label_percentage_world_population.setText(_translate("MainWindow", "Percentage of World Population:"))
        self.pushButton_update_population.setText(_translate("MainWindow", "Update Population"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_Load_Countries.setText(_translate("MainWindow", "Load Countries"))
        self.action_Exit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

