from bs4 import BeautifulSoup
import requests
import json

# slozka = "data.json"
def main():

    url = "https://souhrada.github.io/bsoup-exam/"
    response = requests.get(url)
#vytvari objekt beautiful soup a potom ho rozparsuje do kodu, rozpracuje html stranky 
    soup = BeautifulSoup(response.content, "html.parser") 
    # <--- Úkol: popiš krátce, co tohle dělá
    spisok = soup.find_all("h2")[0], soup.find_all("h2")[1], soup.find_all("h2")[2], soup.find_all("h2")[3]
    print(spisok)

    # with open("data.json", "w", encoding = "uft-8") as f:
    #     json.dump(spisok, f, indent=4)
    # print("pobeda")
    # json.load(path)


if __name__ == "__main__":

    main()
