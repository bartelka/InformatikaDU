def pek_troj(n:int):
    for i in range(n):
        print(" " * (n-i-1) + "*" * (2*i+1))

n = int(input("Zadaj n: "))
print(pek_troj(n))
