import numpy as np
import pandas as pd
from parcer import WorkUaParcing

def correct_salary(salary):
    salary = salary.replace("\u202f", "")
    salary = salary.replace("\u2009", "")
    salary = salary.replace("\xa0", "")
    salary = salary.replace('–', '-')
    return salary

def job_format1(job):
    return job[1]

def job_format2(job):
    return job[0]

def fixed_salary(f_salary):
    if f_salary != 'no salary':
        f_salary = f_salary.replace('грн', '').strip()
        f_salary = f_salary.split('-')
        f_salary = [int(i) for i in f_salary]
        f_salary = np.mean(f_salary)
        return int(f_salary)
    
def validator(question, mode=['1', '2', '3']):
    """Basic anty-dump validator"""
    user_input = input(question)
    while user_input.lower() not in mode:
        user_input = input(question)
    if user_input.lower() in mode:
        return user_input.lower()

def write_file(arg, c):
    ''''''
    data = WorkUaParcing(arg, c).main_parce()

    df = pd.DataFrame(data)


    df['salaries'] = df['salaries'].apply(correct_salary)

    df['Experience'] = df['responses'].apply(job_format1)
    df['responses'] = df['responses'].apply(job_format2)
    df['salaries'] = df['salaries'].apply(fixed_salary)
    df['viewers'] = df['viewers'].astype(int)

    df = df[['salaries', 'responses', 'Experience', 'viewers', 'hrefs']]

    return df
