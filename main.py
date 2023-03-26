import DesTables as dt
import tkinter as tk
import random

def generate_key():
    key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

def loadKey():
    try:
        with open(loadKey_entry.get(), "r") as file:
            key = file.read()
            if len(key) == 8:
                key_entry.delete(0, tk.END)
                key_entry.insert(0, key)
                file.close()
            else:
                print("Klucz ma nieprawidłową długość")
                file.close()
    except FileNotFoundError:
        print("Plik nie istnieje")

def saveKey():
    try:
        with open(saveKey_entry.get(), "w") as file:
            if len(key_entry.get()) == 8:
                key = key_entry.get()
                file.write(key)
                file.close()
            else:
                print("Klucz ma nieprawidłową długość")
                file.close()
    except FileNotFoundError:
        print("Nie podano nazwy")

root = tk.Tk()
root.geometry("900x600")

key_frame = tk.Frame(root, bd=2, relief=tk.RAISED)
key_frame.place(x=250, y=0)

inner_frame = tk.Frame(key_frame)
inner_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)

text="Klucz"
text_label = tk.Label(inner_frame, text="Klucz")
text_label.grid(row=0, column=1)

key_label = tk.Label(inner_frame, text="Twój klucz:", font=("Aerial", 8))
key_label.grid(row=1, column=0)

key_entry = tk.Entry(inner_frame, width=15, font=("Arial", 8))
key_entry.grid(row=1, column=1)

key_entry.bind("<Key>", lambda e: "break")

generate_button = tk.Button(inner_frame, text="Generuj klucz", font=("Arial", 8), command=generate_key)
generate_button.grid(row=1, column=2, padx=10)

loadKey_label = tk.Label(inner_frame, text="Wczytaj klucz z pliku:", font=("Aerial", 8))
loadKey_label.grid(row=2, column=0)

loadKey_entry = tk.Entry(inner_frame, width=15, font=("Aerial", 8))
loadKey_entry.grid(row=2, column=1)

loadKey_button = tk.Button(inner_frame, text="Wczytaj", font=("Arial", 8), command=loadKey)
loadKey_button.grid(row=2, column=2, padx=10)

saveKey_label = tk.Label(inner_frame, text="Zapisz klucz do pliku:", font=("Aerial", 8))
saveKey_label.grid(row=3, column=0)

saveKey_entry = tk.Entry(inner_frame, width=15, font=("Aerial", 8))
saveKey_entry.grid(row=3, column=1)

saveKey_button = tk.Button(inner_frame, text="Zapisz", font=("Arial", 8), command=saveKey)
saveKey_button.grid(row=3, column=2, padx=10)

sd_frame = tk.Frame(root, bd=2, relief=tk.RAISED)
sd_frame.place(x=250 , y=200)

inner2_frame = tk.Frame(sd_frame)
inner2_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)



root.mainloop()


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

