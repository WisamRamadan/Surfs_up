# Surfs_up Analysis

## Overview of the statistical analysis:
Mr. W.Avy needs information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.
The purpose of the analysis is to provide insights to June and December months' temperatures in Oahu derived from the Hawaii sqlite database provided.

## Results:
The below table shows three key differences in weather between June and December:
|Stat|June Temps| December Temps
-----|-----------|--------------
mean|	74.944118|71.041529
min|	64.000000|56.000000
max|	85.000000|83.000000

* December has a significantly lower minimum temperature than June.
* The average temperature is higher in June.
* The maximum temperature is slightly higher in June compared to December.

## Summary:

The temperature analysis results shows that December temperature with a minimum of 56 degree can affect the ice cream and surfing sales. Additional queries can be run to gather more weather data for June and December to see if the business can be sustained all year around. We can analyze precipitation in these months:
* June precipitation:
```jun_prcp = session.query(Measurement.date,Measurement.prcp).filter(extract('month', Measurement.date)==6).all()```
* December percipitation:
``` dec_prcp = session.query(Measurement.date,Measurement.tobs).filter(extract('month', Measurement.date)==6).all()```

