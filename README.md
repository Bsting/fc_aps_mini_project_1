# Foward College - Applied Data Science Mini Project 1
Mini Project 1 for Applied Data Science course.<br> 
This project analyses a dataset of new listed properties on 2024-02-01 from __[iProperty.com.my](https://www.iproperty.com.my/new-property)__.

## Team D
Team members
- Teh Woei Xiang
- Boo Soon Ting

## Project Structure
- web_scraping folder, contains notebook to scrape data from iProperty.com.my
- eda folder, contians notebook for EDA
- word_cloud folder, contains notebook for word cloud
- django, contains file related to a dashboard application developed with Django web framework
- data, contains data generated from notebooks in web_scraping and eda

## Prerequisite
- Install Anaconda, __[Anaconda Installation](https://docs.anaconda.com/free/anaconda/install/index.html)__
- Create a virtual environment with the name 'mini_project_1' and python 3.10
  ```
  conda create -n mini_project_1 python=3.10
  ```
- Activate mini_project_1
  ```
  conda activate mini_project_1
  ```
- Download the code
  ```
  git clone https://github.com/Bsting/fc_aps_mini_project_1.git
  cd fc_aps_mini_project_1
  ```
  
### To run Notebook in web_scraping Folder
- Go to web_scraping folder
  ```
  cd web_scraping
  ```
- Install all required packages
  ```
  pip install -r requirements.txt
  ```
- open iproperty.ipynb notebook and run the cells to scrape data from iProperty.com.my for new listed properties

### To run Notebook in eda Folder
- Go to eda folder
  ```
  cd eda
  ```
- Install all required packages
  ```
  pip install -r requirements.txt
  ```
- open iproperty_eda.ipynb notebook and run the cells for EDA of scrapped data from iProperty.com.my on 2024-02-01

### To run Django Web Application
- Go to django folder
  ```
  cd django
  ```
- Install all required packages
  ```
  pip install -r requirements.txt
  ```
- Set up database
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- Start the app
  ```
  python manage.py runserver
  ```
- The app runs at http://127.0.0.1:8000/
