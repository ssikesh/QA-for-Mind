import os
import pytest
from selenium import webdriver
@pytest.fixture()
def setup(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    if request.node.rep_call.failed:
        screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}.png")
        driver.save_screenshot(screenshot_path)
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)