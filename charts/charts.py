import matplotlib.pyplot as plt
import numpy as np

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    values = [158, 370, 245, 180]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.savefig('pie_chart.png')
    plt.close(fig)