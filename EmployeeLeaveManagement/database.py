from PyQt5 import QtSql
from PyQt5.QtSql import *
from Employee_Add_Info import Employee_Add_Info

class Database:
    is_instantiated = False

    def __init__(self):
        if not Database.is_instantiated:
            #print("Database has been instatiated!")
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName("database/database.db")
            self.db.open()
            Database.is_instantiated = True

        else:
            print("Has already been created")

    def get_employee_info(self, conditionList):

        query = QSqlQuery()

        query_string = """SELECT Employee.personal_id as "Personal ID", Employee.first_name as "First Name",
        Employee.last_name as "Last Name", Employee.department_name as "Department Name",
        Employee.position as "Position"
        FROM Employee  where personal_id = personal_id"""

        condition = ""

        list_len = len(conditionList)

        for i in range(list_len - 1):
            condition +=conditionList[i][0]
            condition += "="
            condition += conditionList[i][1]
            condition += " and "

        if list_len > 0 :
            condition += conditionList [list_len - 1][0]
            condition += "="
            condition += conditionList [list_len - 1][1]

        if condition:
            query_string+= " and " + condition

        print(query_string)

        res = query.exec(query_string)

        record = query.record()
        column_number = record.count()

        header_list = []

        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sublist = []

            for i in range(column_number):
                sublist.append(query.value(i))

            result_list.append(sublist)


        return [header_list,result_list]


    def get_employee_leave_info(self,personal_id):


        query = QSqlQuery()

        queryString = """SELECT Employee.personal_id as "Personal ID",
        Employee_Leave_Log.date as "Date", Employee_Leave_Log.leave_start as "Start",
        Employee_Leave_Log.leave_end as "End", Employee_Leave_Log.leave_period as "Period",
        Employee_Leave_Log.excuse as "Excuse"
        from Employee, Employee_Leave_Log
        where Employee.personal_id = Employee_Leave_Log.employee_id and Employee.personal_id = :personal_id"""

        query.prepare(queryString)
        query.bindValue(":personal_id",personal_id)
        query.exec()

        record = query.record()
        column_number = record.count()

        header_list = []

        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sublist = []

            for i in range(column_number):
                sublist.append(query.value(i))

            result_list.append(sublist)

        return [header_list,result_list]


    def add_new_employee(self,Employee_Add_Info):

        query = QSqlQuery()

        query.prepare("""insert into Employee(first_name, last_name, personal_id, department_name, position)
        values(:first_name, :last_name, :personal_id, :department_name, :position)""")

        query.bindValue(":first_name", Employee_Add_Info.first_name)
        query.bindValue(":last_name", Employee_Add_Info.last_name)
        query.bindValue(":personal_id", Employee_Add_Info.personal_id)
        query.bindValue(":department_name", Employee_Add_Info.department_name)
        query.bindValue(":position", Employee_Add_Info.position)

        query.exec()


    def add_new_leave(self,employee_leave_info):

        query = QSqlQuery()

        query.prepare("""insert into Employee_Leave_Log(employee_id, date, leave_start, leave_end, leave_period, excuse)
        values(:employee_id, :date, :leave_start, :leave_end, :leave_period, :excuse)""")

        query.bindValue(":employee_id", employee_leave_info.employee_id)
        query.bindValue(":date", employee_leave_info.date)
        query.bindValue(":leave_start", employee_leave_info.leave_start)
        query.bindValue(":leave_end", employee_leave_info.leave_end)
        query.bindValue(":leave_period", employee_leave_info.leave_period)
        query.bindValue(":excuse", employee_leave_info.excuse)

        query.exec()


    def delete_employee(self,personal_id):

        query = QSqlQuery()

        query.prepare("delete from Employee where personal_id = :personal_id")
        query.bindValue(":personal_id", personal_id)
        query.exec()

        query.prepare("delete from Employee_Leave_Log where employee_id = :personal_id")
        query.bindValue(":personal_id", personal_id)
        query.exec()


    def get_leave_statistic_employee(self):

        query = QSqlQuery()

        result_list = []

        result = query.exec("""Select employee_id, sum(leave_period)
                                from Employee_Leave_Log
                                where Employee_Leave_Log.employee_id = Employee_Leave_Log.employee_id
                                GROUP BY Employee_Leave_Log.employee_id ORDER BY sum(leave_period) DESC """)

        record = query.record()

        column_number = record.count()
        name_list = []

        for i in range(column_number):
            name_list.append(record.field(i).name())

        limit = 0

        while query.next():
            sublist = []

            for i in range(column_number):
                sublist.append(query.value(i))

            if limit == 5:
                break

            limit = limit + 1
            print(result_list)

            result_list.append(sublist)


        return [name_list, result_list]

    def get_total_department_employee_leave(self):

        query = QSqlQuery()

        query.exec("""select e.department_name, sum(l.leave_period)
        from Employee_Leave_Log l, Employee e
        where l.employee_id = e.personal_id GROUP BY e.department_name
        ORDER BY sum(leave_period) DESC """)


        record = query.record()
        column_number = record.count()
        list = []

        while query.next():
            sublist = []

            for i in range(column_number):
                sublist.append(query.value(i))

            list.append(sublist)

        return list







