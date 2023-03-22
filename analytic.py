import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def analitics(mode=1):
    """Function which model graph by what you need.
Have 3 modes: 1-Responses, 2-KDE of viewers, 3-Salaries by Experiece"""


    df = pd.read_csv('data.csv')

    if mode == 1:
        sns.countplot(data=df, x='responses', hue='Experience', palette='viridis')
        plt.title('Responses')
        plt.show()
    elif mode == 2:
        sns.kdeplot(data=df,x='viewers', hue='Experience', palette='viridis')
        plt.title('KDE of viewers')
        plt.show()
    elif mode == 3:
        
        fig, ax = plt.subplots()
        sns.boxplot(data=df.dropna(), x='salaries', y='Experience', palette='viridis')
        plt.title('Salary from Experience')
        new_position = [0.2, 0.1, 0.75, 0.75] 
        ax.set_position(new_position)
        plt.show()
