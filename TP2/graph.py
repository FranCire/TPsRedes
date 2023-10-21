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


if __name__ == "__main__":
    graph_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/processed_traceroute_cam.ac.uk.txt"
                ,"CambridgePathTimes","Cambridge RTT Times")
    graph_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/processed_traceroute_jhu.edu.txt",
                "JHUPathTimes","JHU RTT Times")
    graph_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/processed_traceroute_uj.ac.za.txt",
                "JohannesburgPathTimes","Johannesburg RTT Times")
    graph_route("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/processed_traceroute_www.u-tokyo.ac.jp.txt",
                "TokyoPathTimes","Tokyo RTT Times")