import allure
from playwright.sync_api import Locator, Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "/"):
        with allure.step(f"Открыть страницу {path}"):
            self.page.goto(path)

    def click(self, locator: Locator, step_name: str):
        with allure.step(f"{step_name}"):
            locator.click()

    def fill(self, locator: Locator, value: str, step_name: str):
        with allure.step(f"{step_name}"):
            locator.fill(value)

    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()
