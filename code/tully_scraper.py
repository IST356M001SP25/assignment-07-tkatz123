import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")

    #Creates an empty list to store scraped menu items in
    menu_items = []

    #Iterates over each section of the menu (EX: starters & snacks, best chicken tenders, etc.)
    for title in page.query_selector_all("h3.foodmenu__menu-section-title"):

        #Gets the text for the section of the menu and prints it 
        title_val = title.inner_text()
        print("MENU SECTION:", title_val) 

        #Goes two rows down from the section title to a div class called row
        row = title.query_selector("~ *").query_selector("~ *")

        #Iterating over each element of the div foodmenu_menu-item
        for item in row.query_selector_all("div.foodmenu__menu-item"):

            #Gets the value of each element in the div
            item_val = item.inner_text()

            #Calls the extract menu item function on the section and that item
            extracted_item = extract_menu_item(title_val, item_val)

            #Prints each menu item
            print(f"  MENU ITEM: {extracted_item.name}")

            #Converts each menu Item to dictionary format
            menu_items.append(extracted_item.to_dict())

    #Converts the menu_items dictionary to a dataframe and exports it as a csv
    df = pd.DataFrame(menu_items)
    df.to_csv("cache/tullys_menu.csv", index=False)    

    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
