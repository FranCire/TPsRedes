from math import log2

def calcular_informacion_a_partir_de_probas(probas_simbolos):
    return dict([(d,-log2(p)) for d,p in probas_simbolos.items()])

def calcular_probabilidad_simbolos(S):
    N = sum(S.values())
    return dict([(d,k/N) for d,k in S.items()])

def calcular_informacion_simbolos(S):
    probas_simbolos = calcular_probabilidad_simbolos(S)
    return calcular_informacion_a_partir_de_probas(probas_simbolos)

def calcular_entropia_fuente(S):
    proba_simbolos = calcular_probabilidad_simbolos(S)
    info_simbolos = calcular_informacion_simbolos(S)
    entropia =  sum([proba_simbolos[s] * info_simbolos[s] for s in S.keys()])
    return entropia


def write_object_to_file(d,filename):
    with open(filename,"w") as file:
        file.write(str(d))

def read_object_from_file(filename):
    with open(filename,"r") as file:
        lines = file.readlines()
    return eval(lines[0])