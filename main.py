from read_csv import *
from store_mongo import *


# 1) Read csv files
# 2) Webscrape other websites for teacher homepages
# 3) Store all links and teacher names in a database
# 4) Webscrape links to find teacher a) availability b) accepting interns/ grad students c) check the courses of each teachers
# 5) Add to database


def main():
   main_csv()
   print("Completed reading csv")
   main_mongo() 


if __name__ == "__main__":
    main()
