import multiprocessing
import random

def hitung_baris(args):
    baris, B = args
    hasil = []
    for kolom in zip(*B):
        total = 0
        for a, b in zip(baris, kolom):
            total += a * b
        hasil.append(total)
    return hasil

if __name__ == "__main__":
    ukuran = 3

    A = [[random.randint(1, 9) for _ in range(ukuran)] for _ in range(ukuran)]
    B = [[random.randint(1, 9) for _ in range(ukuran)] for _ in range(ukuran)]

    print("Matrix A:")
    for i in A:
        print(i)

    print("\nMatrix B:")
    for i in B:
        print(i)

    pool = multiprocessing.Pool()
    hasil = pool.map(hitung_baris, [(baris, B) for baris in A])

    pool.close()
    pool.join()

    print("\nHasil perkalian:")
    for i in hasil:
        print(i)