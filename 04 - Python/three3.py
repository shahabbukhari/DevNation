"""
!Parts
* Verify DNA:
    ? Iterate over every element in UserInputDNA Assign Found Value False 
    ? Check character i is present in DNA return false
    ? if current character is not present in DNA preset then its not a valid dna break the loop 
    ? In the end return found value.
* Reverse String:
* Change A with T, T with A AND C with G, G with C
"""


def verifyDNA(usrDNA, DNA):
    for i in usrDNA:
        found = False

        for j in DNA:
            if i == j:
                found = True

        if found == False:
            break

    return found


def reverseDNA(usrDNA):
    revDNA = ""
    for i in usrDNA:
        revDNA = i + revDNA
    return revDNA


def complementDNA(usrDNA):
    compDNA = ""
    for i in usrDNA:
        if i == "A":
            compDNA += "T"
        if i == "T":
            compDNA += "A"
        elif i == "C":
            compDNA += "G"
        elif i == "G":
            compDNA += "C"
    return compDNA


def DNA():
    UserInputDNA = input("Enter a DNA: ")
    UserInputDNA = UserInputDNA.upper()
    validDNA = "ACGT"

    while verifyDNA(UserInputDNA, validDNA) == False:
        UserInputDNA = input(
            "---Invalid DNA sequence---\n Enter a Valid DNA: ")
        UserInputDNA = UserInputDNA.upper()

    reversedDNA = reverseDNA(UserInputDNA)
    complementedDNA = complementDNA(reversedDNA)

    print("The Reversed complemented DNA: ", complementedDNA)


if __name__ == "__main__":
    DNA()