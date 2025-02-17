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

def verifica_quadrato_magico(matrice):
    """Verifica se la matrice è un quadrato magico."""
    row_result = []
    counter = 0
    for riga in matrice:
        for elemento in riga:
            counter += elemento
        row_result.append(counter)
        counter = 0
    for i in range(len(row_result)):
        if row_result[i]!= row_result[0]:
            return False
    return True

def stampa_matrice(matrice, costante_magica=None):
    """Stampa la matrice in un formato leggibile, aggiungendo la costante se è  disponibile."""
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j])
        print("\n")

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
    return f"{matrice} è un quadrato perfetto"

if __name__ == "__main__":
    print(main())
