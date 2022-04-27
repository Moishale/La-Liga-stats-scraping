from utils import LaLiga , Players

class App(LaLiga) :
  pass

app2 = Players()

def main() :
  print("""
      Welcome To LaLiga Stats Scraper
      Made by - Moishale
      
      """)

  print(""" 
          Commands :
           !table - get the league table by year value
           !score - get the score table of the current season
          """)
  choice = input("Enter any command : ")
  if choice == "!table" :
    year  = input("Enter the  Year of the season to show the table : ")
    app = App(year)
    app.get_table()
    app.plot_table()
  elif choice == "!score" :
    app2.GetTableScore()
   
if __name__ == "__main__" :
  main()