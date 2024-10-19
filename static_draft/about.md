# Unemployment Recipiency
Michael Rosenbaum

**NOTE: This is going to use my late budget. I'm pretty behind for a variety of reasons including the data issues explained below. I'll have a commit up before the end of the weekend to review**

## What is your current goal? Has it changed since the proposal?
My goal has drastically reduced in scope. I still intend to describe why recipiency rates of unemployment insurance is confusingly measured, and leads to obscuring a meaningful problem that Americans face. However, data limitations have meant that I've spent a lot of time dealing with content issues, even after sketching out my preferred format.

## Are there data challenges you are facing? Are you currently depending on mock data?
Yes. Getting in data has been a problem to start with as the data that I scraped from DOL in the past changed in format slightly. This put me a little behind.

This was exacerbated when I found today that the recipiency rate values reported in the ETA-539 report does not actually make sense (>100%, does not match the online tool that DOL releases recipiency data with). I'm planning on downloading and merging in the flat file of recipiency rates from the interactive tool as it's pretty central to the point I'm making. 

In the meantime, I'm not mocking up data yet as the relative formats are fine. I'll push the plots before the end of the weekend.

## Describe each of the provided images with 2-3 sentences to give the context and how it relates to your goal.
I am developing 9 plots across 2 categories.

### What is recipiency?
1. (Single line plot) Federal Recipiency rate: This shows the federal recipiency rate for unemployment insurance since 2006, up until 2020. It aims to introduce the concept of recipiency of unemployment insurance and illustrate that not everyone gets benefits.
2. (Binned historgram(?) with line): Initial claims: This plot aims to introduce more information about what's being counted by showing new claims for unemployment insurance on the same graph. It starts to complicate what the data is showing by saying recipiency is just one dimension.
3. (Highlit line plot) State variation line plot: This adds in 51 lines to the plot to show that there's a lot of variation in recipiency rates that goes into the federal average. Again, this aims to reinforce that this isn't just a quick fix, and some areas the problem is more acute than others.
4. (Bar) State count: Since everything so far has been in rates, I will show the actual counts of the insured unemployed at a fixed time point (12/2022). This will illustrate that rates are misleading because the vast majority of UI claims actually occur in 3 states: NY, TX, and CA.

### Why does recipiency not make sense?
5. (Line plot, with colored top): Zoom in on COVID and states and show that recipiency jumps way above 100% during COVID. By extending the graph into 2020-2023, the rates fully stop making sense, because more than 100% of eligible people start receiving benefits.
6. (Bar and line plot) Calculation of rates. This aims to visualize how the recipiency rate is calculated by showing a line of the number of insured unemployed and the U-3 unemployed counts at the federal level. It takes the mean value across a time point of the U-3 rate and then divides a different time point to generate a range, resulting in a percentage.
    - This may be cut depending on data difficulties as it relies on the ETA-539 report with suspect data.
7. (Line graph): Show the states lines again in a different color, using the Bell et. al., 2021 preferred metric to better show what happens. I'll include a colored dot at the end (just 12/2022) to highlight the point in Chart 8.
8. (Lollipop plots showing change): Alternative formulation lollipop for each state, showing the change at 12/2022 between the two metrics. 
9. (Chloropleth sqaures map) Mapping recipiency compared to average across the country to start to introduce geographic variation. It shows that some of the difference is related to different states. This loosely maps onto political leaning, so will be obviously interpretable, but I will not plot political leaning.

## What form do you envision your final deliverable taking? (An article incorporating the images? A poster? An infographic?)
An article