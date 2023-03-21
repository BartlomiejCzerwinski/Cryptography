import DesTables as dt

def char_to_bits(char):
    binary_string = bin(ord(char))[2:].zfill(8)
    bits = [int(bit) for bit in binary_string]
    return bits

def arrayToString(array):
    result = ""
    for i in array:
        if i == 1:
            result += "1"
        else:
            result +="0"
    return result

def stringToArray(stringToConvert):
    tmp = []
    for i in stringToConvert:
        if i == "1":
            tmp.append(1)
        else:
            tmp.append(0)
    return tmp

def create64BitsBlock(plaintext):
    result = ""
    for char in plaintext:
        charAsBits = char_to_bits(char)
        result += (arrayToString(charAsBits))
    if len(result) < 64:
        result += ((64 - len(result)) * "0")
    print("created block: ", result)
    return result

def initialPermutation(textToPermute):
    result = ""
    for i in dt.IP:
        result +=textToPermute[i - 1]
    print("created permutatuin: ", result)
    return result
initialPermutation(create64BitsBlock("ABCD1234"))

def divide64BitsIntoLeftRihtHalf(bits):
    left = bits[:32]
    right = bits[32:]
    print(left)
    print(right)

def extendRightHalfOfData(rightHalf):
    result = ""
    for i in dt.E:
        result += rightHalf[i-1]
    print("extendent right:", result)
    return result

def createKey(key64Bits):
    key48Bits = ""
    for i in dt.PC1:
        key48Bits += key64Bits[i - 1]
    return key48Bits

def moveKeyBitsIntoLeft(key, numberOfPositions):
    return key[numberOfPositions:] + key[:numberOfPositions]

def xorOnRightHalfAnd48BitsKey(rightHalf, key48Bits):
    result = ""
    for i in range(48):
        a = int(rightHalf[i])
        b = int(key48Bits[i])
        if (a + b) % 2 == 0:
            result += "0"
        else:
            result +="1"
    return result

def divideXorResultInto8x6BitBlocks(xorResult):
    result = []
    for i in range(8):
        tmp = ""
        for j in range(6):
            tmp += xorResult[(i * 6) + j]
        result.append(tmp)
    return result

def permutateWithSBoxes(dataToPermutate):
    result = ""
    tmp = 0
    for i in dataToPermutate:
        result += dt.Sboxes[tmp][i]
        tmp += 1
    return result

def permutateWithPBlock(dataToPermutate):
    result = ""
    for i in dt.P:
        result += dataToPermutate[i]
    return result

