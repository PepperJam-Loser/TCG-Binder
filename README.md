# TCG-Binder
This application is a digital binder for trading card games that allows the user to effortlusly manage their physical card collections. It is written in python and powered by Django. 

# Installation Steps

1. Install python3.12.X on your system. This varies by operating system but once youve dont this you should be able to run `python3 --version` in your terminal and get `Python 3.12.X` as output.

2. Clone this repository to your local system using `git clone git@github.com:ChicoState/TCG-Binder.git`. Then navigate to the directory you just cloned.

3. Create a python virtual enviroment and activate it using the following commands. `python3 -m venv venv` && `source venv/bin/activate` .

4. Install the required python packages using the following command. `python3 -m pip install -r requirements.txt`

5. Launch the Django testing server using the command `python3 manage.py runserver`. You may have to also run the command `python3 manage.py migrate`

