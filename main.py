from utils import LaLiga

year  = input("Enter the  Year of the season to show the table : ")

test = LaLiga(year)
test.get_table()

if __name__ == "__main__" :
  test.plot_table()