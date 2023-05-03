from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, Date
from dateutil import parser
from tkinter import messagebox

Base = declarative_base()


class Hold(Base): # Hold region klassen
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
        return f"id: {self.id}    Kapacitet: {self.kapacitet}    Sværhedsgrad: {self.sverhedsgrad}"

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
        bane = Bane(id=tuple_[0], kapacitet=tuple_[1], sverhedsgrad=tuple_[2])
        return bane


class Bookings(Base): # Bookings region klasse
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    dato = Column(Date)
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
        try:
            if tuple_[0] != '':
                id_ = int(tuple_[0])
            else:
                id_ = 0
            dato = parser.parse(tuple_[1])
            hold_id = int(tuple_[2])
            bane_id = int(tuple_[3])

            booking = Bookings(id=id_, dato=dato, hold_id=hold_id, bane_id=bane_id)
            return booking
        except:
            print("Entries kunne ikke blive konvateret til booking")
