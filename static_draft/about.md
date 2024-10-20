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
2. (Scatterplot) What is recipiency? This shows a few example people using synthetic data to describe what UI recipiency looks like on a week-to-week basis.
    - Note: this is a final plot. But individual claim utilization behavior is protected, so individual data cannot be collected.
3. (Stacked bar) State count: Since everything so far has been in rates, I will show the actual counts of the insured unemployed at a fixed time point (12/2022). This will illustrate that rates are misleading because the vast majority of UI claims actually occur in 3 states: NY, TX, and CA.
4. (Highlit line plot) State variation line plot: This adds in 51 lines to the plot to show that there's a lot of variation in recipiency rates that goes into the federal average. Again, this aims to reinforce that this isn't just a quick fix, and some areas the problem is more acute than others.

### What causes changes in recipiency?
5. (Line plot, with colored top): Zoom in on COVID and states and show that recipiency jumps way above 100% during COVID. By extending the graph into 2020-2023, the rates fully stop making sense, because more than 100% of eligible people start receiving benefits.
6. (Lasagna plot): Goes back to the states identified in 4 to highlight how their recipiency changed over COVID, using color to show the intensity. It highlights that there's a key break around the policy change.

### What can we do about it?
7. (Chloropleth sqaures map) Mapping recipiency compared to average across the country to start to introduce geographic variation. It shows that some of the difference is related to different states. This loosely maps onto political leaning, so will be obviously interpretable, but I will not plot political leaning.
8. (Faceted Density Plot): Shows the recipiency densities for the 6 states highlighted as key to the US UI system earlier. New Jersey jumps out as way higher than everyone else. I will describe in writing how NJ's administrative approaches have increased recipiency -- it's not just policy, but it's implrementation too.

## What form do you envision your final deliverable taking? (An article incorporating the images? A poster? An infographic?)
An article