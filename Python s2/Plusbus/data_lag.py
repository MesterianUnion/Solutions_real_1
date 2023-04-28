from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date
from dateutil import parser  # install with "pip install python-dateutil"
from tkinter import messagebox

Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.


class Kunder(Base):
    __tablename__ = "kunder"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    telefon = Column(Integer)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Kunder({self.id=:4}    {self.email=:5}    {self.telefon=})"

    def convert_to_tuple(self):  # Convert Container to tuple
        return self.id, self.email, self.telefon

    def valid(self):
        return self.email != "deleted"

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Container
        kunder = Kunder(id=tuple_[0], email=tuple_[1], telefon=tuple_[2])
        return kunder


class Rejser(Base):
    __tablename__ = "rejser"
    id = Column(Integer, primary_key=True)
    route = Column(String)
    date = Column(String)
    seats = Column(String)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Rejser ({self.id=:4},   {self.route=:6},  {self.date=}, {self.seats=})"

    def rejser_convert_to_tuple(self):  # Convert aircraft to tuple
        return self.id, self.route, self.date, self.seats

    def valid(self):
        return self.route != "deleted"

    @staticmethod
    def rejser_convert_from_tuple(tuple_):  # Convert tuple to Container
        rejser = Rejser(id=tuple_[0], route=[1], date=tuple_[2], seats=tuple_[3])
        return rejser
