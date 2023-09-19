from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, String, Integer, Date
from dateutil import parser
from tkinter import messagebox

Base = declarative_base()


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    phone = Column(Integer)

    def __repr__(self):
        return f"Customers(Customer id:{self.id}    Customer Email{self.email}    Customer Phone Number{self.phone})"

    def convert_to_tuple(self):
        return self.id, self.email, self.phone

    def valid(self):
        return self.email != "deleted"

    @staticmethod
    def convert_from_tuple(tuple_):
        customers = Customers(id=tuple_[0], email=tuple_[1], phone=tuple_[2])
        return customers


class Journeys(Base):
    __tablename__ = "journeys"
    id = Column(Integer, primary_key=True)
    route = Column(String)
    date = Column(Date)
    max_capacity = Column(Integer)

    def __repr__(self):
        return f"Journeys(Journey id:{self.id}    Journey route:{self.route}    Journey date:{self.route}    Max-capacity:{self.max_capacity})"

    def convert_to_tuple(self):
        return self.id, self.route, self.date, self.max_capacity

    def valid(self):
        try:
            value = int(self.max_capacity)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        try:
            if tuple_[0] != '':  # unnecessary precaution
                id_ = int(tuple_[0])
            else:
                id_ = 0
            route = tuple_[1]
            date = parser.parse(tuple_[2])
            max_capacity = int(tuple_[3])
            journey = Journeys(id=id_, route=route, date=date, max_capacity=max_capacity)
            return journey
        except:
            print("", "Entries could not be converted to journey!")
        # journeys = Journeys(id=tuple_[0], route=tuple_[1], date=tuple_[2], max_capacity=tuple_[3])
        # return journeys


class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    journey_id = Column(Integer, ForeignKey("journeys.id"), nullable=False)
    # customer_id = Column(Integer, ForeignKey("customers.id"))
    # journey_id = Column(Integer, ForeignKey("journeys.id"))
    capacity = Column(Integer)

    def __repr__(self):
        return f"Bookings(Booking id:{self.id}    Customer id:{self.customer_id}    Journey id:{self.journey_id}    Capacity filled:{self.capacity})"

    def convert_to_tuple(self):
        return self.id, self. customer_id, self.journey_id, self.capacity

    def valid(self):
        try:
            value = int(self.capacity)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        bookings = Bookings(id=tuple_[0], customer_id=tuple_[1], journey_id=tuple_[2], capacity=tuple_[3])
        return bookings