import sys
from PyQt5 import QtWidgets, QtCore
from mainmenu import MainWindow
from database import Database

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

    #database =Database()

    #print(database.get_employee_leave_info(1001)[0])
    #print(database.get_employee_leave_info(1001)[1])
    #print(database.get_employee_leave_info(1002)[0])
    #print(database.get_employee_leave_info(1002)[1])





