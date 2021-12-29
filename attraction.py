from sqlalchemy import Table, Column, BigInteger, String, REAL
from db_cofig import Base
from sqlalchemy.orm import relationship, backref


class Attraction(Base):
    __tablename__ = 'atractions'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(REAL, nullable=False)

    def __str__(self):
        return f'<Attraction> id:{self.id} name:{self.name}, price:{self.price}'

    def __repr__(self):
        return f'<Attraction> id:{self.id} name:{self.name}, price:{self.price}'
