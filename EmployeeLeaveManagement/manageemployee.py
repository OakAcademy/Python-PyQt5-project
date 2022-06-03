from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEvent,Qt, QObject
from newemployee import EmployeeDialog
from database import Database
from manageemployeeleave import Employee_Info_Window
import csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.upperGridLayout = QtWidgets.QGridLayout()
        self.upperGridLayout.setObjectName("upperGridLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.upperGridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(618, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upperGridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.upperGridLayout, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(132, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.idlabel = QtWidgets.QLabel(self.widget)
        self.idlabel.setObjectName("idlabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idlabel)
        self.idLineEdit = QtWidgets.QLineEdit(self.widget)
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idLineEdit)
        self.firstnamelabel = QtWidgets.QLabel(self.widget)
        self.firstnamelabel.setObjectName("firstnamelabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firstnamelabel)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastnamelabel = QtWidgets.QLabel(self.widget)
        self.lastnamelabel.setObjectName("lastnamelabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastnamelabel)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.gridLayout_4.addLayout(self.formLayout, 0, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.departmenlabel = QtWidgets.QLabel(self.widget)
        self.departmenlabel.setObjectName("departmenlabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.departmenlabel)
        self.departmentLineEdit = QtWidgets.QLineEdit(self.widget)
        self.departmentLineEdit.setObjectName("departmentLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.departmentLineEdit)
        self.positionlabel = QtWidgets.QLabel(self.widget)
        self.positionlabel.setObjectName("positionlabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.positionlabel)
        self.positionLineEdit = QtWidgets.QLineEdit(self.widget)
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.positionLineEdit)
        self.gridLayout_4.addLayout(self.formLayout_2, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(155, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 3, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.applyButton = QtWidgets.QPushButton(self.widget)
        self.applyButton.setObjectName("applyButton")
        self.gridLayout_2.addWidget(self.applyButton, 0, 1, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.widget)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout_2.addWidget(self.resetButton, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 4)
        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(398, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 0, 1, 1, 1)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.gridLayout.addWidget(self.newButton, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Employee"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.idlabel.setText(_translate("MainWindow", "Personal ID"))
        self.firstnamelabel.setText(_translate("MainWindow", "First Name"))
        self.lastnamelabel.setText(_translate("MainWindow", "Last Name"))
        self.departmenlabel.setText(_translate("MainWindow", "Department"))
        self.positionlabel.setText(_translate("MainWindow", "Position"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.newButton.setText(_translate("MainWindow", "New"))
        self.pushButton_3.setText(_translate("MainWindow", "Export"))



class EmployeeWindow(QtWidgets.QMainWindow):
    def __init__(self, mainMenu):
       super(EmployeeWindow, self).__init__()

       self.mainMenu = mainMenu
       self.ui = Ui_MainWindow()
       self.ui.setupUi(self)

       self.init_table()

       self.init_field_map()


       self.ui.tableWidget.viewport().installEventFilter(self)
       self.ui.newButton.clicked.connect(self.new_button_clicked)
       self.ui.backButton.clicked.connect(self.back_button_clicked)

       self.ui.applyButton.clicked.connect(self.apply_button_clicked)

       self.ui.resetButton.clicked.connect(self.reset_button_clicked)

       self.ui.pushButton_3.clicked.connect(self.export_button_clicked)



    def reload_table(self,conditionList):
        self.ui.tableWidget.setRowCount(0)

        result_list = self.db.get_employee_info(conditionList)

        header_list = result_list[0]
        value_list = result_list[1]

        number_row = len(value_list)
        number_column = len(header_list)
        self.ui.tableWidget.setRowCount(number_row)
        self.ui.tableWidget.setColumnCount(number_column)

        for row in range(number_row):
            for col in range(number_column):
                self.ui.tableWidget.setItem(row,col,QTableWidgetItem(str(value_list[row][col])))


    def init_field_map(self):

        self.fieldMap = {}
        self.fieldMap[self.ui.idLineEdit.objectName()] = "personal_id"
        self.fieldMap[self.ui.firstNameLineEdit.objectName()] = "first_name"
        self.fieldMap[self.ui.lastNameLineEdit.objectName()] = "last_name"
        self.fieldMap[self.ui.departmentLineEdit.objectName()] = "department_name"
        self.fieldMap[self.ui.positionLineEdit.objectName()] = "position"

    def reset_button_clicked(self):
        self.ui.idLineEdit.clear()
        self.ui.firstNameLineEdit.clear()
        self.ui.lastNameLineEdit.clear()
        self.ui.departmentLineEdit.clear()
        self.ui.positionLineEdit.clear()

        self.reload_table([])


    def apply_button_clicked(self):
        condition_list = []

        if self.ui.idLineEdit.text():
            condition_list.append([self.fieldMap[self.ui.idLineEdit.objectName()], "\"" + self.ui.idLineEdit.text() + "\""])

        if self.ui.firstNameLineEdit.text():
            condition_list.append([self.fieldMap[self.ui.firstNameLineEdit.objectName()], "\"" + self.ui.firstNameLineEdit.text() + "\""])

        if self.ui.lastNameLineEdit.text():
            condition_list.append([self.fieldMap[self.ui.lastNameLineEdit.objectName()], "\"" + self.ui.lastNameLineEdit.text() + "\""])

        if self.ui.departmentLineEdit.text():
            condition_list.append([self.fieldMap[self.ui.departmentLineEdit.objectName()], "\"" + self.ui.departmentLineEdit.text() + "\""])

        if self.ui.positionLineEdit.text():
            condition_list.append([self.fieldMap[self.ui.positionLineEdit.objectName()], "\"" + self.ui.positionLineEdit.text() + "\""])

        self.reload_table(condition_list)


    def init_table(self):
        self.db = Database()
        employee_list = self.db.get_employee_info([])
        header_list = employee_list[0]
        value_list = employee_list[1]

        number_row = len(value_list)
        number_column = len(header_list)
        self.ui.tableWidget.setRowCount(number_row)
        self.ui.tableWidget.setColumnCount(number_column)

        self.ui.tableWidget.setHorizontalHeaderLabels(tuple(header_list))
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget.verticalHeader().hide()

        for row in range(number_row):
            for col in range(number_column):
                self.ui.tableWidget.setItem(row,col,QTableWidgetItem(str(value_list[row][col])))


    def eventFilter(self,obj,event):
        if obj == self.ui.tableWidget.viewport() and event.type() == QEvent.MouseButtonPress:

            if event.button() == Qt.RightButton:
                m_index = self.ui.tableWidget.indexAt(event.pos())

                if m_index.isValid():
                    deleteAction = QAction("Delete", self)
                    deleteAction.setObjectName(str(m_index.row()))
                    deleteAction.triggered.connect(self.delete_action_triggered)

                    modifyAction = QAction("Modify", self)
                    modifyAction.setObjectName(str(m_index.row()))
                    modifyAction.triggered.connect(self.modify_action_triggered)

                    contextMenu = QMenu(self)
                    contextMenu.addAction(deleteAction)
                    contextMenu.addAction(modifyAction)

                    contextMenu.exec(event.globalPos())

        return QMainWindow.eventFilter(self, obj, event)


    def delete_action_triggered(self):
        reply = QMessageBox.question(self,"Delete", "Are you sure you want to delete this employee?")

        if reply == QMessageBox.Yes:
            row = int(QObject.sender(self).objectName())

            self.db.delete_employee(self.ui.tableWidget.item(row,0).text())
            self.ui.tableWidget.removeRow(row)



    def modify_action_triggered(self):
        row = int(QObject.sender(self).objectName())
        id = self.ui.tableWidget.item(row, 0).text()

        self.employee_info_window = Employee_Info_Window(id)
        self.employee_info_window.show()

    def back_button_clicked(self):
        self.hide()
        self.mainMenu.show()

    def new_button_clicked(self):
        self.employeeDialog = EmployeeDialog()
        result = self.employeeDialog.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.db.add_new_employee(self.employeeDialog.employee_info)



    def export_button_clicked(self):
        path = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')

        if path:
            with open(str(path[0]), 'w+', newline='') as stream:
                writer = csv.writer(stream)

                row_data = []

                for col in range(self.ui.tableWidget.columnCount()):
                    row_data.append(self.ui.tableWidget.horizontalHeaderItem(col).text())

                writer.writerow(row_data)

                for row in range(self.ui.tableWidget.rowCount()):
                    row_data = []

                    for col in range(self.ui.tableWidget.columnCount()):
                        item = self.ui.tableWidget.item(row, col)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')

                    writer.writerow(row_data)



