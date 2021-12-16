import os
import requests
from bs4 import BeautifulSoup

# [Step 1] Getting the website's information
get = requests.get("https://realpython.github.io/fake-jobs/")

# [Step 2] Printing this would return the unindented parsed code
parse = BeautifulSoup(get.content, "html.parser")

# [Step 3] Scraping
scrapeID = parse.find(id="ResultsContainer") # For findings ids
scrapeClass = parse.find_all("div", class_="card_content")
scrapeSubtitle = parse.find("p", class_="subtitle is-3")

os.system("CLS" if os.name == "nt" else "clear")
print("---USING NO TEXT FORMATTING---")
print(scrapeSubtitle, "\n")
print("---USING .PRETTIFY()---")
print(scrapeSubtitle.prettify(), "\n")
print("---USING .TEXT & .STRIP()---")
print(scrapeSubtitle.text.strip())
