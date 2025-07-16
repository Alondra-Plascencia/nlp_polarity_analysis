import pandas as pd
import matplotlib.pyplot as plt

def load_sentiment_results(csv_path):
    """
    Loads the CSV with the sentiment summary data.
    """
    df = pd.read_csv(csv_path)
    return df

def compute_totals(df, neg_col='NEG', neu_col='NEU', pos_col='POS'):
    """
    Computes the total counts for each sentiment.
    """
    total_neg = df[neg_col].sum()
    total_neu = df[neu_col].sum()
    total_pos = df[pos_col].sum()
    return [total_neg, total_neu, total_pos]

def plot_sentiment_pie_chart(totales, labels, colors, title, output_path):
    """
    Plots a pie chart and saves it as a PDF, no display or print.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8,8))
    plt.pie(
        totales,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        textprops={'fontsize': 12}
    )
    plt.title(title, fontsize=16)
    plt.legend(
        [f'{label}: {size}' for label, size in zip(labels, totales)],
        title="Totales",
        loc="upper right",
        fontsize=12
    )
    plt.savefig(output_path, format='pdf')
    plt.close()

def compute_totals_5categories(df):
    """
    Suma totales para 5 categorías y agrupa en Negativo, Neutro, Positivo.
    Usa los nombres de columna correctos del CSV.
    """
    total_neg = df['muy_negativo_count'].sum() + df['negativo_count'].sum()
    total_neu = df['neutro_count'].sum()
    total_pos = df['positivo_count'].sum() + df['muy_positivo_count'].sum()
    return [total_neg, total_neu, total_pos]

