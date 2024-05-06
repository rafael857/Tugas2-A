def cetak_nilai_kuadrat(n):
    for i in range(n):
        print(i ** 2, end=" ")

while True:
    n_input = input("Masukkan nilai n, atau ketikkan 'berhenti' untuk keluar: ")
    if n_input.lower() == "berhenti":
        print("Terima kasih!")
        break
    else:
        try:
            n = int(n_input)
            if 1 <= n <= 20:
                print("Nilai i^2 untuk n =", n, "adalah:")
                cetak_nilai_kuadrat(n)
            else:
                print("Constraints tidak terpenuhi. Silakan masukkan nilai n antara 1 dan 20.")
        except ValueError:
            print("Masukan tidak valid. Silakan masukkan nilai n sebagai bilangan bulat.")

#