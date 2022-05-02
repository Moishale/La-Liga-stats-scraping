from bs4 import BeautifulSoup
import requests

class LaLiga :
    
    def __init__(self , year) :
         self.url = self.url = f"https://www.skysports.com/la-liga-table/{year}"
         self.rows = None
         self.__title = "  #      Team |      Pl |  W |D  |L | F |A | GD | Pts |"

    def  get_table(self) :
        response = requests.get(self.url).text
        soup = BeautifulSoup(response , "html.parser")
        row = soup.find("tbody")
        self.rows = row
        
    def plot_table(self) :
        print(self.__title)
        for x in self.rows :
          a = str(x.text)
          b = { a.replace("\n" , "  ")}
          for c in b :
            print(c)
