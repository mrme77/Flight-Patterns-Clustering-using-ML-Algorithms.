# Flight Patterns Clustering using ML Algorithm

Author: Pasquale Salomone
<br>
Date: November 3, 2023

## Overview

<p>This project is dedicated to the exploration of flight patterns using machine learning algorithms, specifically K-Means and Mean Shift. The primary objective is to cluster flight data based on relevant features, aiming to uncover potential flight patterns within the geographical area surrounding an ADSB receiver. Unlike traditional machine learning tasks, the dataset is not divided into training and testing sets, as the test set lacks true labels. Instead, the focus is on unsupervised clustering to group flights based on their characteristics. The ultimate goal is to gain insights into flight behavior and identify distinct patterns within the region of interest. The project uses fictional data and simulates a connection to an ADSB receiver.</p>


![PI](pi_receiver.jpg)



## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)

The following modules are required: 


```
import pandas as pd
import numpy as np
import hashlib
import folium
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import haversine
from folium.plugins import HeatMap
from folium import PolyLine
import sqlite3
from shapely.geometry import Point
from scipy.stats import linregress
from prettytable import PrettyTable
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, HTML
```


## Data Sources

The project utilizes de-identified synthetic streamed data, from an Automatic Dependent Surveillance–Broadcast (ADS-B) receiver connected to a Raspberry Pi running Pi Aware 7.2. Synthetic data ensure anonymization( remove or hash any columns that contain PII), randomization (randomize data elements that should not be traceable to individual flights), preserve statistical properties (ensure that the synthetic data maintains the same statistical properties as the original data, such as the mean, variance, and distribution of numerical variables), and maintain relationships (preserve any relationships or correlations between variables that are present in the real data). The original data sources include various flight-related information such as aircraft identifiers, timestamps, altitude, latitude, longitude, speed, heading, and transponder codes.

## Resources

- [FlightAware](https://www.flightaware.com/)
- [Automatic Dependent Surveillance - Broadcast (ADS-B)](https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afx/afs/afs400/afs410/ads-b)
- [PiAware](https://blog.flightaware.com/piaware-7-release#:~:text=PiAware%207%20has%20several%20new,(SD%20Card%20Image%20only).)
- [Transponder Codes](https://code7700.com/transponder.htm)


## Deployment

+ Project7Notebook.ipynb It is a Jupyter Notebook which executes Data Collection, Exploratory Data Analysis (EDA), Data Preprocessing, Model Fitting and Evaluation, and display results.
  
+ adsb_flight_data.py Contains the script for receiving and processing data from an Automatic 
  Dependent Surveillance-Broadcast (ADS-B) system.
  
+ adsb_functions.py Contains the data description language (DDL) syntax for creation of tables as well as the data manipulation language (DML) for inserting data, and the the function (data_stream_and_store) the continuous streaming and storage of data received from a network socket connected to a Raspberry Pi running Pi Aware 7.2. 



## Flowchart

![Flowchart](flow.jpg)

![MLPipeline](MLPipeline.jpg)


## Acknowledgments

I would like to acknowledge Stackoverflow, ChatGPT, Google Bard as an instrumental aid in the development of this project.

## License

This project is licensed under the MIT License.


