# import numpy as np
import copy
import itertools

RULE = (2, (3,), (2, 3))


class Life:
    def __init__(self, seed, rule=RULE):
        Life.verify_rule(rule)
        self.rule = tuple(rule)
        self.dim = self.rule[0]
        self.birthing_rule = self.rule[1]
        self.survival_rule = self.rule[2]

        self._neighbour_grid = set(itertools.product([-1, 0, 1], repeat=self.dim)).difference({(0,)*self.dim})

        self.living = set()
        self.nbd = set()
        self.add_lives(seed)

    def verify_tuple(self, life):
        if len(life) != self.dim:
            raise ValueError(f"This game has dimension {self.dim}. This tuple has length {len(life)}: {life}")

    def add_life(self, life):
        self.verify_tuple(life)
        self.living.add(life)

        neighbourhood = {tuple(sum(x) for x in zip(life, grid_item)) for grid_item in self._neighbour_grid}
        self.nbd.update(neighbourhood)

    def add_lives(self, lives):
        for life in lives:
            self.add_life(life)

    def living_neighbours(self, cell):
        cell_neighbours = {tuple(sum(x) for x in zip(cell, grid_item)) for grid_item in self._neighbour_grid}
        living_neighbours = cell_neighbours.intersection(self.living)
        return living_neighbours

    def will_live(self, cell):
        if cell not in self.nbd:
            return False
        elif cell not in self.living:
            num_living_nbs = len(self.living_neighbours(cell))
            return num_living_nbs in self.birthing_rule
        else:
            num_living_nbs = len(self.living_neighbours(cell))
            return num_living_nbs in self.survival_rule

    def __next__(self):
        new_living = {cell for cell in self.nbd if self.will_live(cell)}
        self.__init__(new_living, self.rule)
        # return Life(new_living, self.rule)

    @staticmethod
    def verify_rule(rule):
        tuple_rule = tuple(rule)
        if len(tuple_rule) != 3:
            error_msg = ("Rules must have 3 elements: \n"
                         "A dimension (int), a birth rule (list-like) and a survival rule (list-like)")
            raise ValueError(error_msg)


def tuples_as_matrix(coords):
    max_x = max([coord[0] for coord in coords])
    min_x = min([coord[0] for coord in coords])
    max_y = max([coord[1] for coord in coords])
    min_y = min([coord[1] for coord in coords])

    x_dim = max_x - min_x
    y_dim = max_y - min_y
    return None


if __name__ == '__main__':
    new_life = Life({(1, 1), (0, 1), (1, 0)})
    print(new_life.living_neighbours((0, 0)))
    next(new_life)
    print(new_life.living)

