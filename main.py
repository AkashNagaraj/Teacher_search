from read_csv import *
from store_mongo import *

# Search teacher vs [interested field, research papers(google scholar link)] Anything else? 

# 1) Read csv files [university homepage link, teachers homepage link]
# 3) Store all links and teacher names in a database
# 4) Website functionality:
#    Input  -> University Name
#    *Output1 -> average test score at the university (seems unlikely)
#    Output2 -> List of teachers names [more info : specific fields] , internships/ Reasearch Assistant openings
# 5) Website UI

def main():
   main_csv()
   print("Completed reading csv")
   main_mongo() 


if __name__ == "__main__":
    main()
