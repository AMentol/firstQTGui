from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()
    
    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('tasks_db.db')
        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open DataBase!")
            return False
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS tasks (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), Name VARCHAR(20))")
        return True
        
    def execute_query_with_params(self, sql_query, query_values=None):
            query = QtSql.QSqlQuery()
            query.prepare(sql_query)
            
            if query_values is not None:
                for query_value in query_values:
                    query.addBindValue(query_value)
            
            query.exec()
            return query
            
    def add_new_task_query(self, date, name):
            sql_query = "INSERT INTO tasks (Date, Name) VALUES (?, ?)"
            self.execute_query_with_params(sql_query, [date, name])
            
    def delete_task_query(self, id):
            sql_query = "DELETE FROM tasks WHERE ID=?"
            self.execute_query_with_params(sql_query, [id])
        
        