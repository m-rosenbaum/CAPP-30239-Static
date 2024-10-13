## Static Visualization Project Proposal
#### Michael Rosenbaum

## Description
I intend to focus my static visualization on Unemployment Insurance (UI) recipiency (who receives benefits). There's a bit of tension on how to calculate recipiency, who's actually eligible, as well as a lot of misunderstandings on who knows what. I would like to explore how the recipiency rates are calculated, how they can be calculated, and then what differences in UI recipiency mean for different states.

My initial plan is to create a database of the data used by the Department of Labor to report on UI recipiency, and then create a few visualizations that show the different ways to get to this number visually. Since this data is a time series, I could also explore how this has changed over time both nationally and at the state-level. Finally, what's most interesting to me is showing the state-level variation in how many people get unemployment insurance, and what their characteristics are. There's been some more academic research ([ex. 1](https://www.dol.gov/sites/dolgov/files/OASP/evaluation/pdf/CaliforniaPolicyLab_Final_20220105_508.pdf), [ex. 2](https://www.bls.gov/opub/mlr/1997/07/art2full.pdf), [ex. 3](https://www.dol.gov/sites/dolgov/files/OASP/evaluation/pdf/University%20of%20Illinois%20-%20Final%20SDC%20Paper.pdf)) on who gets UI, but I think there's a lot of opportuntiy to explore how to understand what recipiency means and how it shapes our perception of who gets UI. 

## Likely Data Sources
I will use a combination of the following data sources to estimate who many recipients there are:

- [Unemployment Insurance Weekly Claims Data](https://oui.doleta.gov/unemploy/claims.asp): This is a state-, week-level panel of the number of new claimants of unemplyoment insurance and the number of unemployment insurance payments (weeks claimed) of active insured unemployed workers. It includes 104,304 state weeks (including Puerto Rico, District of Columbia, and the United States Virgin Islands) between August 1987 and the present.
- [ETA 203 (Characteristics of Insured Unemployed)](https://oui.doleta.gov/unemploy/DataDownloads.asp#ETA_203): This is a state- month-level panel of the number of new recipients of unemployment insurance and their self-reported race, gender, ethnicity, and industrial characteristics. It contains 20,317 state months (including Puerto Rico, District of Columbia, and the United States Virgin Islands) between August 1994 and the present.
- [Current Population Survey - NBER Rerelease](https://www.nber.org/research/data/current-population-survey-cps-basic-monthly-data): This is a person- / month-panel of Current Population Survey with some processing to construct relevant variables to estimate alternative unemployment rates. This data will be converted into state- / month-estimates of unemployment using various measures based on existing statistical software code I've written. I estimate that this will contain 18,309 records with the same variables of race, ethnicity, gender, and recent employment sector as ETA 203.

## Questions
As of right now, my questions are focused on scope and how to set up an easy to use database.

- I'm aware that I'm frontloading a bit of data processing, but have been meaning to set up a UI recipiency database for a while. I've done this already in Stata for research I've done professionally and last year. To do so, I plan on creating a sqlite 3 database that's view-only on my Google Drive and then having some code to copy it into this repo. I would plan on running queries on that to pull out the data for each visualization at the right unit of analysis. Do you see any problems with that? 
- Given that there's already a fair amount of academic work on this, should I pivot topics?