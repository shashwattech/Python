num = int(input("input the number you want to check if is prime or not: " ))


def checkPrime(num):

    if num <= 1:
        return False
    
    else:
        for i in range (2,num):

            if (num%i == 0): #be mindful of when to return True or False
                return False
            
            else:
                return True
            

print (checkPrime(num =num))