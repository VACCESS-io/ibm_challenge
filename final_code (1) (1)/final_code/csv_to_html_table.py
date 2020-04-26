import pandas as pd
from datetime import datetime

def apply_green(s):
    color = 'green'
    if s == 'Status.UNDER_CONTROL':
        color = 'green'
    elif s == 'Status.ABOVE_THRESHOULD':
        color = 'yellow'
    elif s == 'Status.RED_ALERT':
        color = 'red'
    return f'background-color: {color}'

columns = ['name', 'date', 'count', 'status']
today_str = datetime.today().strftime("%Y-%m-%d")
df = pd.read_csv('Florida_prediction_data.csv')
today_data = df[df['date'] == today_str]
today_data['count'] = today_data['count'].astype(int)
today_data = today_data.drop(columns='date')
today_data = today_data.rename(columns={'name': 'County Name','count':'Number of Infected Cases'})
today_data = today_data.style.applymap(apply_green, subset=['status'])
print(today_data.hide_index().render())


