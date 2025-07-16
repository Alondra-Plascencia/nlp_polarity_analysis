import pandas as pd
import matplotlib.pyplot as plt

def load_sentiment_results(csv_path):
    """
    Loads the CSV file containing the sentiment summary data.
    """
    df = pd.read_csv(csv_path)
    return df

def compute_totals(df, neg_col='NEG', neu_col='NEU', pos_col='POS'):
    """
    Computes the total count for each sentiment category.
    """
    total_neg = df[neg_col].sum()
    total_neu = df[neu_col].sum()
    total_pos = df[pos_col].sum()
    return [total_neg, total_neu, total_pos]

def plot_sentiment_pie_chart(totals, labels, colors, title, output_path):
    """
    Generates a pie chart and saves it as a PDF file without displaying it.
    """
    plt.figure(figsize=(8,8))
    plt.pie(
        totals,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        textprops={'fontsize': 12}
    )
    plt.title(title, fontsize=16)
    plt.legend(
        [f'{label}: {size}' for label, size in zip(labels, totals)],
        title="Totals",
        loc="upper right",
        fontsize=12
    )
    plt.savefig(output_path, format='pdf')
    plt.close()

def compute_totals_5categories(df):
    """
    Sums the totals for the 5-category model and groups them into
    Negative, Neutral, and Positive overall sentiment.

    It uses the correct column names from the CSV.
    """
    total_neg = df['very_negative_count'].sum() + df['negative_count'].sum()
    total_neu = df['neutral_count'].sum()
    total_pos = df['positive_count'].sum() + df['very_positive_count'].sum()
    return [total_neg, total_neu, total_pos]
