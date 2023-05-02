from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, Date
from dateutil import parser
from tkinter import messagebox

Base = declarative_base()


class Hold(Base):
    __tablename__ = "hold"
    id = Column(Integer, primary_key=True)
    erfaring = Column(Integer)
    storelse = Column(Integer)

    def __repr__(self):
        return f"id:{self.id}    erfaring{self.erfaring}    størelse{self.storelse}"

    def convert_to_tuple(self):
        return self.id, self.erfaring, self.storelse

    def valid(self):
        return self.erfaring != "deleted"

    @staticmethod
    def convert_from_tuple(tuple_):
        hold = Hold(id=tuple_[0], erfaring=tuple_[1], storelse=tuple_[2])
        return hold


class Bane(Base):
    __tablename__ = "bane"
    id = Column(Integer, primary_key=True)
    kapacitet = Column(Integer)
    sverhedsgrad = Column(Integer)

    def __repr__(self):
        return f"id:{self.id}    kapacitet{self.kapacitet}    sværhedsgrad{self.sverhedsgrad}"

    def convert_to_tuple(self):
        return self.id, self.kapacitet, self.sverhedsgrad

    def valid(self):
        try:
            value = int(self.kapacitet)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        try:
            if tuple_[0] != '':
                id_ = int(tuple_[0])
            else:
                id_ = 0
            kapacitet = int(tuple_[1])
            sverhedsgrad = int(tuple_[2])
            bane = Bane(id=id_, sverhedsgrad=sverhedsgrad, kapacitet=kapacitet)
        except:
            print("", "Entries kunne ikke blive konvateret til bane")


class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    dato = Column(String)
    hold_id = Column(Integer, ForeignKey("hold.id"), nullable=False)
    bane_id = Column(Integer, ForeignKey("bane.id"), nullable=False)

    def __repr__(self):
        return f"Bookings( id{self.id}    dato:{self.dato}    hold id:{self.hold_id}    bane id:{self.bane_id}"

    def convert_to_tuple(self):
        return self.id, self.dato, self.hold_id, self.bane_id

    def valid(self):
        try:
            value = int(self.bane_id)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        bookings = Bookings(id=tuple_[0], dato=tuple_[1], hold_id=tuple_[2], bane_id=tuple_[3])
        return bookings
