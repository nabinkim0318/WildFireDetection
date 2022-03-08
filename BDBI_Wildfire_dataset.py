import requests
import pandas as pd
TABLE_START = 4
ROW_START = 55
START_YEAR = 2000
END_YEAR = 2022

# Converting each url to text files

firstPartLink = "https://www.cnrfc.noaa.gov/data/text/precip_google/PNM"
Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df = pd.DataFrame()

for year in range (START_YEAR, END_YEAR + 1):
    for month in Month:
        monYear = ("_" + month + "_" + str(year))
        linkName = (firstPartLink + monYear + ".txt")
        
        data = requests.get(linkName)   # response object = contents 
        content = data.text
        lines = content.splitlines()[TABLE_START:]
        data = [line[ROW_START:].split() for line in lines]

        df2 = pd.DataFrame(data)
        df2 = df2.reset_index()
        df2.columns = df2.iloc[0]
        df2 = df2[1:]
        df2['Month'] = month
        df2['Year'] = year
        df = pd.concat([df, df2], ignore_index = True)
df.to_csv("data_noaa_precip.csv")


