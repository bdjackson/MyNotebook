import numpy as np
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------------------------
def simulate_free_throws(num_shots=100):
    num_made = 1
    current_prob = 0.5

    # simulation for shots 3-num_shots-2
    simulations = np.random.rand(num_shots-2)
    history = [1, 0]
    history.extend([0]*(num_shots-2))

    for _shot_num in range(2, num_shots):
        history[_shot_num] = int(simulations[_shot_num-2] < current_prob)
        num_made += history[_shot_num]
        current_prob = float(num_made)/(_shot_num+1)

    return history


# ------------------------------------------------------------------------------
def find_running_probability(history, title=''):
    running_counts = history.cumsum(axis=1)
    running_probability = running_counts.divide([_itr+1 for _itr in
                                                 range(history.shape[1])],
                                                 axis=1)

    running_probability.transpose().plot(legend=False, colormap='Greys',
                                         title=title)
    running_mean = [np.mean(running_probability[_index]) for _index
                    in range(history.shape[1])]
    final_probability = np.mean(running_probability[history.shape[1]-1])
    end_point = mp.patches.Ellipse((history.shape[1], final_probability),
                                   width=5, height=0.05, color='steelblue',
                                   zorder=10)
    ax = plt.gcf().gca()
    ax.set_xlabel('Shot number')
    ax.set_ylabel('Running probability')
    ax.add_artist(end_point)

    props = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)

    # place a text box in upper left in axes coords
    print(round(final_probability, 2))
    ax.text(history.shape[1], final_probability,
                         'Avg; {}'.format(round(final_probability, 2)),
                                        # transform=ax.transAxes,
                                        # fontsize=14,
                    verticalalignment='top', bbox=props)

    plt.show()


# ------------------------------------------------------------------------------
def run_simulations(num_simulations, num_shots=100):
    simulations = [simulate_free_throws(num_shots)
                   for _ in range(num_simulations)]
    simulations = pd.DataFrame(simulations)
    simulations_selection = simulations[simulations[num_shots-2] == 1]
    simulations_anti_selection = simulations[simulations[num_shots-2] == 0]

    find_running_probability(simulations, title='All shots')
    find_running_probability(simulations_selection,
                             title='Make second to last')
    find_running_probability(simulations_anti_selection,
                             title='Miss second to last')


# ==============================================================================
if __name__ == '__main__':
    # run_simulations(10000)
    run_simulations(250, 100)
