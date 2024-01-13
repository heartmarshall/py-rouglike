from abc import ABC, abstractmethod


class MapBuilder(ABC):

    @abstractmethod
    def init_map(self):
        pass
    
    @abstractmethod
    def generate_terrain(self):
        pass

    @abstractmethod
    def generate_bioms(self):
        pass


class MapBuildDirector:
    def __init__(self, builder: MapBuilder):
        self.builder = builder

    def construct_map(self):
        self.builder.init_map()
        self.builder.generate_bioms()
        self.builder.generate_terrain()

    def get_map(self):
        return self.builder.map