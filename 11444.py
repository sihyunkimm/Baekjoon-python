PRIME = 1_000_000_007

f_dict = {
    0 : 0,
    1 : 1,
    2 : 1,
    3 : 2
}

def fibo(n):
    if n in f_dict:
        return f_dict[n]
    else:
        half = n //2
        if n % 2 == 0 :
            h0 = fibo(half)
            h1 = fibo(half-1)
            f_dict[n] = ((2*h1 + h0)*h0) % PRIME
            return f_dict[n]
        else : 
            h0 = fibo(half+1)
            h1 = fibo(half)
            f_dict[n] = (h0**2 + h1**2) % PRIME
            return f_dict[n]
    

n = int(input())
print(fibo(n))