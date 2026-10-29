palavras = ["pneumoultramicroscopicosilicovulcanoconiose", "Anticonstitucionalissimamente", "Ornitorrinco", "Cavalo", "Carol", "Sara"]

P_MAX = 0
P_MIN = 50

for palavra in palavras:
    if len(palavra) < P_MIN:
        P_MIN = len(palavra)
        P_MENOR = palavra
    if len(palavra) > P_MAX:
        P_MAX = len(palavra)
        P_MAIOR = palavra

print("A maior palavra é:", P_MAIOR, "com", P_MAX, "letras.")
print("A menor palavra é:", P_MENOR, "com", P_MIN, "letras.")