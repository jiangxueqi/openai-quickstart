from domain.sale_robot.sale_robot import SaleRobot
from infrastructure.utils.object_repository import ObjectRepository


class SaleRobotFactory(object):

    @staticmethod
    def create(similarity_score_threshold=0.8, temperature=0):
        sale_robot = ObjectRepository().find("sale_robot")
        if not sale_robot:
            sale_robot = SaleRobot(similarity_score_threshold, temperature)
            ObjectRepository().add("sale_robot", sale_robot)
        return sale_robot
