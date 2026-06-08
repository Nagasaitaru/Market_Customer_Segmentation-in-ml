import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(filepath):

    df = pd.read_csv(filepath)

    print(df.head())

    return df

def preprocess_data(df):

    df = df.copy()

    df['Genre'] = df['Genre'].map({
        'Male':0,
        'Female':1
    })

    features = [
        'Genre',
        'Age',
        'Annual Income (k$)',
        'Spending Score (1-100)'
    ]

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(
        df[features]
    )

    return scaled_data, df