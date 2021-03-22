input1 = ["123","456","789","112","4588"]

# Solution cleared myself.
def solution1(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if(phone_book[i+1].find(phone_book[i])==0):
            return False
    return True

# Good solution on programmer.
# var.startswith(foo), same find() f
# zip() multy list

def solution2(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

if __name__ == "__main__":
   print(solution1(input1))