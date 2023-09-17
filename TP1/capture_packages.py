from scapy.all import *
import pytz
from properties_about_source import *
import time


cant_packages = 0
S1 = {}


    
def mostrar_fuente(S):
    N = sum(S.values())
    simbolos = sorted(S.items(), key=lambda x: -x[1])
    print("\n".join([ "%s : %.5f" % (d,k/N) for d,k in simbolos ]))
    print()
def callback(pkt):
    global cant_packages
    cant_packages += 1
    if cant_packages % 100 == 0:
        print(f"Cantidad de paquetes procesados hasta el momento: {cant_packages}")
    if pkt.haslayer(Ether):
        dire = "BROADCAST" if pkt[Ether].dst=="ff:ff:ff:ff:ff:ff" else "UNICAST"
        proto = pkt[Ether].type # El campo type del frame tiene el protocolo
        s_i = (dire, proto) # Aca se define el simbolo de la fuente
        if s_i not in S1:
            S1[s_i] = 0.0
        S1[s_i] += 1.0



if __name__ == "__main__":
    count = int(input("Cantidad de Paquetes a recibir: "))
    filename = input("Donde escribir los resultados del análisis: ")
    starting_time = datetime.now(pytz.timezone("America/Argentina/Buenos_Aires"))
    sniff(prn=callback,count = count)
    write_object_to_file(S1,f"{filename}_source.txt")
    write_object_to_file(calcular_probabilidad_simbolos(S1),f"{filename}_probas.txt")
    write_object_to_file(calcular_informacion_simbolos(S1),f"{filename}_info.txt")
    write_object_to_file(calcular_entropia_fuente(S1),f"{filename}_entropy.txt")
    ending_time = datetime.now(pytz.timezone("America/Argentina/Buenos_Aires"))
    write_object_to_file(f"Experimentos realizados desde {starting_time} hasta {ending_time}",f"{filename}_times.txt")

    
    