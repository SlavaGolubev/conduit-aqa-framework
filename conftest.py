import allure
import pytest
from playwright.sync_api import Page

from utils.config import settings


@pytest.fixture(scope="session")
def base_url():
    return settings.base_url


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1920, "height": 1080}}


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": settings.headless,
    }


@pytest.fixture(scope="function")
def page(page: Page):
    page.set_default_timeout(settings.timeout)
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                allure.attach(
                    body=page.screenshot(full_page=True),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print(f"Failed to take screenshot: {e}")
