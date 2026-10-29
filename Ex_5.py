def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Acima do peso"
    else:
        return "Obesidade"

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print("IMC:", round(imc, 2))
print("Classificação:", classificacao)