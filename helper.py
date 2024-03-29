import matplotlib.pyplot as plt
from IPython import display

plt.ion()
plt.show()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    #display.display(plt.gcf())
    plt.figure(1)
    plt.cla()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.pause(.1)

def losses_plot(plot_losses):
    display.clear_output(wait=True)
    #display.display(plt.gcf())
    plt.figure(2)
    plt.cla()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Loss')
    plt.plot(plot_losses)
    plt.text(len(plot_losses) - 1, plot_losses[-1], str(plot_losses[-1]))
    plt.pause(.1)
