from sqlalchemy import MetaData, Table, Column
from sqlalchemy.dialects import mysql

class Users:
    '''MySQL Model'''

    def __init__(self, metadata: MetaData) -> None:
        self.name = 'users'
        self.metadata = metadata

    def get_table(self) -> Table:
        return Table(self.name, self.metadata,
            Column('user_id', mysql.BIGINT(), primary_key=True),
            Column('status', mysql.VARCHAR(200))
        )
      