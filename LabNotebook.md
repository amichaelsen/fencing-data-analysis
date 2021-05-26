# Lab Notebook

Inspired by Abhishek Gupta's [talk](https://zenodo.org/record/4737535#.YJGjZn1KhN0) on Lab Notebooks at [csv,conf,v6](https://csvconf.com/), I have decided to maintain a lab notebook as part of this project to track more detailed, unfiltered notes. The aim of this notebook is not to be a polished presentation of the final product, but a history of its development including half-baked ideas and failed experiments/implementations. Entries will be ordered reverse-chronologically, with the most recent ones appearing at the top. 

# Entries 

### 05/25/2021

**Collaborative Filtering Methods**

[Towards DataScience Article](https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0): Review of collab filtering methods 

--> using Surprise for SVD matrix factorization 

`Surprise` Docs:
* [Getting Started](https://surprise.readthedocs.io/en/stable/getting_started.html#load-from-folds-example)
* [Custom Dataset](https://surprise.readthedocs.io/en/stable/getting_started.html#use-a-custom-dataset)
* [Using Readers](https://surprise.readthedocs.io/en/stable/reader.html#surprise.reader.Reader)
* [SVD Doc page](https://surprise.readthedocs.io/en/stable/matrix_factorization.html?highlight=svd#surprise.prediction_algorithms.matrix_factorization.SVD)
### 05/24/2021 

**Train/Test Split**

Created a split by global time with ~80% bouts in dataset occuring before the date (tournaments were kept together) and all testing data (~20%) occurring strictly *after* all training example to avoid any data leakage. Should maybe come back and create a method for recreating the data split using different thresholds. 

### 05/21/2021

**Recommender System?** 

Recommender systems seem to most commonly be used to provide an ordered list of top recommended items from a list. In this context, that would be the fencers that a specific athlete is going to do best against in competition. In reality, the goal of this model is to predict given a fixed athlete, how are they predicted to do against another athlete in a tournament/pool (i.e. pick another athlete in the list)? Need to look into the methods available for a collab filtering models and how reasonable it is to pull that data from them. 

Should also compare to a baseline model predicting based on points as well as a either logistic (win/loss) or linear ('score' outcome) regression model feeding in fencers based on their statistics. 

**Data Train/Test Splits**

How to split train/test data for a collaborative filtering system? [Here](https://arxiv.org/pdf/2007.13237.pdf) is an arxiv article on the impacts of data splitting strategies on the evaluation of recommendation models. 

Data splitting strategies:
* last one item/basket - take last bout/pool (item/basket) for each user and reserve for training (and second to last for validation)
* **temporal global split** - choose a fixed time point with 80% items before and 20% after to use for testing (repeat with training to get validation set). 

The temporal global split is the more realistic one and recommended by the paper, will be the one to use for this model. Is accurate to the setting where we might have historical results data and want to predict outcomes in pools at the next event (here the temporal split is past/future). 

The paper also mentions different models used for collaborative filtering  
* NMF [7] and BPR [13] (classic)
    * [7] Daniel D Lee and H Sebastian Seung. 2001. Algorithms for non-negative matrix factorization. In NeurIPS. 556–562
    * [13] Steffen Rendle, Christoph Freudenthaler, Zeno Gantner, and Lars Schmidt-Thieme. 2009. BPR: Bayesian personalized ranking from implicit feedback. In UAI. 452–461.
* NeuMF [4], VAECF [9] and NGCF [24] (neural net) 
    * [4] Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu, and Tat-Seng Chua. 2017. Neural collaborative filtering. In WWW. 173–182.
    * [9] Dawen Liang, Rahul G Krishnan, Matthew D Hoffman, and Tony Jebara. 2018. Variational autoencoders for collaborative filtering. In WWW. 689–698
    * [24] Xiang Wang, Xiangnan He, Meng Wang, Fuli Feng, and Tat-Seng Chua. 2019. Neural graph collaborative filtering. In SIGIR. 165–174.

The paper also uses two evaluation metrics for recommender systems: NDCG@10 and Recall@10, both which focus on the ordering of top 10 recommendations for the system. Since this is not the true goal of the model in this setting, something like RMSE of predicted bout outcomes might be more applicable. 



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