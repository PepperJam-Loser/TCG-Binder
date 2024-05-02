# TCG-Binder
This application is a digital binder for trading card games that allows the user to effortlusly manage their physical card collections. It is written in python and powered by Django. 

# Installation Steps

1. Install python3.12.X on your system. This varies by operating system but once youve dont this you should be able to run `python3 --version` in your terminal and get `Python 3.12.X` as output.

2. Clone this repository to your local system using `git clone git@github.com:ChicoState/TCG-Binder.git`. Then navigate to the directory you just cloned.

3. Create a python virtual enviroment and activate it using the following commands. `python3 -m venv venv` && `source venv/bin/activate` .

4. Install the required python packages using the following command. `python3 -m pip install -r requirements.txt`

5. Launch the Django testing server using the command `python3 manage.py runserver`. You may have to also run the command `python3 manage.py migrate`

# Importing Cards into database

1. delete the current sqlite file you have in your project directory, we are going to start with a clean db file

2. run the db migrations using `python3 manage.py migrate` (if your on linux) or whatever command your platform uses

3. create a super user account using `python3 manage.py createsuperuser` (if your on linux) or whatever command your platform uses

4. run the application

5. Open the app, login as your admin account and navigate to /admin

6. Click on 'cards' from the left hand menue. Then once you are on the card page, click on import in the top right part of your screen. ![card import](/static/images/admin_card.png)


7. Click on the browse button to select a file to import and navigate to TCG-Binder/static/data/cards_cleaned.json ![card import](/static/images/import_cards.png)


8. Click the Submit button and wait for the preview to take place. This may take a couple of minutes. 


9. Once the preview has taken place finish importing the cards by clicking confrim import. This process can take a few minutes to finish. ![card import](/static/images/confirm_import.png)

10. Once the cards are imported it will look like this ![card import](/static/images/confirm_import.png)
