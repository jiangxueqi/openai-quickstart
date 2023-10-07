from domain.vector_database.real_estate_db import RealEstateDB


class SaleRobot(object):
    def __init__(self):
        self.vector_db = RealEstateDB()