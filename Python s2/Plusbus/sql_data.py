from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from datetime import date
from data_lag import Kunder, Base
from data_lag import Rejser, Base

# add the following 7 lines to make foreign key constraints work  https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#sqlite-foreign-keys
from sqlalchemy.engine import Engine
from sqlalchemy import event
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Database = 'sqlite:///plusbus.db'  # first part: database type, second part: file path


def create_test_data():  # Optional. Used to test data base functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Kunder(email="test@mail.com", telefon=93949221))
        new_items.append(Kunder(email="test2@mail.com", telefon=62370000))
        a_date = date(day=10, month=12, year=2022)
        session.add_all(new_items)
        session.commit()


def select_all(classparam):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))  # very useful for converting into our data class
        result = []
        for record in records:
            # print(record)
            result.append(record)
    return result


def get_record(classparam, record_id):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return the record in classparams table with a certain id
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()  # very useful for converting into our data class
    return record


def create_record(record):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # create a record in the database
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()  # makes changes permanent in database


# region container
def update_container(kunder):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the container table
    with Session(engine) as session:
        session.execute(update(Kunder).where(Kunder.id == kunder.id).values(email=kunder.email, telefon=kunder.telefon))
        session.commit()  # makes changes permanent in database


def delete_hard_container(kunder):
    # delete a record in the container table
    with Session(engine) as session:
        session.execute(delete(Kunder).where(Kunder.id == kunder.id))
        session.commit()  # makes changes permanent in database


def delete_soft_container(kunder):
    # soft delete a record in the container table by setting its weight to -1 (see also method "valid" in the container class)
    with Session(engine) as session:
        session.execute(update(Kunder).where(Kunder.id == kunder.id).values(email='deleted', telefon=kunder.telefon))
        session.commit()  # makes changes permanent in database
# endregion container


# Rejser


def rejser_create_test_data():  # Optional. Used to test data base functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Rejser(route="test rute1", date="test dato1", seats="test seats"))
        new_items.append(Rejser(route="test rute2", date="test dato2", seats="test seats"))
        a_date = date(day=10, month=12, year=2022)
        session.add_all(new_items)
        session.commit()


def rejser_select_all(classparam):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))  # very useful for converting into our data class
        result = []
        for record in records:
            # print(record)
            result.append(record)
    return result


def rejser_get_record(classparam, record_id):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return the record in classparams table with a certain id
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()  # very useful for converting into our data class
    return record


def rejser_create_record(record):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # create a record in the database
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()  # makes changes permanent in database


# region container
def rejser_update_container(rejser):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the container table
    with Session(engine) as session:
        session.execute(update(Rejser).where(Rejser.id == rejser.id).values(route=rejser.email, date=rejser.date, seats=rejser.seats))
        session.commit()  # makes changes permanent in database


def rejser_delete_hard_container(rejser):
    # delete a record in the container table
    with Session(engine) as session:
        session.execute(delete(Rejser).where(Rejser.id == rejser.id))
        session.commit()  # makes changes permanent in database


def rejser_delete_soft_container(rejser):
    # soft delete a record in the container table by setting its weight to -1 (see also method "valid" in the container class)
    with Session(engine) as session:
        session.execute(update(Rejser).where(Rejser.id == rejser.id).values(route='deleted', date=rejser.date, seats=rejser.seats))
        session.commit()  # makes changes permanent in database
# endregion Rejser


if __name__ == "__main__":  # Executed when invoked directly
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)
    create_test_data()
    print(select_all(Kunder))
    print(get_record(Kunder, 2))
    rejser_create_test_data()
    print(rejser_select_all(Rejser))
    print(rejser_get_record(Rejser, 2))
    # insert_example(engine)
    # select_text(engine)
else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)