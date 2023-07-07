# DPS AI Challenge

To predict number of accidents, vizualize historical trends and create a web app for the same.

## Dataset

The dataset used for this challenge is taken from the München Open Data Portal

### Monatszahlen Verkehrsunfälle

Link : https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7

The above data provides historical information values on the number of accidents for different categories per month in the
city of Munich, Germany. As the dataset contains several columns, but the focus is on the mentioned first five columns which are important to our task, hence feature selection is not required here.

| Translated Column Name - >       | Category   | Accident-type | Year | Month | Value |
| -------------------------------- | ---------- | ------------- | ---- | ----- | ----- |
| Actual Column Name in Dataset -> | MONATSZAHL | AUSPRAEGUNG   | JAHR | MONAT | WERT  |

### Category Types [ MONATSZAHL ]:

1. 'Alkoholunfälle' - Alcohol accidents
2. 'Fluchtunfälle' - Escape accidents
3. 'Verkehrsunfälle' - Traffic Accidents

### Accident Types [ AUSPRAEGUNG ]:

1. 'insgesamt' - total
2. 'mit personenschäden' - personal injury
3. 'Verletzte und Getötete' - injured and killed

---

## The final results are generated through a Neural Network (GRU)
