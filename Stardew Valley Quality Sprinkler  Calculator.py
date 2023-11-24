#Learning Python and using it to help me create quality sprinkler in Stardew Valley

minerioDeFerro = int(input("Quantos minérios de ferro você tem? "))
minerioDeOuro = int(input("Quantos minérios de ouro você tem? "))
quartzo = int(input("Quantos quartzo você tem? "))
print("")

barraDeFerro = minerioDeFerro // 5
barraDeOuro = minerioDeOuro // 5
quartzoRefinado = quartzo // 5

aspersor = min(barraDeFerro, barraDeOuro, quartzoRefinado)

print(f"Você tem {barraDeFerro} barras de ferro")
print(f"Você tem {barraDeOuro} barras de ouro")
print(f"Você tem {quartzoRefinado} quartzo refinado")
print("")
print(f"A quantidade de aspersores de qualidade que você pode criar é: {aspersor}")
