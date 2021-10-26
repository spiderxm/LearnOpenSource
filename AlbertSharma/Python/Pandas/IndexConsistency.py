import pandas as pd
srs_1 = pd.Series([50, 49, 48], index = ['Gautam', 'Arnav', 'Sood'])
srs_2 = pd.Series([47, 49, 45], index = ['Kaustubh', 'Arnav', 'Areeb'])
srs = srs_1 / srs_2
srs.name = "Resultant"
srs.index.name = "STUDENT"
print("Lets See")
print(srs) # -----------------------------------------------------------------------------------------------!
# Here NaN is for non common elements
# here one that are common , gets the ellemt divided as the operation suggest.

print("Some more functions")
print(pd.isnull(srs)) # true that are NaN ------------------------------------------------------------------2
print(pd.notnull(srs)) # true that are common --------------------------------------------------------------3
print(srs[srs == 1.0]) # -----------------------------------------------------------------------------------4
print(srs[srs != 1.0]) # -----------------------------------------------------------------------------------5
# 1.0 is stored for the values that are true.
