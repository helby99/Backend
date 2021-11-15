daftar_makanan = ["Bakso","Mie ayam","Sate"]
daftar_minuman = ["Es Teh","Es Jeruk","Es Kelapa"]
daftar_snack = ["Ring Onion","Kentang Goreng","Tahu Walik"]
keranjang = []

while True:

    def daftar_menu():
        print("---Daftar Menu---")
        print("-----------------")
        print(" 1. | Makanan  | ")
        print(" 2. | Minuman  | ")
        print(" 3. | Snack    | ")
        print("-----------------")
        menu = int(input("Pilih pesanan anda : "))
        if menu == 1:
            isi_makanan()
        elif menu == 2:
            isi_minuman()
        elif menu == 3:
            isi_snack()
        else:
            print("Pilihan menu tidak ditemukan ")

    def isi_makanan():
        print("---Daftar Makanan---")
        for isi_makanan in range(0, len(daftar_makanan)):
                print(f"{isi_makanan +1}  {daftar_makanan[isi_makanan]}")
        print("--------------------")
        makanan = int(input("Pilih makanan yang ingin dipesan. [1/2/3] "))
        if makanan == 1:
            print(" | Bakso   | 1x")
            keranjang.append(daftar_makanan[0])
        elif makanan == 2:
            print(" | Mie Ayam   | 1x")
            keranjang.append(daftar_makanan[1])
        elif makanan == 3:
            print(" | Sate   | 1x")
            keranjang.append(daftar_makanan[2])
        tanya()

    def isi_minuman():
        print("---Daftar  Minuman---")
        for isi_minuman in range(0, len(daftar_makanan)):
                print(f"{isi_minuman +1}  {daftar_minuman[isi_minuman]}")
        print("--------------------")
        minuman = int(input("Pilih minuman yang ingin dipesan. [1/2/3] "))
        if minuman == 1:
            print(" | Es teh   | 1x")
            keranjang.append(daftar_minuman[0])
        elif minuman == 2:
            print(" | Es jeruk   | 1x")
            keranjang.append(daftar_minuman[1])
        elif minuman == 3:
            print(" | Es kelapa   | 1x")
            keranjang.append(daftar_minuman[2])
        tanya()
        
    def isi_snack():
        print("---Daftar Snack---")
        for isi_snack in range(0, len(daftar_snack)):
                print(f"{isi_snack +1}  {daftar_snack[isi_snack]}")
        print("------------------")
        snack = int(input("Pilih snack yang ingin dipesan. [1/2/3] "))
        if snack == 1:
            print(" | Kentang goreng   | 1x")
            keranjang.append(daftar_snack[0])
        elif snack == 2:
            print(" | Onion ring   | 1x")
            keranjang.append(daftar_snack[1])
        elif snack == 3:
            print(" | Tahu walik   | 1x")
            keranjang.append(daftar_snack[2])
        tanya()

    def tanya():
        T = ""
        while T != "y":
            T = input("Apakah anda ingin membeli lagi? [y/n] ")
            selesai()
            continue

    def selesai():
        print("====Daftar Pesanan Anda====")
        for isi_keranjang in range(0, len(keranjang)):
            print(f"{isi_keranjang +1}  {keranjang[isi_keranjang]} | 1x")
        print("---------------------------")
        print("Terimakasih pesanan anda akan segera diantar")
        print("---------------------------")

    daftar_menu()