import datetime
from attraction import Attraction
from tourist import Tourist
from visit import Visit
from sqlalchemy import text
from touristRepository import TouristRepository
from db_cofig import local_session, create_all_entities


def main():
    create_all_entities()
    repo = TouristRepository(local_session)
    # tourist1 = Tourist(name='Daniel Marmor', origin_country='Israel')
    # tourist2 = Tourist(name='David Jones', origin_country='United Kingdom')
    #
    # repo.add(tourist1)
    # repo.add(tourist2)
    #
    # attr1 = Attraction(name='Coloseum', price=75.5)
    # attr2 = Attraction(name='St Pietrus Basilica', price=110)
    # attr3 = Attraction(name='Vila Borgeza', price=62)
    # attr4 = Attraction(name='Piazza Vernecia', price=14)
    #
    # repo.add(attr1)
    # repo.add(attr2)
    # repo.add(attr3)
    # repo.add(attr4)
    #
    # visit1_1 = Visit(attraction_id=attr1.id, tourist_id=tourist1.id, year_of_visit=2004)
    # visit1_3 = Visit(attraction_id=attr3.id, tourist_id=tourist1.id, year_of_visit=2010)
    # visit1_4 = Visit(attraction_id=attr4.id, tourist_id=tourist1.id, year_of_visit=2015)
    # visit2_1 = Visit(attraction_id=attr1.id, tourist_id=tourist2.id, year_of_visit=2016)
    # visit2_3 = Visit(attraction_id=attr3.id, tourist_id=tourist2.id, year_of_visit=2017)
    #
    # repo.add(visit1_1)
    # repo.add(visit1_3)
    # repo.add(visit1_4)
    # repo.add(visit2_1)
    # repo.add(visit2_3)
    #
    # local_session.commit()

    tourist_number1 = repo.get_by_column_value(Tourist, 'id', 1)
    tourist_visits = tourist_number1[0].visits;
    print(tourist_visits)

    attr_number1 = repo.get_by_column_value(Attraction, 'id', 1)
    attr_visits = attr_number1[0].visits
    print(tourist_visits)


main()
