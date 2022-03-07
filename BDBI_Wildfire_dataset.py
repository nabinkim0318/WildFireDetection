import requests
import pandas as pd
TABLE_START = 4
ROW_START = 55
START_YEAR = 2000
END_YEAR = 2021

# Converting each url to text files

firstPartLink = "https://www.cnrfc.noaa.gov/data/text/precip_google/PNM"
Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for year in range (START_YEAR, END_YEAR + 1):
    for month in Month:
        monYear = ("_" + month + "_" + str(year))
        linkName = (firstPartLink + monYear + ".txt")
        fileName = ("data_noaa_precip_" + monYear) # ex) data_noaa_precip__Apr_2000
        
        data = requests.get(linkName)   # response object = contents 
        content = data.text
        lines = content.splitlines()[TABLE_START:]
        data = [line[ROW_START:].split() for line in lines]

        df = pd.DataFrame(data)
        df.columns = df.iloc[0]
        df = df[1:]

        #data/test_noaa_precip.csv
        df.to_csv(fileName + ".csv")
        print(fileName, " done!")


        
 
