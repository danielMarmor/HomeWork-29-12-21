from sqlalchemy import Table, Column, BigInteger, String
from db_cofig import Base
from sqlalchemy.orm import relationship, backref


class Tourist(Base):
    __tablename__ = 'tourists'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    origin_country = Column(String(20), nullable=False)

    def __str__(self):
        return f'<Tourist> id:{self.id} name:{self.name}, origin_country:{self.origin_country}'

    def __repr__(self):
        return f'<Tourist> id:{self.id} name:{self.name}, origin_country:{self.origin_country}'
