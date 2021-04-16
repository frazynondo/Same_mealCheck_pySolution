from abc import ABCMeta, abstractmethod


class Int_Builder(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def change_mealName():
        pass

    @staticmethod
    @abstractmethod
    def get_mealName():
        pass

    @staticmethod
    @abstractmethod
    def get_recipes():
        pass

    @staticmethod
    @abstractmethod
    def add_recipe():
        pass



