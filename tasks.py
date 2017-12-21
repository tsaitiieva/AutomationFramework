from invoke import task
import os.path
import json
import allure
import conftest

from Model.User import User
from Fixtures.session import Session




@task
def init_venv(context):
    """
     Creating new virtual env -- NOT READY don`t use it please)
        virtualenv --python=result{which pyton3} --relocatable ENV
      """
    result = context.run("which python3")
    if result.ok:
      context.run("virtualenv --python="+result.stdout.splitlines()[-1]+" --relocatable ENV")
    else :
        print("You don`t have python 3 please install it!")

@task
def save_dependencies(context):
    """
     Saves dependencies to requirements.txt
        pip freeze > requirements.txt
      """
    context.run("pip freeze > requirements.txt")

@task
def update_dependencies(context):
    """
     Updates environment from requirements.txt
        pip freeze > requirements.txt
      """
    context.run("pip install -r requirements.txt")

@task
def init_db(context):
    """
       Here goes script that will help initialize db for the first run
          <add description here>
        """
    session_helper = Session()
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), conftest.get_database_options('users'))
    session_helper.connect_to_db(db_path)
    session_helper.create_tables_db()
#TODO Here goes DB FILE Creation

@task
def fill_db(context):
    """
          Here goes script that will help fill db with data
              <add description here>
           """
# set connection to DB
    session_helper = Session()
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), conftest.get_database_options('users'))
    session_helper.connect_to_db(db_path)


#fill data manually like this
    User.create(user='seeded_male', email='api_male_seeker1@a.com', password='12345678', name='api_male_seeker1',
                platform='Api')
    User.create(user='seeded_male', email='mobile_male_speaker3@a.com', password='12345678',
                name='mobile_male_speaker3', platform='iOS')
    User.create(user='seeded_male', email='api_male_seeker2@a.com', password='12345678', name='api_male_seeker2',
                platform='Android')
    User.create(user='seeded_female', email='api_female_speaker1@a.com', password='12345678',
                name='api_female_speaker1', platform='Api')
    User.create(user='seeded_female', email='mobile_female_receiver1@a.com', password='12345678',
                name='mobile_female_receiver1', platform='iOS')
    User.create(user='seeded_female', email='api_female_speaker2@a.com', password='12345678',
                name='api_female_speaker2', platform='Android')


    # TODO Here goes Filling database with new data

@task
def run_api_tests(context):
    """
          Runs api tests

           """
    context.run("py.test ./Tests/test_api.py  --platform=api --server=qa")