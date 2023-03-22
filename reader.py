import pandas as pd
from parcer import WorkUaParcing
from handlers import correct_salary, job_format1, job_format2, fixed_salary

def write_file(arg):
    ''''''
    data = WorkUaParcing(arg).main_parce()

    df = pd.DataFrame(data)


    df['salaries'] = df['salaries'].apply(correct_salary)

    df['Experience'] = df['responses'].apply(job_format1)
    df['responses'] = df['responses'].apply(job_format2)
    df['salaries'] = df['salaries'].apply(fixed_salary)

    df = df[['salaries', 'responses', 'Experience', 'viewers', 'hrefs']]

    df.to_csv('data.csv', index=False)
    
# write_file('data')

WorkUaParcing