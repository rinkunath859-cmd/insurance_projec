import pandas as pd

def clean_data(df):
    # Drop unnecessary columns
    df = df.drop(columns=['person_id'], errors='ignore')
    
    # Handle missing values
    df = df.fillna(0)
    
    return df


def encode_data(df):
    # Convert categorical to numeric
    df = pd.get_dummies(df, drop_first=True)
    return df