if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:

    #Removes $ from price
    price = price.replace("$", "")

    #Removes , from price
    price = price.replace(",", "")

    #Converts price to a float
    price = float(price)

    #Returns price
    return price

def clean_scraped_text(scraped_text: str) -> list[str]:

    #Splits scraped data into new lines
    text = scraped_text.split('\n')

    #Creates an empty list to store cleaned items in
    cleaned_items = []

    #Loops through each item that was scraped and filters out the designated lines
    for item in text:
        if item in ['GS', 'V', 'S', 'P']:
            continue
        if item.startswith('NEW'):
            continue
        if len(item.strip()) == 0:
            continue

        #Adds lines that don't contain the designated items to the list
        cleaned_items.append(item)
    
    #Returns the list of cleaned items
    return cleaned_items

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:

    #Calls function created above to get clean scraped text
    cleaned_text = clean_scraped_text(scraped_text)

    #Creates item with a default value for MenuItem
    item = MenuItem(category= title, name = "", price = 0.0, description= "")

    #Adds the first element of cleaned text as the name of the item
    item.name = cleaned_text[0]

    #Adds the second element of cleaned text as the price of the item, uses clean_price function on text before to convert to float
    item.price = clean_price(cleaned_text[1])

    #Checks to see if item has a description since not all items do
    if len(cleaned_text) > 2:
        item.description = cleaned_text[2]
    else:
        item.description = "No Description Available."

    #Returns created item of the MenuItem class
    return item



if __name__=='__main__':
    pass
