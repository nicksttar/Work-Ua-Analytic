import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from sys import exit
import streamlit as sl

# Ging to import UserAgent to make best experience with parcing
ua = UserAgent()
headers = {"User-Agent": ua.chrome}

class WorkUaParcing:
    """Class which gets data from work.ua like: salary, responses, viewers, salaries.
First of all we create function called "max_pages" in class, to know how much pages we need to parce.
Next function "main_parce" using information about length pages going to search data and return it into dictionary."""

    def __init__(self, job, c='kyiv'):
        """Init job and city if you want from cities.txt"""
        self.job = "+".join(job.split())
        self.city = c

    def get_max_pages(self):
            """Returns max pages of choosen job"""
            data = [1]
            counter = 1
            while data != []:
                counter += 1

                url = f'https://www.work.ua/ru/jobs-{self.city}-{self.job}/?page={counter}'
                url_by_country = f'https://www.work.ua/jobs-{self.job}/?page={counter}'

                # take url into response as argument if u want to parce job in choosen city 
                # take url_by_country into response as argument if u want to parce job in all country 

                response = requests.get(url, headers=headers) 
                soup = BeautifulSoup(response.text, "lxml")
                data = soup.find_all("div", class_="card card-hover card-visited wordwrap job-link")
            return counter-1


    def main_parce(self):
        '''Main function which takes all links from all pages and next going to parce inside every page'''
        print('Getting pages\n')

        length_of_pages = self.get_max_pages() + 1
        salaries, responses, viewers, hrefs = [], [], [], []

        progress_text = "Operation in progress. Please wait."
        my_bar = sl.progress(0.0, text=progress_text)

        # for percent_complete in range(length_of_pages+1):
        #     time.sleep(0.1)
        #     my_bar.progress(percent_complete + 1, text=progress_text)
        for page in range(1, length_of_pages):
                print(f'Gathering information now: page {page} of {length_of_pages-1}')

                url = f"https://www.work.ua/ru/jobs-{self.city}-{self.job}/?page{page}"

                response = requests.get(url, headers)
                soup = BeautifulSoup(response.text, 'lxml')
                data = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link')
                # all vacansies in this page


                links = []
                for vacancy_href in data:
                    link = "https://www.work.ua" + vacancy_href.find('h2', class_='').find('a').get('href')
                    links.append(link)
                # get links from each vacancy

                for link in links:
                    response = requests.get(link, headers)
                    soup = BeautifulSoup(response.text, 'lxml')
                    try:
                        salary = soup.find('b', class_="text-default").text
                    except AttributeError:
                        salary = 'no salary'
                    finally:
                        vacancy_response = soup.find_all("p", class_="text-indent add-top-sm")[1].text.strip().split(".")
                        view = soup.find("h5", class_="cut-top cut-bottom").text.split()[3]
                        
                        responses.append(vacancy_response)
                        viewers.append(view)
                        hrefs.append(link)
                        salaries.append(salary)
                koef = 100/(length_of_pages-1)
                my_bar.progress(page*koef/100, text=progress_text)

        data = {'salaries': salaries, 'responses': responses, 'viewers': viewers, 'hrefs': hrefs}
        print('\ndata.csv created in your directory')
        if len(hrefs) == 0:
             sl.error('No vacancies, type something else')
             exit()
        return data
    
