# import numpy as np
import copy

RULE = (2, (3,), (2, 3))

NEIGHBOURHOOD = {(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]}

class Place():
    alive = set()
    region = set()
    next_gen = set()

    def __init__(self, coord, is_alive):
        assert type(coord) == tuple
        assert len(coord) == RULE[0]
        assert type(is_alive) == bool

        self.coord = coord
        self.is_alive = is_alive
        self.neighboursa = self.get_neighbours()
        if is_alive:
            Place.alive.add(coord)
            Place.region.add(self.neighbours)

    def get_neighbouring_coords(self):
        grid = copy.copy(NEIGHBOURHOOD)
        grid.difference_update({(0, 0)})
        neighbours = {(self.coord[0] + x, self.coord[1] + y) for x, y in grid}
        return neighbours

    def get_neighbours(self):

    def will_live(self):
        living_neighbours = Place.alive.intersection(self.neighbours)
        num_living_neighbours = len(living_neighbours)
        if self.is_alive and num_living_neighbours in RULE[2]:
            return True
        elif not self.is_alive and num_living_neighbours in RULE[1]:
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other, Place):
            raise ValueError(f"{other} is not an instance of Place")
        return self.coord == other.coord and self.is_alive == other.is_alive

    # @classmethod
    # def calc_next_gen(cls):
    #     new_alive = {point for point in }

def tuples_as_matrix(coords):
    max_x = max([coord[0] for coord in coords])
    min_x = min([coord[0] for coord in coords])
    max_y = max([coord[1] for coord in coords])
    min_y = min([coord[1] for coord in coords])

    x_dim = max_x - min_x
    y_dim = max_y - min_y
    return None


if __name__ == '__main__':
    # gol = world({(0, 0)})
    # print(gol.potentials)
    a_point = Point((0, 0))
    print(a_point.neighbours)