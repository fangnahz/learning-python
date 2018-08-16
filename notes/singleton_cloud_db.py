# Consistency across operations in the database:
#   no operation should result in conflicts with others
# Memory and CPU utilization should be optimal for the handling of multiple operations on the DB
# Using singleton, there is only one object, calls to the database are synchronized,
#   this is inexpensive on system resources
# But, when have many apps but only one DB,
#   singleton is not a good choice,
#   because multiple singletons are created,
#   which leads to unsynchronized DB operations, and is heavy on resources.
#   In such cases, database connection pooling is better
import sqlite3


class MetaSigleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSigleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

if __name__ == '__main__':
    db1 = Database().connect()
    db2 = Database().connect()
    assert db1 is db2
    print("Database object DB1", db1)
    print("Database object DB2", db2)
