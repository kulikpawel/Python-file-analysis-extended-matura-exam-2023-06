#3.1
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
file = open("anagram.txt")
#file = open("example.txt")
lines = file.readlines()
abbn = 0  #amount of balanced binary numbers
abnab = 0 #amount of binary numbers almost balanced
for l in lines:
    if l.count("0") == l.count("1"):
        abbn+=1
    elif l.count("0") - l.count("1") == 1 or l.count("1") - l.count("0") == 1:
        abnab +=1
print("3.1")
print("Amount of balanced binary numbers: ", abbn)
print("Amount of binary numbers almost balanced", abnab)
#3.2 Digital anagrams
print("_"*60)
lines8bit = []
for l in lines:
    if len(l) == 9:
        lines8bit.append(l[:-1])
listanagramcounts = dict({})
for l in lines8bit:
    if l.count("1")>=1:
        count1 = l.count("1")
        count0 = l.count("0")
        anagramscount = factorial(count0+count1-1)//(factorial(count1-1)*factorial(count0))
        listanagramcounts.update({l:anagramscount})
maxanagramscount = max(listanagramcounts.values())
print("3.2")
print("""All 8-digit binary numbers in the anagram.txt file from which you can create the largest number of anagrams: """)
for l in listanagramcounts:
    if maxanagramscount == listanagramcounts[l]:
        print(l)
print("_"*60)
#3.3 Absolute value
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
max_abs = 0
for i in range(len(lines)-1):
    number1 = 0
    number2 = 0
    for j in range(len(lines[i])):
        number1 += int(lines[i][j]) * (2 ** (len(lines[i])-j-1))
    for j in range(len(lines[i+1])):
        number2 += int(lines[i+1][j]) * (2 ** (len(lines[i+1])-j-1))
    if abs(number1-number2) > max_abs:
        max_abs = abs(number1-number2)
print("3.3")
print("The greatest absolute value of the difference between adjacent numbers:", str(bin(max_abs))[2:])
print("_"*60)
#3.4.a Numbers without zero
decimal = []
for i in range(len(lines)):
    number = 0
    for j in range(len(lines[i])):
        number += int(lines[i][j]) * (2 ** (len(lines[i]) - j - 1))
    decimal.append(number)
withoutzero = 0
for i in range(len(decimal)):
    if "0" not in str(decimal[i]):
        withoutzero += 1
print("3.4.a")
print("Number of decimal numbers without zero in the notation: ", withoutzero)
# 3.4.b - The number with the largest sum of distinct digits
maxsumdistinct = 0
indexmaxsumdistinct = 0
for i in range(len(decimal)):
    setofdigits = set()
    d_copy = decimal[i]
    while d_copy // 10 > 0:
        setofdigits.add(d_copy % 10)
        d_copy = d_copy // 10
    setofdigits.add(d_copy % 10)
    if maxsumdistinct < sum(setofdigits):
        maxsumdistinct = sum(setofdigits)
        indexmaxsumdistinct = i
print("3.4.b")
print("The number with the largest sum of distinct digits:", decimal[indexmaxsumdistinct])




