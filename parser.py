from bs4 import BeautifulSoup
import requests

choices = input("Enter schools to check for in all pages").split(" ")
print(choices)

index = 98
while index > 0:
    print(f"Checking Page {index}")
    link = "https://www.everyonesinvited.uk/read-testimonies-page-"
    link += str(index)
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html.parser')

    for part in soup.select('.coloredtext'):
        splitting = part.select('p')
        try:
            title = str(splitting[1])
        except:
            title = " "

        try:
            text = splitting[0]
        except:
            text = " "

        for school in choices:
            print(title)
            if school.lower() in title.lower():
                print(title, text)

    index -= 1
