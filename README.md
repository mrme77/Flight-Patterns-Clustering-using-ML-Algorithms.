# Flight Patterns Clustering using ML Algorithm

Author: Pasquale Salomone
<br>
Date: November 3, 2023

## Overview

This project focuses on implementing algorithms like K-Means and Mean Shift to cluster flight data. Both models are fitted on flight data, without splitting into training and testing set since the test set will not have true labels available. The intent is assign each flight to a clsuter based on specific features to possibly identify flight patterns in the geographical region closer to the ADSB receiver.

to be continued....

## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)

The following modules are required: 
import pandas as pd
import numpy as np
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

| Module          | Version  |
|-----------------|----------|
| time            | 3.11.4   |
| collections     | 3.11.4   |
| pandas          | 1.5.3    |
| numpy           | 1.23.2   |
| folium          | 0.13.1   |
| matplotlib      | 3.5.3    |
| os              | 1.11.0   |
| haversine       | 3.2.1    |
| sqlite3         | 3.39.2   |
| linregress      | 1.9.3    |

## Data Sources

The project utilizes live data from FlightAware, a leading provider of aviation data and flight tracking information, through PiAware 7.2 running on a Raspberry PI. The original data sources include various flight-related information such as aircraft identifiers, timestamps, altitude, latitude, longitude, speed, heading, and transponder codes.

## Resources

- [FlightAware](https://www.flightaware.com/)
- [Automatic Dependent Surveillance - Broadcast (ADS-B)](https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afx/afs/afs400/afs410/ads-b)
- [PiAware](https://blog.flightaware.com/piaware-7-release#:~:text=PiAware%207%20has%20several%20new,(SD%20Card%20Image%20only).)
- [Transponder Codes](https://code7700.com/transponder.htm)


## Output



## Flowchart

![Flowchart](flow.jpg)
![Clusters](initial_clusters.jpg)
## Video




## Acknowledgments

I would like to acknowledge Stackoverflow, ChatGPT, Google Bard as an instrumental aid in the development of this project.

## License

This project is licensed under the MIT License.


