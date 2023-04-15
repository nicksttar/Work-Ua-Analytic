# Work Ua Analytic
This project is a Python-based web scraper designed to analyze job postings on the Work.ua website. It utilizes various data processing and visualization libraries, such as NumPy, Seaborn, Matplotlib, Pandas, Requests, Beautiful Soup, and Fake User Agent, to generate graphs and provide various job analytics. Please understand that web application works from on stremlit host and this cause slow working. 
## Files
* main.py: the application file.
* parser.py: a script that scrapes information from Work.ua.
* reader.py: a function that improves data accuracy.
* requirements.txt: a list of requirements for your virtual environment.
* cities.txt: a list of cities where the program operates.
* analytic.py: a script that generates job analytics within the application.
## Updates
### Version 2.2
Small update:
* Fixed ucorrect link clicking.
* Fixed troubles with launching.
* Add warning in Readme.
### Version 2.1
All aspects of the project have been converted into a web application. The following features have been added:
* A CSV download feature.
* A search-by-city feature.
* And more.
### Version 1.0
* The original project was developed for use in the terminal.
## How to Use
1. Clone the repository to your computer.
2. Open a terminal and navigate to the repository folder.
3. Install the required dependencies by running pip install -r requirements.txt.
4. Run the main.py script in the terminal and launch the web application using the command: python -m streamlit run main.py.
5. Enter your desired job position and area, next click the "Analize" button.
6. The program will generate three graphs to help you understand the job situation in your area and "Quick Report".
## Example
You can try this app by following this link: https://nicksttar-work-ua-analytic-main-o35s80.streamlit.app/
## License
This project is licensed under the MIT License. See the LICENSE file for details.
