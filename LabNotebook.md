# Lab Notebook

Inspired by Abhishek Gupta's [talk](https://zenodo.org/record/4737535#.YJGjZn1KhN0) on Lab Notebooks at [csv,conf,v6](https://csvconf.com/), I have decided to maintain a lab notebook as part of this project to track more detailed, unfiltered notes. The aim of this notebook is not to be a polished presentation of the final product, but a history of its development including half-baked ideas and failed experiments/implementations. Entries will be ordered reverse-chronologically, with the most recent ones appearing at the top. 

# Entries 

### 05/20/2021

**Covid events?** 

In initial exploration noticed decline in tournament events in 2020 and 2021 (likely due to COVID). Created some graphics to explore that using pandas Periods. 

**Fencer Bout/Event Counts**

Since the data is very sparse, may need to focus on fencers with more events/bouts (may be hard to collaboratively filter a fencer who has results for only a single pool). Created counts for this and explored how much bout data would be lost if fencers with only a single result were dropped (either bouts containing a single or both fencers without multiple events)


### 05/13/2021

**Ideas for Data Exploration**

* Compute how often upsets happen 
* Compute statistics like how many fencers are left handed? Nationality distribution? Age distribution? 
* Compute upset data for each fencer, are some fencers more likely to win upsets? more likely to lose them? 


* get # of bouts between two fencers and create array with this data, plot as a heat map? 