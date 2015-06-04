import pandas as pd
import numpy as np
#This will create a plot for each participant for each trial showing each duration of each fixation in order


#subs = pd.Series(df_fix['Subject'].values.ravel()).unique()
non_perfect_subs = pd.Series(df_fix_ana_err['Subject'].values.ravel()).unique()

for sub in non_perfect_subs:
    df_new = df_fix_ana_err[df_fix_ana_err['Subject']==sub]

#With Andrew's help 4-14-15:
#Create a dictionary with trial number as the key and fixation location and duration as tuple values in the list for each trial

    myDict = {}

    for row, item in df_new.iterrows():
        if df_new['Trial_Order'][row] not in myDict:
            myDict[df_new['Trial_Order'][row]] = []
            myDict[df_new['Trial_Order'][row]].append((df_new['Fixation_AOI_Lure'][row],df_new['Fixation_duration'][row]))
        elif df_new['Trial_Order'][row] in myDict:
            myDict[df_new['Trial_Order'][row]].append((df_new['Fixation_AOI_Lure'][row],df_new['Fixation_duration'][row]))

# This calculates the duration for each trial in terms of fixation duration
    trials = pd.Series(df_new['Trial_Order'].values.ravel()).unique()

    max_trial = np.zeros(len(trials))

    for index, trial in enumerate(trials):
        max_trial[index] = (df_new['Fixation_duration'][0:len(df_new[df_new['Trial_Order'].isin([trial])])].sum())

#This creates a broken bar plot where each of the rows is a trial and each length of color is fixation duration
    fig, ax = plt.subplots()

    for index,trial in enumerate(trials):
        point = 0
        for row, item in enumerate(myDict[trial]):
            if myDict[trial][row][0] == '2A':
                ax.broken_barh([(point, myDict[trial][row][1])], ((index+1)*10, 9), facecolors='blue')
                point += myDict[trial][row][1]
            elif myDict[trial][row][0] == '2B':
                ax.broken_barh([(point, myDict[trial][row][1])], ((index+1)*10, 9), facecolors='red')
                point += myDict[trial][row][1]
            elif myDict[trial][row][0] == '2C':
                ax.broken_barh([(point, myDict[trial][row][1])], ((index+1)*10, 9), facecolors='yellow')
                point += myDict[trial][row][1]
            elif myDict[trial][row][0] == 'CRESP':
                ax.broken_barh([(point, myDict[trial][row][1])], ((index+1)*10,9), facecolors = 'green')
                point += myDict[trial][row][1]
            elif myDict[trial][row][0] == 'sLure_loc':
                ax.broken_barh([(point, myDict[trial][row][1])], ((index+1)*10,9), facecolors = 'cyan')
                point += myDict[trial][row][1]
            elif myDict[trial][row][0] == 'pLure_loc':
                ax.broken_barh([(point, myDict[trial][row][1])], ((index+1)*10,9), facecolors = 'magenta')
                point += myDict[trial][row][1]
            elif myDict[trial][row][0] == 'uLure_loc':
                ax.broken_barh([(point, myDict[trial][row][1])], ((index+1)*10,9), facecolors = 'grey')
                point += myDict[trial][row][1]
            else:
                ax.broken_barh([(point, myDict[trial][row][1])], ((index+1)*10,9), facecolors = 'black')
                point += myDict[trial][row][1]


#This will format the plot
    index=0
    for x in range(0,len(trials)):
        tick=(index+1) * 10 + 5
        ticks.append(tick)
        index+=1
    ax.set_ylim(5,len(trials))
    ax.set_xlim(0,max_trial.max())
    ax.set_xlabel('milliseconds since start')
    ax.set_yticks(ticks)
    ax.set_yticklabels([])
    ax.grid(False)
    A_loc = mpatches.Patch(color='blue', label='A')
    B_loc = mpatches.Patch(color='red', label='B')
    C_loc = mpatches.Patch(color='yellow', label='C')
    D_loc = mpatches.Patch(color='black', label='D')
    Target_loc = mpatches.Patch(color='green', label='Target')
    sLure_loc = mpatches.Patch(color='cyan', label='sLure')
    pLure_loc = mpatches.Patch(color='magenta', label='pLure')
    uLure_loc = mpatches.Patch(color='grey', label='uLure')

    plt.legend(handles=[A_loc, B_loc, C_loc, D_loc, Target_loc, sLure_loc, pLure_loc, uLure_loc],bbox_to_anchor=(1, 1), loc=2,
           ncol=1, borderaxespad=0.)

    subject = df_new['Subject'].iloc[1]
    pylab.savefig(str(subject) + '_fix_dur.png')
    plt.close()

