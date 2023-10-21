from save_and_load import *
import matplotlib.pyplot as plt

def graph_route(path_file,filename,title):
    path = read_object_from_file(path_file)
    xs  = path.keys()
    ys = [val[1] for val in path.values()]
    plt.plot(xs,ys,linestyle='--',marker='o')
    plt.xlabel('TTL')
    plt.ylabel('RTT time')
    plt.title(title)
    plt.savefig(f"{filename}.png")
    plt.close()

def graph_increasing_route(path_file,filename,title):
    rtt_between_jumps = read_object_from_file(path_file)
    xs = [jump[0] for jump in rtt_between_jumps] + [rtt_between_jumps[-1][1]]
    ys = [0]
    for jump in rtt_between_jumps:
        ys.append(ys[-1] + jump[4])
    plt.plot(xs,ys,linestyle='--',marker='o')
    plt.xlabel('TTL')
    plt.ylabel('RTT time')
    plt.title(title)
    plt.savefig(f"{filename}.png")
    plt.close()


if __name__ == "__main__":
    graph_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/processed_traceroute_cam.ac.uk.txt"
                ,"data/CambridgePathTimes","Cambridge Tiempos RTT")
    graph_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/processed_traceroute_jhu.edu.txt",
                "data/JHUPathTimes","JHU Tiempos RTT")
    graph_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/processed_traceroute_uj.ac.za.txt",
                "data/JohannesburgPathTimes","Johannesburg Tiempos RTT")
    graph_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/processed_traceroute_www.u-tokyo.ac.jp.txt",
                "data/TokyoPathTimes","Tokyo Tiempos RTT")
    
    graph_increasing_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/rtt_between_jumps_cam.ac.uk.txt"
                ,"data/CambridgeTruePathTimes","Cambridge Tiempos RTT")
    graph_increasing_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/rtt_between_jumps_jhu.edu.txt",
                "data/JHUTruePathTimes","JHU Tiempos RTT")
    graph_increasing_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/rtt_between_jumps_uj.ac.za.txt",
                "data/JohannesburgTruePathTimes","Johannesburg Tiempos RTT")
    graph_increasing_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/rtt_between_jumps_www.u-tokyo.ac.jp.txt",
                "data/TokyoTruePathTimes","Tokyo Tiempos RTT")
    
    