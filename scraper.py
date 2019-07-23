from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


class RecipeScraper(object):

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")

    def scrape(self, recipe):
        self.driver.get('https://minimalistbaker.com/')

        search_bar = self.driver.find_element_by_xpath('//input[@placeholder="Search Minimalist Baker..."]')
        search_bar.send_keys(recipe)
        search_bar.submit()

        # click the first recipe
        first_recipe = self.driver.find_element_by_class_name("entry-title-link")
        first_recipe.click()

        try:
            recipe = self.driver.find_element_by_class_name("wprm-recipe-ingredient-group")
        except: 
            # find the first recipe in the list
            time.sleep(5)
            ad = self.driver.find_element_by_class_name("adthrive-close")
            ad.click()
            listing = self.driver.find_element_by_xpath('//article/div[1]/p[1]/a')
            listing.click()
            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[1])

        recipe = self.driver.find_element_by_class_name("wprm-recipe-ingredient-group")
        # hack to get all the <li> elements
        ingredients = recipe.find_elements_by_class_name('wprm-recipe-ingredient')
        instructions = self.driver.find_element_by_class_name("wprm-recipe-instructions")
        instruction_list = instructions.find_elements_by_class_name("wprm-recipe-instruction-text")

        title = self.driver.find_elements_by_class_name("entry-title")
        print(self.driver.title + '\n') 


        print("Ingredients:\n")
        for ingredient in ingredients:
            print(ingredient.text)

        print('\n')

        print("Instructions:\n")
        for instruction in instruction_list:
            print(instruction.text + '\n')

def main(args):
    scraper = RecipeScraper()
    print('Scraping site...\n')
    scraper.scrape(args[0])


if __name__ == '__main__':
    main(sys.argv[1:])
