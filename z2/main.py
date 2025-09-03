from selenium import webdriver
from selenium.webdriver import ActionChains
import csv
import sys
from baseapp import BasePage
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from selenium.webdriver.remote.webelement import WebElement


class PageOnlyOffice(BasePage):
    def go(self) -> None:
        self.driver.get('https://www.onlyoffice.com/')

    def click_to_contacts(self) -> None:
        element: 'WebElement' = self.driver.find_element('xpath', '//a[@id="navitem_about"]')
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_element('xpath', '//a[@id="navitem_about_contacts"]').click()

    def parse_contacts(self, path_to_file: str) -> None:
        with open(path_to_file, 'w') as fw:
            csv_writter = csv.writer(fw, delimiter=';')
            csv_writter.writerow(['Country', 'CompanyName', 'FullAddress'])
            elements: List['WebElement'] = self.driver.find_elements(
                'xpath',
                '//div[@itemtype="https://schema.org/PostalAddress"]'
            )
            for element in elements:
                country = ''
                company_name = ''
                address: List[str] = []
                elems: List['WebElement'] = element.find_elements('xpath', './span[@class="region"]')
                if elems:
                    country = elems[0].text
                elems = element.find_elements('xpath', './span/b')
                if elems:
                    company_name = elems[0].text
                #
                # тут явно в itemprop косяк!
                elems = element.find_elements('xpath', './span[@itemprop="addressCountry"]')
                if elems:
                    address.append(elems[0].text)
                #
                elems = element.find_elements('xpath', './span[@itemprop="telephone"]')
                if elems:
                    address.append(elems[0].text)
                elems = element.find_elements('xpath', './span[@itemprop="postalCode"]')
                if elems:
                    address.append(elems[0].text)
                csv_writter.writerow([country, company_name, ' '.join(address)])


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        raise ValueError('Не указан путь в выходному файлу')
    path = args[1]
    if not path.endswith('.csv'):
        raise ValueError('Путь в выходному файлу должен заканчиваться на ".csv"')
    driver = webdriver.Firefox()
    page = PageOnlyOffice(driver)
    page.go()
    page.click_to_contacts()
    page.parse_contacts(path)
    page.driver.close()
