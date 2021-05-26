import pandas as pd
from data.helper.dataframe_columns import FENCERS_RANKINGS_DF_COLS, FENCERS_RANKINGS_MULTI_INDEX
from data.helper.dataframe_columns import convert_list_to_dataframe_with_multi_index

date = 'May_13_2021'
div_name = 'all_womens_foil'

# from data.load_csv import orig_tournament_df, orig_bout_df, orig_fencer_bio_df, orig_fencer_rankings_df
def load_original_data():
    """Loads original data as pd.Dataframes"""
    orig_bout_df = pd.read_csv('data/initial_data/'+div_name + '_bout_data_' + date+'.csv')
    orig_tournament_df = pd.read_csv(
        'data/initial_data/'+div_name + '_tournament_data_' + date+'.csv')
    orig_fencer_bio_df = pd.read_csv(
        'data/initial_data/'+div_name + '_fencer_bio_data_' + date+'.csv')
    init_rankings_df = pd.read_csv(
        'data/initial_data/'+div_name + '_fencer_rankings_data_' + date+'.csv')

    orig_fencer_rankings_df = convert_list_to_dataframe_with_multi_index(
        init_rankings_df.values.tolist(), FENCERS_RANKINGS_DF_COLS, FENCERS_RANKINGS_MULTI_INDEX)

    orig_tournament_df.df_name = "Tournament Dataframe"
    orig_tournament_df._metadata += ['df_name']
    orig_bout_df.df_name = "Bouts Dataframe"
    orig_fencer_bio_df.df_name = "Fencer Bio Dataframe"
    orig_fencer_rankings_df.df_name = "Fencer Rankings Dataframe"

    return orig_tournament_df, orig_bout_df, orig_fencer_bio_df, orig_fencer_rankings_df


# from data.load_csv import cleaned_tournament_df, cleaned_bout_df, cleaned_fencer_bio_df, cleaned_fencer_rankings_df
def load_cleaned_data():
    """Returns data after cleanup from data-cleanup.ipynb"""
    cleaned_bout_df = pd.read_csv('data/cleaned_data/'+div_name + '_bout_data_' + date+'_cleaned.csv')
    cleaned_tournament_df = pd.read_csv(
        'data/cleaned_data/'+div_name + '_tournament_data_' + date+'_cleaned.csv')
    cleaned_fencer_bio_df = pd.read_csv(
        'data/cleaned_data/'+div_name + '_fencer_bio_data_' + date+'_cleaned.csv')
    init_cleaned_rankings_df = pd.read_csv(
        'data/cleaned_data/'+div_name + '_fencer_rankings_data_' + date+'_cleaned.csv')

    cleaned_fencer_rankings_df = convert_list_to_dataframe_with_multi_index(
        init_cleaned_rankings_df.values.tolist(), FENCERS_RANKINGS_DF_COLS, FENCERS_RANKINGS_MULTI_INDEX)

    cleaned_tournament_df.df_name = "Tournament Dataframe"
    cleaned_tournament_df._metadata += ['df_name']
    cleaned_bout_df.df_name = "Bouts Dataframe"
    cleaned_fencer_bio_df.df_name = "Fencer Bio Dataframe"
    cleaned_fencer_rankings_df.df_name = "Fencer Rankings Dataframe"
    
    return cleaned_tournament_df, cleaned_bout_df, cleaned_fencer_bio_df, cleaned_fencer_rankings_df


def load_split_data():
    """Returns training and testing data in bout dataframes"""
    training_bouts_df = pd.read_csv('data/cleaned_data/'+div_name + '_bout_data_' + date+'_training.csv')
    testing_bouts_df = pd.read_csv('data/cleaned_data/'+div_name + '_bout_data_' + date+'_testing.csv')
    training_bouts_df.df_name = "Training Bout Data"
    training_bouts_df._metadata += ['df_name']
    testing_bouts_df.df_name = "Testing Bout Data"
    return training_bouts_df, testing_bouts_df
   