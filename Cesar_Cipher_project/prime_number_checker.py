nbr = int(input("Entre a number: "))

def prime_number(nbr):
    is_prime = True 
    for i in range(2, nbr+1):
      if i%nbr == 0:
        is_prime = False
    return is_prime


if prime_number(nbr):
  print("It's a prime number")
else:
  print("It's not a prime number.")