from chess import Pawn, Bishop, Rook, Queen, King

# TESTY VYGENEROVANE GEMINI AI

# ==========================================
# 1. TESTY PRO PAWN
# ==========================================
print("--- PAWN TESTS ---")
pawn1 = Pawn("white", (2, 4))  # Základní pozice bílého pěšce (může o 1 nebo 2 pole vpřed)
print(pawn1)
print(pawn1.possible_moves())
print("Očekávané výsledky jsou: [(3, 4), (4, 4)]\n")

pawn2 = Pawn("black", (7, 4))  # Základní pozice černého pěšce (pohybuje se dolů)
print(pawn2)
print(pawn2.possible_moves())
print("Očekávané výsledky jsou: [(6, 4), (5, 4)]\n")

pawn3 = Pawn("white", (4, 4))  # Uprostřed desky (už jen o 1 pole vpřed)
print(pawn3)
print(pawn3.possible_moves())
print("Očekávané výsledky jsou: [(5, 4)]\n")

pawn4 = Pawn("white", (8, 1))  # Na konci desky (žádný tah vpřed)
print(pawn4)
print(pawn4.possible_moves())
print("Očekávané výsledky jsou: []\n")


# ==========================================
# 2. TESTY PRO BISHOP
# ==========================================
print("--- BISHOP TESTS ---")
bishop1 = Bishop("white", (4, 4))  # Uprostřed desky (všechny 4 diagonály)
print(bishop1)
print(bishop1.possible_moves())
print("Očekávané výsledky jsou: [(1, 1), (1, 7), (2, 2), (2, 6), (3, 3), (3, 5), (5, 3), (5, 5), (6, 2), (6, 6), (7, 1), (7, 7), (8, 8)]\n")

bishop2 = Bishop("black", (1, 1))  # Levý dolní roh (pouze jedna diagonála)
print(bishop2)
print(bishop2.possible_moves())
print("Očekávané výsledky jsou: [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]\n")


# ==========================================
# 3. TESTY PRO ROOK
# ==========================================
print("--- ROOK TESTS ---")
rook1 = Rook("white", (4, 4))  # Uprostřed desky (4 směry do kříže)
print(rook1)
print(rook1.possible_moves())
print("Očekávané výsledky jsou: [(1, 4), (2, 4), (3, 4), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 4), (6, 4), (7, 4), (8, 4)]\n")

rook2 = Rook("black", (1, 1))  # Levý dolní roh (jen doprava a nahoru)
print(rook2)
print(rook2.possible_moves())
print("Očekávané výsledky jsou: [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]\n")


# ==========================================
# 4. TESTY PRO QUEEN
# ==========================================
print("--- QUEEN TESTS ---")
queen1 = Queen("white", (4, 4))  # Uprostřed desky (kombinace věže a střelce)
print(queen1)
print(queen1.possible_moves())
print("Očekávané výsledky jsou: [(1, 1), (1, 4), (1, 7), (2, 2), (2, 4), (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (5, 3), (5, 4), (5, 5), (6, 2), (6, 4), (6, 6), (7, 1), (7, 4), (7, 7), (8, 4), (8, 8)]\n")

queen2 = Queen("black", (1, 1))  # Levý dolní roh
print(queen2)
print(queen2.possible_moves())
print("Očekávané výsledky jsou: [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 1), (2, 2), (3, 1), (3, 3), (4, 1), (4, 4), (5, 1), (5, 5), (6, 1), (6, 6), (7, 1), (7, 7), (8, 1), (8, 8)]\n")


# ==========================================
# 5. TESTY PRO KING
# ==========================================
print("--- KING TESTS ---")
king1 = King("white", (4, 4))  # Uprostřed desky (všech 8 okolních polí)
print(king1)
print(king1.possible_moves())
print("Očekávané výsledky jsou: [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]\n")

king2 = King("black", (1, 1))  # Levý dolní roh (pouze 3 sousední pole)
print(king2)
print(king2.possible_moves())
print("Očekávané výsledky jsou: [(1, 2), (2, 1), (2, 2)]\n")

king3 = King("white", (4, 8))  # Horní okraj šachovnice (5 polí)
print(king3)
print(king3.possible_moves())
print("Očekávané výsledky jsou: [(3, 7), (3, 8), (4, 7), (5, 7), (5, 8)]\n")