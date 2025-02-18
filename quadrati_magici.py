import random

def genera_matrice(n: int, valid_numbers: list):
    """Genera una matrice n x n con numeri casuali."""
    matrice = []
    avalaible_numbers = valid_numbers [:] # Per creare una copia della lista in modo che non venga modificata la lista originale
    for _ in range(n):
        row = []
        for _ in range(n):
            num = random.choice(avalaible_numbers)
            row.append(num)
            avalaible_numbers.remove(num)
        matrice.append(row)
    return matrice

def verifica_quadrato_magico(matrice: list[list[int]]):
    """Verifica se la matrice è un quadrato magico."""
    for i in range(len(matrice)):
        if sum(matrice[i])!= sum(matrice[0]):
            return False
    for col in range(len(matrice)):
        col_result = 0
        for row in matrice:
            col_result += row[col]
        if col_result!= sum(matrice[0]):
            return False
    primary_diag_result = 0
    secondary_diag_result = 0
    for i in range(len(matrice)):
        primary_diag_result += matrice[i][i]
        secondary_diag_result += matrice[i][len(matrice) - 1 - i]
    if primary_diag_result!= sum(matrice[0]) or secondary_diag_result != sum(matrice[0]):
        return False
    return True

def stampa_matrice(matrice: list[list[int]]):
    """Stampa la matrice in un formato leggibile, aggiungendo la costante se è  disponibile."""
    for i in range(len(matrice)):
        print(matrice[i])

def main():
    """Funzione principale che genera e verifica quadrati magici."""
    valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        matrice = genera_matrice(3, valid_numbers)
        verifica = verifica_quadrato_magico(matrice)
        if verifica == True:
            break
        else:
            continue
    print("Il quadrato magico generato è:")
    stampa_matrice(matrice)
    costante_magica = sum(matrice[0])
    print(f"La costante magica del quadrato è: {costante_magica}")

if __name__ == "__main__":
    main()
