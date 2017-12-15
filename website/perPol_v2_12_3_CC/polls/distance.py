import pandas as pd
import numpy as np
import math
from us import states as us_states


distance_cols = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

soc_cols = ['1','3','4','8','9','12','15','16','17','19']
econ_cols = ['2','5','6','7','10','11','13','14','18','20']

states_map = us_states.mapping('abbr', 'name')

def similarity_score(row,user,cols):
    """
    A simple euclidean distance function
    """
    inner_value = 0
    for k in cols:
        inner_value += (row[k] - user[k]) ** 2
    similarity = round((50-math.sqrt(inner_value))*2, 1)
    return similarity


def candidate_distance(candidate_df,user_inputs):
    
    candidate_distance = {'name':candidate_df['candidate'],
                      'year':candidate_df['year'],
                      'state':candidate_df['state'].map(states_map),
                      'overall_sim':candidate_df.apply(similarity_score, user=user_inputs, cols=distance_cols, axis=1),
                      'social_sim':candidate_df.apply(similarity_score, user=user_inputs, cols=soc_cols, axis=1),
                      'econ_sim':candidate_df.apply(similarity_score, user=user_inputs, cols=econ_cols, axis=1),
                      'battleground':candidate_df['battleground'].apply(lambda x: 'Yes' if x==1 else 'No'),
                      'return_on_donation':candidate_df['relative_impact_donation'].apply(lambda x: round(x,1)),
                      'election_pred':candidate_df['win_prob_candidate'].apply(lambda x: 0 if math.isnan(x) else float((round(x,3)*100))),
                      'party':candidate_df['party_full']}
    df_candidate_dists = pd.DataFrame(candidate_distance).sort_values(['overall_sim'])
    return df_candidate_dists

def senator_distance(senator_df,user_inputs):
    
    senator_distance = {'name':senator_df['full_name'].apply(lambda x: x.replace('_', ' ')),
                      'state':senator_df['state'].map(states_map),
                      'overall_sim':senator_df.apply(similarity_score, user=user_inputs, cols=distance_cols, axis=1),
                      'social_sim':senator_df.apply(similarity_score, user=user_inputs, cols=soc_cols, axis=1),
                      'econ_sim':senator_df.apply(similarity_score, user=user_inputs, cols=econ_cols, axis=1),
                      'party':senator_df['party_full']}
    df_senator_dists = pd.DataFrame(senator_distance).sort_values(['overall_sim'])
    return df_senator_dists
