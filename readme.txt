pip3 install pipenvLibraries:
yaml

Run test
Start appium server on one of the ports: 4777-iOS, 4778-Android
appium -p [port] --chromedriver-executable [path to chromedriver from Tools folder]

Allure report generation:
allure serve allure/report

For new branch and contributor access