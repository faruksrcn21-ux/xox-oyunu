import random 


tahta = [[" " for i in range(3)] for j in range(3)]

def tahtayi_yazdir():
    print("\n")
    for satir in tahta:
        print(" | ".join(satir))
        print("-" * 9)

def kazanan_var_mi():
    for i in range(3):
        if tahta[i][0] == tahta[i][1] == tahta[i][2] != " ": return True
        if tahta[0][i] == tahta[1][i] == tahta[2][i] != " ": return True
    if tahta[0][0] == tahta[1][1] == tahta[2][2] != " ": return True
    if tahta[0][2] == tahta[1][1] == tahta[2][0] != " ": return True
    return False

def bos_kareler():
    kareler = []
    for r in range(3):
        for c in range(3):
            if tahta[r][c] == " ":
                kareler.append((r, c)) 
    return kareler

def bilgisayarin_hamlesi():

    for r, c in bos_kareler():
        tahta[r][c] = "O"
        if kazanan_var_mi():
            return
        tahta[r][c] = " "
    
    for r, c in bos_kareler():
        tahta[r][c] = "X"
        if kazanan_var_mi():
            tahta[r][c] = "O"
            return
        tahta[r][c] = " "
    
    if tahta[1][1] == " ":
        tahta[1][1] = "O"
        return
    
    koseler = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_koseler = [k for k in koseler if tahta[k[0]][k[1]] == " "]
    if available_koseler:
        r, c = random.choice(available_koseler)
        tahta[r][c] = "O"
        return
    
    r, c = random.choice(bos_kareler())
    tahta[r][c] = "O"

print("--- XOX: Bilgisayara Karşı ---")
print("Sen: X | Bilgisayar: O")

while True:
    tahtayi_yazdir()
    
    while True:
        try:
            satir = int(input("Satır (1,2,3): "))
            sutun = int(input("Sütun (1,2,3): "))
            if not (1 <= satir <= 3 and 1 <= sutun <= 3):
                print("Lütfen 1, 2 veya 3 girin.")
                continue
            if tahta[satir-1][sutun-1] == " ":
                tahta[satir-1][sutun-1] = "X"
                break
            else:
                print("Orası dolu!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    if kazanan_var_mi():
        tahtayi_yazdir()
        print("Tebrikler! Sen kazandın!")
        break
    
    if not bos_kareler():
        tahtayi_yazdir()
        print("Berabere!")
        break

    print("\nBilgisayar hamle yapıyor...")
    bilgisayarin_hamlesi()

    if kazanan_var_mi():
        tahtayi_yazdir()
        print("Bilgisayar kazandı! Daha çok çalışmalısın.")
        break