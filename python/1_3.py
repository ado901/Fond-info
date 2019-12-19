anno = int(input("inserire anno: "))
while anno != 0:
    if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
        print(" Anno bisestile")
    else:
        print("anno non bisestile")
    anno = int(input("inserire anno: "))
