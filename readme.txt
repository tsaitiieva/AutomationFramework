===Virtual environment===

General info: http://docs.python-guide.org/en/latest/dev/virtualenvs/

!!!! In PyCharm->Preferences->Buil, Execution, Deployment change project interpreter to virtualenv !!!!!

install globally
pip install virtualenv

-- activate virtualenv
source project_env_py3/bin/activate

-- installing new dependencies
pip install -r requirements.txt

-- after adding new dependencies:
pip freeze > requirements.txt

-- after work is done ...
deactivate

===Libraries===
https://pypi.python.org/pypi/allure-pytest
https://docs.qameta.io/allure/2.0/#_pytest

===Design Patterns===
2 design patterns were used:
- Page Object
- Steps

+ pytest fixtures

===General info===
DB is used for storing user accounts
Locators can be stored in csv/yaml file. If you're working with one platform you can use yaml,
if you're working with iOS and Android it can be more convenient csv.

Allure is used for reporting. Annotate each step to get beautiful reports.

===Project structure===
root
- config.json - config file. We should specify platform in command line, other settings (such as server name) can be
specified in this json config
- conftest.py - file with pytest fixtures, methods for reading config file anf getting parameters from comend line.
ATTENTION! don't rename or delete coftest.py if you want to continue work with fixtures. Otherwise pytest will be unable
to read them.
- Logfile - logs are written here. Log method is located in helpers fixture.
- requirements - libraries used in project are listed here and used in virtual environment.

Fixtures
- all fixtures are lying here

Model
- used for storing some models (e.g. Users, Request)

PageObject
- all Page Object class are living here.
- all classes should inherit basic Page class
- also class that allows to work with data for api methods living here

project_env_p3
- needed for virtualenvironment

Steps
- all steps are living here in appropriate files
- give clear names to files and methods(steps) in order to read test easily (e.g. Authentication.enter_email)
- steps consist of some page object classes methods calls and some assertins

Support
- files with json schemes are living in JSON_Scheme folder
- accounts.db is sqllite3 db were accounts is stored. Link to utility to work with DB: http://sqlitebrowser.org/
- locators - 2 ways are implemented: csv and yaml file. Use whatever you like
ATTENTION: if you rename, delete or transfer folder/files keep in mind that appropriate methods should be modified to work with updated data


Temp
- when attach_file method is called files will be written in this folder
ATTENTION: if you rename, delete or transfer folder/files keep in mind that appropriate methods should be modified to work with updated data

Tests
- tests are lying here
- reports will be written here to (report folder)

Tools
- cromedriver is lying here
- your apk, app files can be here too

===How To===
Api
- correct config.json if you want to use it
- correct users fixture is you need it
- correct Users model if you need it
- correct api fixture in conftest.py
- correct Api file with proper capabilities
- add required data to api_helpers class in PageObject
- correct ApiRequest if needed
- correct Api steps if needed
- add test to api_test.py

UI
- add your app/apk file to Tools directory
- add locators
- add user account to DB if some is used in your app
- correct config.json if you want to use it
- correct users fixture is you need it
- correct Users model if you need it
- correct app fixture in conftest.py
- correct Application file with proper capabilities
- create Page object class for your page
- create Steps file with steps
- create test

===Runing tests===
Start appium server on one of the ports: 4777-iOS, 4778-Android
appium -p [port] --chromedriver-executable [path to chromedriver from Tools folder]

Run test
see run.sh

Allure report generation:
$ py.test --alluredir=%allure_result_folder% ./tests
$ allure serve %allure_result_folder%


To run tests by Feature or Story:
py.test my_tests/ --allure_features=feature1,feature2
py.test my_tests/ --allure_features=feature1,feature2 --allure_stories=story1,story2

