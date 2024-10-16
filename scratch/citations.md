## Reference for casting types in replaces
I wanted to trouble shoot an error relating to casting specific types that wasn't clear from polars documentation. 

### Ask:
Error code on polars replace from dictionary:
  Cell In[90], line 2
        1 # Ref: Chat-GPT to get code to map without turning
  ----> 2 df = df.with_columns(
        3     pl.col("gestfips").replace(STATES).alias('st')
        4 )
        5 df.head()
  
  InvalidOperationError: conversion from str to i64 failed in column '' for 51 out of 51 values: ["AL", "AK", … "WY"]

### Response
The error you're encountering indicates that polars is trying to convert a string ("str") column into an integer ("i64"), which is causing the failure. This happens because the replace method is likely trying to map string values (state abbreviations) to integer values, but it is not handling the string-to-integer conversion properly.

...

Check Data Types: Make sure that the gestfips column contains strings that match the keys in STATES. You can verify the column type before performing the replacement:
// Casting
df = df.with_columns(
    pl.col("gestfips").cast(pl.Utf8).replace(STATES).alias('st')
)

### Approach
I added this into the code to test and confirmed that the issue was casting the int formatted to a string prior to applying the mapping in the replace solved the type issue. Probably could've figured this out with enough trial and error, but this worked easily.