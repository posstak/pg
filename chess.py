from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        if (self.color == "black"): # snizovani radku pro cerne pesaky
            row, col = self.position
            if (row == 7):
                return sorted([(row - 1, col), ((row - 2), col)]) # prvni tah = 2 mozne skoky
            row -= 1
            if (self.is_position_on_board((row, col))):
                return [(row, col)]
        else:
            row, col = self.position
            if (row == 2):
                return sorted([(row + 1, col), ((row + 2), col)])
            row += 1
            if (self.is_position_on_board((row, col))):
                return [(row, col)]

        print(f"Pawn {self.position} has no possible moves.")
        return []
    
    def __str__(self):
        return f'Pawn ({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return sorted(final_moves)

    def __str__(self):
        return f'Knight ({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves:list[tuple] = []
        final_moves:list[tuple] = []
        for i in range(1, 9):
            moves.append((row + i, col + i))
            moves.append((row + i, col - i))
            moves.append((row - i, col + i))
            moves.append((row - i, col - i))
        for move in moves:
            if (self.is_position_on_board(move)):
                final_moves.append(move)

        return sorted(final_moves)

    def __str__(self):
        return f"Bishop ({self.color}) at position {self.position}"


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves:list[tuple] = []
        for i in range(1, 9):
            moves.append((i, col))
            moves.append((row, i))
        moves.remove(self.position) # 2x odstraneni hodnoty, na ktere figurka uz je (nevim jak jinak elegantneji to udelat 😄)
        moves.remove(self.position)

        return sorted(moves)

    def __str__(self):
        return f"Rook ({self.color}) at position {self.position}"


class Queen(Piece):
    def possible_moves(self):
        final_moves:list[tuple] = Rook.possible_moves(self) + Bishop.possible_moves(self)
        
        return sorted(final_moves)

    def __str__(self):
        return f"Queen ({self.color}) at position {self.position}"


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row, col + 1), (row, col - 1),
            (row + 1, col), (row - 1, col),
            (row + 1, col + 1), (row -1, col - 1),
            (row + 1, col - 1), (row -1, col + 1)]
        final_moves:list[tuple] = []
        for move in moves:
            if (self.is_position_on_board(move)):
                final_moves.append(move)

        return sorted(final_moves)

    def __str__(self):
        return f"King ({self.color}) at position {self.position}"


if __name__ == "__main__":
    try:
        print("Hra běží, ale nejsou v ní figurky :)\nSada testů v souboru chess_test.py")
    
    except Exception as e:
        print(f"Vyskytla se velice neočekávaná chyba:\n {e}")