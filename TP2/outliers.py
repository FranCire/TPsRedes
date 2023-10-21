from scipy.stats import t
from math import sqrt
from save_and_load import *
import matplotlib.pyplot as plt


def mean(sample):
    return sum(sample) / len(sample)

def std(sample):
    mean_val = mean(sample)
    return sqrt(sum([(x - mean_val)**2 for x in sample]) / len(sample))


def tau(n):
    t_alpha = t.ppf(0.975,df = n-2)
    tau = (t_alpha * (n-1))/(sqrt(n) * sqrt(n-2 + t_alpha * t_alpha))
    return tau


def graph_standardized(sample,filename,title):
    xs = list(range(len(sample)))
    mean_val = mean(sample)
    std_val = std(sample)
    ys = [abs(x - mean_val)/std_val for x in sample]
    plt.scatter(xs,ys)
    plt.ylabel("Distancia a la media normalizada")
    plt.axhline(y=tau(len(sample)),linestyle='-')
    plt.title(title)
    plt.savefig(f"{filename}.png")
    plt.close()


def find_outliers(sample):
    sample_pair = [(x,i) for i,x in enumerate(sample)]
    filtered = []
    while len(sample) >= 3:
        mean_val = mean(sample)
        std_val = std(sample)
        biggest = max(sample)
        idx = sample.index(biggest)
        delta = abs(biggest - mean_val)
        if delta > tau(len(sample)) * std_val:
            filtered.append(sample_pair[idx][1])
            del sample[idx]
            del sample_pair[idx]
        else:
            return filtered
    return filtered

if __name__ == "__main__":
    rtt_between_jumps = read_object_from_file("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/rtt_between_jumps_cam.ac.uk.txt")
    outliers = find_outliers([jump[4] for jump in rtt_between_jumps])
    outlier_jumps = [rtt_between_jumps[i] for i in outliers]
    write_object_to_file(outlier_jumps,"data/cambridge_outliers.txt")
    graph_standardized([jump[4] for jump in rtt_between_jumps],"data/standardized_cambridge","Sample Estandarizada Cambridge")


    rtt_between_jumps = read_object_from_file("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/rtt_between_jumps_jhu.edu.txt")
    outliers = find_outliers([jump[4] for jump in rtt_between_jumps])
    outlier_jumps = [rtt_between_jumps[i] for i in outliers]
    write_object_to_file(outlier_jumps,"data/jhu_outliers.txt")
    graph_standardized([jump[4] for jump in rtt_between_jumps],"data/standardized_jhu","Sample Estandarizada JHU")


    rtt_between_jumps = read_object_from_file("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/rtt_between_jumps_uj.ac.za.txt")
    outliers = find_outliers([jump[4] for jump in rtt_between_jumps])
    outlier_jumps = [rtt_between_jumps[i] for i in outliers]
    write_object_to_file(outlier_jumps,"data/johannesburg_outliers.txt")
    graph_standardized([jump[4] for jump in rtt_between_jumps],"data/standardized_johannesburg","Sample Estandarizada Johannesburg")


    rtt_between_jumps = read_object_from_file("/home/fcirelli/Documents/UBA/Redes/TPs/TP2/rtt_between_jumps_www.u-tokyo.ac.jp.txt")
    outliers = find_outliers([jump[4] for jump in rtt_between_jumps])
    outlier_jumps = [rtt_between_jumps[i] for i in outliers]
    write_object_to_file(outlier_jumps,"data/tokyo_outliers.txt")
    graph_standardized([jump[4] for jump in rtt_between_jumps],"data/standardized_tokyo","Sample Estandarizada Tokyo")

