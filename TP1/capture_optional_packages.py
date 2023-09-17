from properties_about_source import *
from scapy.all import *
import time
import pytz

S2_src = {}
S2_dst = {}
cant_packages = 0


def callback(pkt):
    global cant_packages
    cant_packages += 1
    if cant_packages % 100 == 0:
        print(f"Cantidad de paquetes procesados hasta el momento: {cant_packages}")
    
    if pkt.haslayer(Ether):
        proto = pkt[Ether].type # El campo type del frame tiene el protocolo
        if proto == 2054: #Codigo de ARP
            s_src_i = pkt[Ether].psrc
            s_dst_i = pkt[Ether].pdst
            if s_src_i not in S2_src:
                S2_src[s_src_i] = 0.0
            if s_dst_i not in S2_dst:
                S2_dst[s_dst_i] = 0.0
            S2_src[s_src_i] += 1.0
            S2_dst[s_dst_i] += 1.0
           

if __name__ == "__main__":
    count = int(input("Cantidad de Paquetes a recibir: "))
    filename = input("Donde escribir los resultados del análisis: ")
    starting_time = datetime.now(pytz.timezone("America/Argentina/Buenos_Aires"))
    sniff(prn=callback,count = count)
    write_object_to_file(S2_dst,f"{filename}_dst_source.txt")
    write_object_to_file(calcular_probabilidad_simbolos(S2_dst),f"{filename}_dst_probas.txt")
    write_object_to_file(calcular_informacion_simbolos(S2_dst),f"{filename}_dst_info.txt")
    write_object_to_file(calcular_entropia_fuente(S2_dst),f"{filename}_dst_entropy.txt")
    write_object_to_file(S2_src,f"{filename}_src_source.txt")
    write_object_to_file(calcular_probabilidad_simbolos(S2_src),f"{filename}_src_probas.txt")
    write_object_to_file(calcular_informacion_simbolos(S2_src),f"{filename}_src_info.txt")
    write_object_to_file(calcular_entropia_fuente(S2_src),f"{filename}_src_entropy.txt")
    ending_time = datetime.now(pytz.timezone("America/Argentina/Buenos_Aires"))
    write_object_to_file(f"Experimentos realizados desde {starting_time} hasta {ending_time}",f"{filename}_src_times.txt")
    write_object_to_file(f"Experimentos realizados desde {starting_time} hasta {ending_time}",f"{filename}_dst_times.txt")

    

