

# def greet(firstName, lastName):
#     print("Hello,", firstName + " " + lastName)


# greet("Aanav", "Noolee")    


# for i in range(5):
#     print(i)


# def passRange(start, end):
#     for i in range(start, end):
#         if(i % 2 == 0):
#            print(i)

# passRange(5, 21)


def checkPrime(a):
    for i in range(2, a):
        if(a % i == 0):
            print(a, "is not a Prime number")
            break
    print(a , "is a prime number")        


checkPrime(7)    