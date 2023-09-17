import matplotlib.pyplot as plt
import seaborn

from properties_about_source import *

def graph_pie_chart(dict,filename = "piegraph",title = "Piegraph",xaxis = "X",yaxis = "Y"):
    data = list(dict.values())
    keys = dict.keys()

    palette_color = seaborn.color_palette('bright')

    plt.pie(data,labels = keys,colors=palette_color,textprops={'fontsize':8},
            autopct='%1.2f%%')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    plt.savefig(f"{filename}.png")
    plt.close()

def graph_bar_chart(dict,filename = "barchart",title="Barchart",xaxis = "X",yaxis = "Y"):
    heights = list(dict.values())
    keys = [str(key) for key in dict.keys()]

    plt.figure(figsize=(14,6))

    print("HOLAA")

    plt.barh(keys,heights)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    plt.savefig(f"{filename}.png")
    plt.close()

if __name__ == "__main__":
    probas = read_object_from_file("results_fran_probas.txt")
    info = read_object_from_file("results_fran_info.txt")
    graph_pie_chart(probas)
    print(info)
    graph_bar_chart(info)