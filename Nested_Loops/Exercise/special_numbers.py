n = int(input())

for i in range (1 , 10):
    for k in range (1 , 10):
        for l in range(1, 10):
            for z in range(1 , 10):
                if n % i == 0 and n % k == 0 and n % l == 0 and n % z == 0:
                    print(f"{i}{k}{l}{z}", end= " ")