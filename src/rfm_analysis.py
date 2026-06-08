def create_rfm(df):

    df['Recency'] = 100 - df['Spending Score (1-100)']

    df['Frequency'] = df['Age']

    df['Monetary'] = df['Annual Income (k$)']

    return df