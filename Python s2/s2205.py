from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine

Database = 'sqlite:///../data/my_sirst_sql_database.db'  # first part: database type, second part: file path
Base = declarative_base()


class Person(Base):
    # this class declaration does 2 important things at once:
    # 1. as usual, it declares a class we can store data in, inside our python program.
    # 2. it creates a table in a sql database with the specified columns
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


def create_test_data():  # Optional. Used to test data base functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Person(name="peter", age=48))
        new_items.append(Person(name="susan", age=19))
        new_items.append(Person(name="jane", age=21))
        new_items.append(Person(name="harry", age=20))
        session.add_all(new_items)
        session.commit()


# https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine.
# This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space
# called a connection pool for these database connections. The engine is typically a global object created just once for a particular
# database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
engine = create_engine(Database, echo=False, future=True)  # define engine
Base.metadata.create_all(engine)  # establish connection to database (and create if it does not exist yet)

create_test_data()