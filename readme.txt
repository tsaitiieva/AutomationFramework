http://docs.python-guide.org/en/latest/dev/virtualenvs/

!!!! In PyCharm change project interpreter to virtualenv !!!!!

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

pip3 install pipenvLibraries:
yaml

Run test
Start appium server on one of the ports: 4777-iOS, 4778-Android
appium -p [port] --chromedriver-executable [path to chromedriver from Tools folder]

https://pypi.python.org/pypi/allure-pytest
https://docs.qameta.io/allure/2.0/#_pytest

Allure report generation:
$ py.test --alluredir=%allure_result_folder% ./tests
$ allure serve %allure_result_folder%



To run tests by Feature or Story:
py.test my_tests/ --allure_features=feature1,feature2
py.test my_tests/ --allure_features=feature1,feature2 --allure_stories=story1,story2

