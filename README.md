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

### View Django Web Application at __[Team D](https://team-d.onrender.com)__ or Run It Locally
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
- Create the Superuser
  ```
  python manage.py createsuperuser
  ```
- Start the app
  ```
  python manage.py runserver
  ```
- The app runs at http://127.0.0.1:8000/
- Login page

  <img width="824" alt="image" src="https://github.com/Bsting/fc_aps_mini_project_1/assets/7638997/63e33633-2ba8-49ed-9f66-f3ba35d7776a">
  
- User registration page
  
  <img width="824" alt="image" src="https://github.com/Bsting/fc_aps_mini_project_1/assets/7638997/63c8eadf-e562-4de0-8a2e-242b1fb74296">
  
- Admin page
  
  <img width="925" alt="image" src="https://github.com/Bsting/fc_aps_mini_project_1/assets/7638997/b1d2032c-ae48-4030-9cd7-e99d2382cd09">
  
- Dashboard in light mode
  
  <img width="931" alt="image" src="https://github.com/Bsting/fc_aps_mini_project_1/assets/7638997/be72249c-240f-42a1-909b-c3ae7dbe23b0">
  <img width="915" alt="image" src="https://github.com/Bsting/fc_aps_mini_project_1/assets/7638997/111d0d3d-9c22-4bc2-82d7-fefef6904a73">
  <img width="926" alt="image" src="https://github.com/Bsting/fc_aps_mini_project_1/assets/7638997/6104821c-f80e-4c71-8bcf-39e66c9f8fd5">

- Dashboard in dark mode
  
  <img width="929" alt="image" src="https://github.com/Bsting/fc_aps_mini_project_1/assets/7638997/9b17af93-417e-4d3d-88e7-903400228883">
  <img width="924" alt="image" src="https://github.com/Bsting/fc_aps_mini_project_1/assets/7638997/40a0dd89-0ed1-4e0d-97f3-875d006eaf0d">

