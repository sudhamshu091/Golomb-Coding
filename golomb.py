import math

def golomb(codeword,m):
    c = int(math.ceil(math.log(m,2)))
    reminder = codeword%m
    quotent = int(math.floor(codeword/m))
    print("c",c,"Reminder",reminder,"Quotent",quotent)
    div = int(math.pow(2,c)-m)
    first = ""
    one = "1"
    for i in range(quotent):
        first = first + one
        print("First:",first)
    if reminder < div:
        b = c-1
        a = "{0:0" + str(b) + "b}"
        print("1",a.format(reminder))
        binary = a.format(reminder)
    else:
        b = c
        a = "{0:0" + str(b) + "b}"
        print("2",a.format(reminder + div))
        binary = a.format(reminder + div)

    final = first + "0" + str(binary)
    return final

golombcode = golomb(codeword,m) # golomb(18,16)
print("Golomb Coding:",golombcode)
