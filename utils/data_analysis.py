import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style('darkgrid')

def save_plots_from_df(path):
    df = pd.read_csv(path, parse_dates=['ds'] if 'ds' in pd.read_csv(path, nrows=1).columns else None)
    imgs = []
    os.makedirs('static/images', exist_ok=True)

    # time series: vehicle_count vs ds (if exists)
    if 'ds' in df.columns and 'vehicle_count' in df.columns:
        plt.figure(figsize=(8,3))
        df.set_index('ds')['vehicle_count'].resample('H').mean().plot()
        p = 'static/images/ts_vehicle_count.png'
        plt.title('Vehicle Count over Time')
        plt.savefig(p, bbox_inches='tight')
        plt.close()
        imgs.append(p)

    # heatmap: correlation
    numeric = df.select_dtypes(include=['int64','float64'])
    if numeric.shape[1] > 1:
        plt.figure(figsize=(6,5))
        sns.heatmap(numeric.corr(), annot=True)
        p = 'static/images/heatmap_corr.png'
        plt.title('Correlation Heatmap')
        plt.savefig(p, bbox_inches='tight')
        plt.close()
        imgs.append(p)

    # day of week bar if hour/day present
    if 'hour' in df.columns:
        plt.figure(figsize=(6,3))
        df.groupby('hour')['vehicle_count'].mean().plot(kind='bar')
        p = 'static/images/hourly_avg.png'
        plt.title('Avg Vehicles by Hour')
        plt.savefig(p, bbox_inches='tight')
        plt.close()
        imgs.append(p)

    return imgs


def summarize_data(path):
    df = pd.read_csv(path)
    summary = {
        'rows': int(df.shape[0]),
        'columns': list(df.columns),
    }
    if 'vehicle_count' in df.columns:
        summary['vehicle_mean'] = float(df['vehicle_count'].mean())
        summary['vehicle_max'] = int(df['vehicle_count'].max())
    return summary
