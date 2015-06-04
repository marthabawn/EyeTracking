import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab

### Creates fixation plot for matrices, with each aoi colored according to group

# modified from Mike's script

df = pd.read_csv('All_Stats/LSAT_T1matrices_fixations.csv')
subjects = pd.Series(df['PID'].values.ravel()).unique()

# can also replace subjects with a list of PIDs if only some plots needed
for subj in subjects:

    df_copy = df[df['PID'] == subj]
    # Create dictionary with trial number as key and fixation AOI and duration in a tuple as value
    dict = {}

    for row, item in df_copy.iterrows():
        if df_copy['Trial'][row] not in dict:
            dict[df_copy['Trial'][row]] = []
            dict[df_copy['Trial'][row]].append((df_copy['Fixation_AOI'][row], df_copy['Fixation_Dur'][row]))
        elif df_copy['Trial'][row] in dict:
            dict[df_copy['Trial'][row]].append((df_copy['Fixation_AOI'][row], df_copy['Fixation_Dur'][row]))

    print subj+':', dict

    # Calculate the total trial duration
    trials = pd.Series(df_copy['Trial'].values.ravel()).unique()
    trial_durs = np.zeros(len(trials))

    for i, trial in enumerate(trials):
        trial_durs[i] = df_copy[df_copy['Trial'] == trial]['Fixation_Dur'].sum()

    # Create the plot
    try:
        fig, ax = plt.subplots()
        for i, trial in enumerate(trials):
            point = 0
            for row, item in enumerate(dict[trial]):
                if dict[trial][row][0] in ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'nowhere/Problem']:
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='blue')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'nowhere/Answers']:
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='yellow')
                    point += dict[trial][row][1]
                else:
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10,9), facecolors='gray')
                    point += dict[trial][row][1]

        # Format the plot
        index = 0
        ticks = []
        for x in range(0, len(trials)+1):
            tick = (index + 1) * 10 + 5
            ticks.append(tick)
            index += 1

        ax.set_title(subj + ': Fixations in AOIs')
        ax.set_ylim(5, len(trials))
        ax.set_xlim(0, trial_durs.max()+2500)
        ax.set_xlabel('milliseconds since start')
        ax.set_ylabel('Trial')
        ax.set_yticks(ticks)
        ax.set_yticklabels(trials)
        ax.grid(False)
        # Format the legend, define labels
        Problem = mpatches.Patch(color='blue', label='Problem')
        Answers = mpatches.Patch(color='yellow', label='Answers')
        nowhere = mpatches.Patch(color='gray', label='Other')

        lgd = plt.legend(handles=[Problem, Answers, nowhere], bbox_to_anchor=(1, 1), loc=2, ncol=1, borderaxespad=0)

        # where to save graphs
        pylab.savefig('Graphs/Fixation_Plots/matrices/LSAT_T1/' + subj + '_fixation_plot_grouped.png', bbox_inches='tight')
        #plt.show()
        plt.close()
    except ValueError:
        print subj + ' no fixations found'
