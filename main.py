from selenium import webdriver
import time
import csv

top_100_games = []
fixed_top_100 = []

# Create Driver
chrome_driver_path = "C:\Programacion\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://steamdb.info/graph/")
time.sleep(1)

# Get all the games and append it to the list
list_of_games = driver.find_elements_by_class_name("app")
for game in list_of_games:
    text = game.find_elements_by_css_selector("td")
    for g in text:
        top_100_games.append(g.text)



# Separate all the games and append them into the list
counter = 7
counter2 = 0

for n in range(0, 101):
    fixed_top_100.append(top_100_games[counter2:counter])
    counter += 7
    counter2 += 7


# Clean the text
for n in range(0, len(fixed_top_100)-1):
    del fixed_top_100[n][1]
    fixed_top_100[n].remove('')


# Write the list into csv
with open('steam_games.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerows(fixed_top_100)