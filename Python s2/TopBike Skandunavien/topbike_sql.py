from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from datetime import date
from topbike_data import Hold, Bane, Bookings, Base

from sqlalchemy.engine import Engine
from sqlalchemy import event
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Database = 'sqlite:///topbikef.db'


def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Hold(erfaring=2, storelse=8))
        new_items.append(Hold(erfaring=1, storelse=6))
        new_items.append(Bane(kapacitet=12, sverhedsgrad=2))
        new_items.append(Bane(kapacitet=26, sverhedsgrad=1))
        a_date = date(day=10, month=12, year=2022)
        new_items.append(Bookings(Dato=a_date, hold_id=1, bane_id=2))
        a_date = date(day=30, month=4, year=2023)
        new_items.append(Bookings(Dato=a_date, hold_id=2, bane_id=1))
        session.add_all(new_items)
        session.commit()


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)

        return result


def get_record(classparam, record_id):
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


def create_record_hold(record):
    with Session(engine) as session:
        print(record)
        record.entry_hold_id = None
        session.add(record)
        try:
            session.commit()
        except:
            print("Der var en fejl, mens du lavede en optagelse/record [Fejl = Linje 49]")


def update_hold(hold):
    with Session(engine) as session:
        session.execute(update(Hold).where(Hold.id == hold.id).values(erfaring=hold.erfaring, storelse=hold.storelse))


def soft_delete_hold(hold):
    with Session(engine) as session:
        session.execute(update(Hold).where(Hold.id == hold.id).values(erfaring="deleted", storelse=hold.storelse))
        session.commit()


#Bane
def create_record_bane(record):
    with Session(engine) as session:
        print(record)
        record.entry_bane_id = None
        print(record)
        session.add(record)
        try:
            session.commit()
        except:
            print("Der var en fejl, mens du lavede en optagelse/record [Fejl = linje 72]")


def update_bane(bane):
    with Session(engine) as session:
        session.execute(update(Bane).where(Bane.id == bane.id).values(kapacitet=bane.kapacitet, sverhedsgrad=bane.sverhedsgrad))
        session.commit()


def soft_delete_bane(bane):
    with Session(engine) as session:
        session.execute(update(Bane).where(Bane.id == bane.id).values(kapacitet=-1, sverhedsgrad=bane.sverhedsgrad))
        session.commit()


#Bookings
def update_bookings(booking):
    with Session(engine) as session:
        session.execute(update(Bookings).where(Bookings.id == booking.id).values(dato=booking.dato, hold_id=booking.hold_id, bane_id=booking.bane.id))
        session.commit()


def hard_delete_bookings(booking):
    with Session(engine) as session:
        session.execute(delete(Bookings).where(Bookings.id == booking.id))
        session.commit()

if __name__ == "__main__":
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    print(get_record(Hold, 1))
    print(get_record(Bane, 2))
    print(get_record(Bookings, 2))
    print(select_all(Hold))

else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)