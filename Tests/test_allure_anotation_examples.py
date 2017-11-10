import pytest
import allure
from flaky import flaky
from random import randint


@allure.issue('http://jira.lan/browse/ISSUE-3')
def test_something():
    pass

@pytest.allure.testcase('http://my.tms.org/TESTCASE-1')
def test_something_else():
    pass

@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_minor():
    assert False


@allure.feature('Feature1')
@allure.story('Story1')
def test_major():
    step()
    assert False


@allure.step('some operation for bar={0}')
def step():
    pass

@flaky(max_runs=3, min_passes=2)
@pytest.mark.label
def test_something_that_usually_passes():
    if randint(0,1)== 1:
        pass
    else:
        assert False