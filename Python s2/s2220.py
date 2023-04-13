from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine, select

Database = 'sqlite:///../data/my_first_sql_database.db'
Base = declarative_base()


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Person({self.id=} {self.name=} {self.age=})"


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

print(select_all(Person))
