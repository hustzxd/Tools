import sys
import matplotlib.pyplot as plt


def plot_figure(test_file):
    with open(test_file, 'r') as rf:
        text = rf.read()
    lines = text.split('\n')
    iter_list = []
    acc_list = []
    for i, line in enumerate(lines):
        if i == 0:
            continue
        attributes = line.split()
        if len(attributes) != 4:
            break
        iter_list.append(int(attributes[0]))
        acc_list.append(float(attributes[2]))
    plt.figure()
    plt.plot(iter_list, acc_list, marker='o')
    plt.xlabel('Iter')
    plt.ylabel("Accuracy")
    plt.title("Iter vs Accuracy(Val)")
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python plot_figures.py  [test.log]")
        exit(1)
    plot_figure(sys.argv[1])
