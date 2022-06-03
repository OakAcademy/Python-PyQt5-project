from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import Database
from AddLeave import EmployeeLeaveDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_3.addWidget(self.toolButton, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leave Info"))
        self.label.setText(_translate("MainWindow", "Leave Date"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Leave Info"))
        self.pushButton.setText(_translate("MainWindow", "New"))
        self.pushButton_2.setText(_translate("MainWindow", "Show"))


class Employee_Info_Window(QtWidgets.QMainWindow):

    def __init__(self, id):
        super(Employee_Info_Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id = id
        self.init_tables()

        self.ui.pushButton.clicked.connect(self.add_leave_button_clicked)


    def init_tables(self):
         self.database = Database()

         leave_info = self.database.get_employee_leave_info(self.id)
         self.init_table(self.ui.tableWidget,leave_info[0],leave_info[1])


    def init_table(self,tableWidget,header_list,value_list):
        number_row = len(value_list)
        number_column = len(header_list)

        tableWidget.setRowCount(number_row)
        tableWidget.setColumnCount(number_column)


        tableWidget.setHorizontalHeaderLabels(tuple(header_list))
        tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        tableWidget.verticalHeader().hide()

        for row in range(number_row):
            for col in range(number_column):
                tableWidget.setItem(row,col,QTableWidgetItem(str(value_list[row][col])))


    def add_leave_button_clicked(self):
        self.employeeLeaveDialog = EmployeeLeaveDialog()
        result = self.employeeLeaveDialog.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.database.add_new_leave(self.employeeLeaveDialog.employee_leave_info)














