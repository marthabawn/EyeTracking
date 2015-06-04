import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab

### Creates fixation plot for matrices, with each aoi colored separately

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
                if dict[trial][row][0] == 'P1':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='blue')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'P2':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='aqua')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'P3':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10,9), facecolors='darkturquoise')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'P4':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10,9), facecolors='royalblue')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'P5':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10,9), facecolors='lightblue')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'P6':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10,9), facecolors='cornflowerblue')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'P7':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10,9), facecolors='mediumorchid')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'P8':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10,9), facecolors='mediumpurple')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'nowhere/Problem':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10,9), facecolors='darkblue')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'A1':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='goldenrod')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'A2':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='yellow')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'A3':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='darkorange')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'A4':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='indianred')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'A5':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='orangered')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'A6':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='gold')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'A7':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='navajowhite')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'A8':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='lightcoral')
                    point += dict[trial][row][1]
                elif dict[trial][row][0] == 'nowhere/Answers':
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='maroon')
                    point += dict[trial][row][1]
                else:
                    ax.broken_barh([(point, dict[trial][row][1])], ((i+1)*10, 9), facecolors='gray')
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
        P1 = mpatches.Patch(color='blue', label='P1')
        P2 = mpatches.Patch(color='aqua', label='P2')
        P3 = mpatches.Patch(color='darkturquoise', label='P3')
        P4 = mpatches.Patch(color='royalblue', label='P4')
        P5 = mpatches.Patch(color='lightblue', label='P5')
        P6 = mpatches.Patch(color='cornflowerblue', label='P6')
        P7 = mpatches.Patch(color='mediumorchid', label='P7')
        P8 = mpatches.Patch(color='mediumpurple', label='P8')
        nowhere_P = mpatches.Patch(color='darkblue', label='Problem Other')
        A1 = mpatches.Patch(color='goldenrod', label='A1')
        A2 = mpatches.Patch(color='yellow', label='A2')
        A3 = mpatches.Patch(color='darkorange', label='A3')
        A4 = mpatches.Patch(color='indianred', label='A4')
        A5 = mpatches.Patch(color='orangered', label='A5')
        A6 = mpatches.Patch(color='gold', label='A6')
        A7 = mpatches.Patch(color='navajowhite', label='A7')
        A8 = mpatches.Patch(color='lightcoral', label='A8')
        nowhere_A = mpatches.Patch(color='maroon', label='Answer Other')
        nowhere = mpatches.Patch(color='gray', label='Other')

        lgd = plt.legend(handles=[P1, P2, P3, P4, P5, P6, P7, P8, nowhere_P, A1, A2, A3, A4, A5, A6, A7, A8, nowhere_A, nowhere],
                         bbox_to_anchor=(1, 1), loc=2, ncol=1, borderaxespad=0)

        # where to save graphs
        pylab.savefig('Graphs/Fixation_Plots/matrices/LSAT_T1/' + subj + '_fixation_plot.png', bbox_inches='tight')
        #plt.show()
        plt.close()
    except ValueError:
        print subj + ' no fixations found'
