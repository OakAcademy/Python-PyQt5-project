from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import *
from PyQt5.QtWidgets import *
from database import Database


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(555, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(353, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 20)
        self.gridLayout_2.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.first_layout =QGridLayout(self.widget)
        self.second_layout = QGridLayout(self.widget_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back"))


class ChartWindow(QtWidgets.QMainWindow):
            def __init__(self, mainMenu):
               super(ChartWindow, self).__init__()

               self.mainMenu = mainMenu
               self.ui = Ui_MainWindow()
               self.ui.setupUi(self)

               self.ui.pushButton.clicked.connect(self.back_button_clicked)

               self.first_chart = QChart()
               self.second_chart = QChart()
               self.first_series = QBarSeries()
               self.second_series = QPieSeries()
               self.load_first_series()
               self.load_second_series()

               self.first_chart.addSeries(self.first_series)
               self.first_chart.setTitle("Total Leave - Employee")


               self.second_chart.addSeries(self.second_series)
               self.second_chart.setTitle("Total Leave - Department")


               self.first_chart_view = QChartView(self.first_chart)
               self.first_chart_view.setRenderHint(QtGui.QPainter.Antialiasing)

               self.second_chart_view = QChartView(self.second_chart)
               self.second_chart_view.setRenderHint(QtGui.QPainter.Antialiasing)

               self.ui.first_layout.addWidget(self.first_chart_view)
               self.ui.second_layout.addWidget(self.second_chart_view)



            def load_first_series(self):
                self.database = Database()

                result_list = self.database.get_leave_statistic_employee()

                employee_one = result_list[1][0][0]
                value_one = result_list[1][0][1]

                employee_two = result_list[1][1][0]
                value_two = result_list[1][1][1]

                employee_three = result_list[1][2][0]
                value_three = result_list[1][2][1]

                employee_four = result_list[1][3][0]
                value_four = result_list[1][3][1]

                employee_five = result_list[1][4][0]
                value_five = result_list[1][4][1]

                first_bar = QBarSet(str(employee_one))
                second_bar = QBarSet(str(employee_two))
                third_bar = QBarSet(str(employee_three))
                fourth_bar = QBarSet(str(employee_four))
                fifth_bar = QBarSet(str(employee_five))

                first_bar << value_one
                second_bar << value_two
                third_bar << value_three
                fourth_bar << value_four
                fifth_bar << value_five

                self.first_series.append(first_bar)
                self.first_series.append(second_bar)
                self.first_series.append(third_bar)
                self.first_series.append(fourth_bar)
                self.first_series.append(fifth_bar)



            def load_second_series(self):
                result_list = self.database.get_total_department_employee_leave()
                for entry in result_list:
                    self.second_series.append(entry[0],entry[1])



            def back_button_clicked(self):
                self.hide()
                self.mainMenu.show()




