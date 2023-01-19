peso = float(input("Digite o peso da porção em gramas"))
proteina = float(input("Digite o valor da proteina"))
carbo = float(input("Digite o valor do carbo"))
gordura = float(input("Digite o valor da gordura"))
peso_a_saber = float(input("Digite o peso que você quer saber"))


def transforma_em_kg(x):
    if x >= 1000:
        x = x / 1000
        return x 
    else:
        return x 


def calcula_caloria(a,b,c):
    calorias = ((a + b) * 4) + (c * 9)
    calorias = calorias * (peso_a_saber / peso)
    print(f'A porção tem {calorias} calorias')




def transforma(gramas,macro,var,nome):
    x = (var * macro) / gramas
    print(f"A quantidade de {nome} em {transforma_em_kg(var)} é {x}")






proteina_1 = transforma(peso,proteina,peso_a_saber,"Proteina")
carbo_1 = transforma(peso,carbo,peso_a_saber,"Carbo")
gordura_1 = transforma(peso,gordura,peso_a_saber,"Gordura")

kcall = calcula_caloria(carbo,proteina,gordura)







