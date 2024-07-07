
import numpy as np
import pandas as pd


data=pd.read_csv("./clustering_data.csv",low_memory=False)

class Location:
    def __init__(self):
        self.ap = data[data["CircleName"] == "Andhra Pradesh Circle"].copy()
        self.ap["Longitude"] = pd.to_numeric(self.ap["Longitude"], errors="coerce")
        self.ap["Latitude"] = pd.to_numeric(self.ap["Latitude"], errors="coerce")

        self.ap.dropna(subset=["Longitude", "Latitude"], inplace=True)

        longitude_percentiles = np.percentile(self.ap["Longitude"], [5, 95])
        latitude_percentiles = np.percentile(self.ap["Latitude"], [5, 95])

        self.ap = self.ap[(self.ap["Longitude"] >= longitude_percentiles[0]) &
                (self.ap["Longitude"] <= longitude_percentiles[1]) &
                (self.ap["Latitude"] >= latitude_percentiles[0]) &
                (self.ap["Latitude"] <= latitude_percentiles[1])]
        latitudes = list(self.ap["Latitude"])
        longitudes = list(self.ap["Longitude"])
        latitudes = [float(l) for l in latitudes]
        longitudes = [float(k) for k in longitudes]

        self.location_coordinate=self.ap[["Longitude","Latitude"]].values
        self.location_coordinate=self.location_coordinate.astype(float)
