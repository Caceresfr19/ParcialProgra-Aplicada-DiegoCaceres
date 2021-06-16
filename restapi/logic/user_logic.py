from core.pyba_logic import PybaLogic


class UserLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getUserById(self, id):
        database = self.createDatabaseObj()
        sql = f"select * from user where id={id};"
        result = database.executeQuery(sql)
        return result

    def insertUser(self, user):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `world`.`user`"
            + f"(`id`,`user_name`,`user_email`,`password`,`salt`) "
            + f"VALUES(0, '{user['user_name']}', '{user['user_mail']}', "
            + f"{user['password']}, {user['salt']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateUser(self, id, user):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE `world`.`user` "<
            + f"SET `user_name` = '{user['user_name']}', `user_email` = '{user['user_email']}', "
            + f"`password` = {user['password']}, `salt` = {user['salt']} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteUser(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from user where id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows
