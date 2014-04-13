A_max = 256
A_max_squared = A_max * A_max

primes = ["1"]*A_max_squared

for n in range(2,A_max_squared//2):
    if (primes[n]=="1"):
        j = 2
        while((j*n)<A_max_squared):
            primes[j*n] = "0"
            j=j+1

for n in range(2,A_max_squared//2):
    if(primes[n]=="1"):
        print("Prime number: ", n)

for A in range(A_max):
    if((primes[A*256-1]=="1") and (primes[A*128-1]=="1")):
        print (A)
