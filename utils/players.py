from bs4 import BeautifulSoup
import requests

class Players :
  def __init__(self) :
   self.__url = "https://www.topscorersfootball.com/la-liga"
   self.__response = requests.get(self.__url).text
   self.__soup = BeautifulSoup(self.__response , "html.parser")
   self. __row = self.__soup.find("table")

  def GetTableScore(self) :
     for x in self.__row :
          a = str(x.text)
          data = a.replace("\n" , " ")
          l = (data.replace("\xa0" , ""))
          print(l)



