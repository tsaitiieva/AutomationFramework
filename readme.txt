http://docs.python-guide.org/en/latest/dev/virtualenvs/

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

Allure report generation:
allure serve allure/report
