from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine, select

Database = 'sqlite:///../data/my_one_database.db'
Base = declarative_base()


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Person({self.id=} {self.name=} {self.age=})"

    def convert_to_tuple(self):
        return self.id, self.name, self.age

    def valid(self):

        try:
            value = int(self.age)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):
        person = Person(id=tuple_[0], name=tuple_[1], age=tuple_[2])
        return person


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

print(Person.convert_from_tuple((12, "Lars", 16)))