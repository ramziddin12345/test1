def say_salom(name):
    print(f"Salom, {name}!")
say_salom("Ali")
say_salom("Vali")
say_salom("Diyor")

def hisoblash_sum(a, b):
    return a + b
print(hisoblash_sum(5, 3))  
print(hisoblash_sum(10, 2))  
print(hisoblash_sum(2, 5))  

def chop_etish_royxati_raqamlar(raqamlar):
    for raqam in raqamlar:
        print(raqam)
raqamlar = [1, 2, 3, 4, 5]
chop_etish_royxati_raqamlar(raqamlar)

def juft(raqam):
    if raqam % 2 == 0:
        return "To'g'ri"
    else:
        return "Toq"
print(juft(7)) 
print(juft(12))  
print(juft(0))  

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)
print_numbers(1, 5)
print_numbers(10, 15)
