"""
#1
def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False
x=int(input("Enter the number:"))
print(is_odd(x))


#2
def is_leap(year):
    if year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    elif year % 4 == 0:
        return True

y=int(input("Enter the year:"))
print(is_leap(y))


#3
def print_tri(n):
    total=0
    for i in range(1,n+1):
        total+=i
        print(i,total)
print_tri(10)


#4
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n >2:
     for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True
number=int(input("Enter the number:"))
print(is_prime(number))



#5
def reverse(s):
    result = ""
    for ch in s:
        result = ch+result
    return result
print(reverse("hello"))

def reverse_slice(s):
    return s[::-1]
print(reverse_slice("hello"))

#6
def remove(sub,s):
    return s.replace(sub,"")
print(remove("l","hello world"))


#7
def substitute(message, key):
    alphabet="abcdefgğhıijklmnoöprsştuüvyzw"
    result=""
    for ch in message:
        index=alphabet.find(ch.lower())
        if index==-1:
            result=ch+result
        elif ch.isupper():
            result=result+key[index].upper()
        else:
            result=result+key[index].lower()
    return result

key="qtcabertyuıofghjklzxnwmöçşğüiq"
print(substitute("Hello world",key))

"""
#8
def remove_dups(s):
    result=""
    for ch in s:
        if ch not in result:
            result= result +ch
    return result
print(remove_dups("Hello world"))





























































