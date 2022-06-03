from PyQt5 import QtCore, QtGui, QtWidgets
from manageemployee import EmployeeWindow
from Charts import ChartWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 335)
        MainWindow.setMinimumSize(QtCore.QSize(250, 200))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(9, 9, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 87, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.ManageEmployeeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ManageEmployeeButton.setMinimumSize(QtCore.QSize(200, 60))
        self.ManageEmployeeButton.setObjectName("ManageEmployeeButton")
        self.gridLayout.addWidget(self.ManageEmployeeButton, 1, 0, 1, 1)
        self.ViewChartsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ViewChartsButton.setMinimumSize(QtCore.QSize(200, 60))
        self.ViewChartsButton.setObjectName("ViewChartsButton")
        self.gridLayout.addWidget(self.ViewChartsButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 86, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.ManageEmployeeButton.setText(_translate("MainWindow", "Manage Employees"))
        self.ViewChartsButton.setText(_translate("MainWindow", "View Charts"))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ManageEmployeeButton.clicked.connect(self.manage_employees_button_clicked)
        self.ui.ViewChartsButton.clicked.connect(self.view_charts_button_clicked)


    def manage_employees_button_clicked(self):
        self.hide()
        self.employeeWindow = EmployeeWindow(self)
        self.employeeWindow.show()

    def view_charts_button_clicked(self):
        self.hide()

        self.chartWindow = ChartWindow(self)
        self.chartWindow.show()









