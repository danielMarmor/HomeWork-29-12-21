from sqlalchemy import Table, Column, BigInteger, String, ForeignKey
from db_cofig import Base
from sqlalchemy.orm import relationship, backref



class Visit(Base):
    __tablename__ = 'visits'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    attraction_id = Column(BigInteger, ForeignKey('atractions.id'), nullable=False)
    tourist_id = Column(BigInteger, ForeignKey('tourists.id'), nullable=False)
    year_of_visit = Column(BigInteger, nullable=False)

    attraction = relationship('Attraction', backref=backref('visits', uselist=True))
    tourist = relationship('Tourist', backref=backref('visits', uselist=True))

    def __str__(self):
        return f'<Visit> id:{self.id} attraction_id:{self.attraction_id}, tourist_id:{self.tourist_id}' \
               f'year_of_visit:{self.year_of_visit}'

    def __repr__(self):
        return f'<Visit> id:{self.id} attraction_id:{self.attraction_id}, tourist_id:{self.tourist_id}' \
               f'year_of_visit:{self.year_of_visit}'
