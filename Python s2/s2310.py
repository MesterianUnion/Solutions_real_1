from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select

Database = 'sqlite:///../data/my_second_sql_database.db'
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Customer({self.id=}    {self.name=}    {self.address=}    {self.age=})"


# def create_test_data():
#     with Session(engine) as session:
#         data = []
#         data.append(Customer(name="Lars", address="Rødvedvej 27, Holte", age=17))
#         data.append(Customer(name="Jabakl", address="Hatcha 24, Israel", age=47))
#         data.append(Customer(name="Peter", address="Me alle 2 7th, Korsør", age=1))
#         data.append(Customer(name="Peter", address="Vedbækstranvej 297, Vedbæk", age=18))
#         session.add_all(data)
#         session.commit()


class Product(Base):
    __tablename__ = "products2"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Integer)
    brand = Column(String)

    def __repr__(self):
        return f"Product({self.id=}    {self.product_number=}    {self.price=}    {self.brand=})"


def create_test_data():
    with Session(engine) as session:
        data = []
        data.append(Product(product_number=7, price=201, brand="idk"))
        data.append(Customer(name="Lars", address="Rødvedvej 27, Holte", age=17))
        # data.append(Product(2, 201, "idk"))
        # data.append(Customer(name="Jabakl", address="Hatcha 24, Israel", age=47))
        # data.append(Product(3, 201, "idk"))
        # data.append(Product(5, 201, "idk"))
        session.add_all(data)
        session.commit()


def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()
print(get_record(Customer, 1))
print(get_record(Product, 1))