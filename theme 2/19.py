rub = int(input())	#a
kop = int(input())	#b
n = int(input())

rub = n * rub + (n * kop) // 100	
kop = (n * kop) % 100				

print(rub, kop)