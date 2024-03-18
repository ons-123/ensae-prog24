from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    
    def get_solution(self):

        target_state = list(range(1, self.grid.size**2)) + [0]
        current_state = self.grid.grid[:]
        swap_sequence = []

        while current_state != target_state:
            for i in range(self.grid.size**2):
                if current_state[i] != target_state[i]:
                    zero_index = current_state.index(0)
                    swap_sequence.append((zero_index, i))
                    self.grid.swap(zero_index, i)
                    current_state = self.grid.grid[:]
                    break

        return swap_sequence
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
       """
       cette solution n'est pas optimale car sa complexite est de l'ordre de (taille de grid)
        au carre car il y a une boucle for et une boucle while
    """


