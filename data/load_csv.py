import pandas as pd
from data.helper.dataframe_columns import FENCERS_RANKINGS_DF_COLS, FENCERS_RANKINGS_MULTI_INDEX
from data.helper.dataframe_columns import convert_list_to_dataframe_with_multi_index

date = 'May_13_2021'
div_name = 'all_womens_foil'

orig_bout_df = pd.read_csv('data/'+div_name + '_bout_data_' + date+'.csv')
orig_tournament_df = pd.read_csv(
    'data/'+div_name + '_tournament_data_' + date+'.csv')
orig_fencer_bio_df = pd.read_csv(
    'data/'+div_name + '_fencer_bio_data_' + date+'.csv')
init_rankings_df = pd.read_csv(
    'data/'+div_name + '_fencer_rankings_data_' + date+'.csv')

orig_fencer_rankings_df = convert_list_to_dataframe_with_multi_index(
    init_rankings_df.values.tolist(), FENCERS_RANKINGS_DF_COLS, FENCERS_RANKINGS_MULTI_INDEX)

orig_tournament_df.df_name = "Tournament Dataframe"
orig_tournament_df._metadata += ['df_name']
orig_bout_df.df_name = "Bouts Dataframe"
orig_fencer_bio_df.df_name = "Fencer Bio Dataframe"
orig_fencer_rankings_df.df_name = "Fencer Rankings Dataframe"

# from data.load_csv import orig_tournament_df, orig_bout_df, orig_fencer_bio_df, orig_fencer_rankings_df
