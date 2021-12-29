import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy import asc, text, desc, delete, update


class TouristRepository:
    def __init__(self, local_session):
        self.local_session = local_session

    def get_all(self, table_class):
        all_entries = self.local_session.query(table_class).all()
        return all_entries

    def get_all_limit(self, table_class, limit):
        all_entries_limit = self.local_session.query(table_class, limit).all()
        return all_entries_limit

    def get_all_order_by(self, table_class, column_name, direction=asc):
        all_entries_ordered = self.local_session.query(table_class).order_by(direction(column_name)).all()
        return all_entries_ordered

    def add(self, new_entry):
        self.local_session.add(new_entry)
        self.local_session.commit()

    def add_all(self, new_entries):
        self.local_session.add_all(new_entries)
        self.local_session.commit()

    # added by me
    def add_with_vaild(self, table_class, new_entry, unique_columns_names):
        check_unique_valid = self.check_unique_const_valid(table_class, new_entry, unique_columns_names)
        if not check_unique_valid:
            raise Exception("Unique values allready exists!")
        self.local_session.add(new_entry)
        self.local_session.commit()

    def delete_by_id(self, table_class, id_column_name, object_id):
        entries_for_delete = self.local_session.query(table_class)\
            .filter(getattr(table_class, id_column_name) == object_id)
        # CHECK IF EXISTS
        entries_size = len(entries_for_delete.all())
        if entries_size == 0:
            raise Exception(f'Entry With {id_column_name} = {object_id} in table {table_class}'
                  f' - does not exists. changed not commited!')
        # EXISTS - DELETE
        entries_for_delete.delete(synchronize_session=False)

        delete(table_class)
        self.local_session.commit()

    def update_by_id(self, table_class, id_column_name, object_id, data):
        entries_for_update = self.local_session.query(table_class)\
            .filter(getattr(table_class, id_column_name) == object_id)
        # CHECK IF EXISTS
        entries_size = len(entries_for_update.all())
        if entries_size == 0:
            raise Exception(f'Entry With {id_column_name} = {object_id} in table {table_class}'
                  f' - does not exists. changed not commited!')
        # EXISTS - UPDATE
        entries_for_update.update(data)
        self.local_session.commit()

    def get_by_column_value(self, table_class, column_name, value):
        entries = self.local_session.query(table_class).filter(getattr(table_class, column_name) == value).all()
        return entries

    # added by me !
    def get_by_columns_values(self, table_class, filters: dict):
        query = self.local_session.query(table_class)
        counter = len(query.all())
        for attr, value in filters.items():
            query = query.filter(getattr(table_class, attr) == value)
            counter = len(query.all())
        entries = query.all()
        return entries

    def get_by_column_like(self, table_class, column_name, value):
        search = '%{}%'.format(value)
        entries = self.local_session.query(table_class).filter(getattr(table_class, column_name).like(search)).all()
        return entries

    def check_unique_const_valid(self, table_class, new_entity, unique_columns_names):
        for unique in unique_columns_names:
            new_entity_attr = getattr(new_entity, unique)
            query = self.local_session.query(table_class).filter(getattr(table_class, unique) == new_entity_attr).all()
            if len(query) > 0:
                return False
        return True


