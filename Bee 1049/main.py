#Usando dicionário na resolução, mas dá para fazer por if e else
p1 = str(input())
p2 = str(input())
p3 = str(input())

catalogo = {
    "vertebrado":{
        "ave":{
            "carnivoro": "aguia",
            "onivoro": "pomba",
        },

        "mamifero":{
            "onivoro": "homem",
            "herbivoro": "vaca",
        },
    },

    "invertebrado":{
        "inseto":{
            "hematofago": "pulga",
            "herbivoro": "lagarta",
        },
        "anelideo":{
            "hematofago": "sanguessuga",
            "onivoro": "minhoca",
        },
    }
}

print(catalogo[p1][p2][p3])