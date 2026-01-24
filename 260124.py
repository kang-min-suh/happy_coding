import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

df = pd.read_csv('your_journal.csv')  # date, main_category, initial_words, text_len, write_time 컬럼 가정
df['date'] = pd.to_datetime(df['date'])

age_50_date = datetime(2025, 1, 1)  # 50세 되는 실제 날짜로 변경
start_date = age_50_date - timedelta(days=180)  # 6개월 전
end_date = age_50_date + timedelta(days=180)    # 6개월 후

period_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)].copy()
period_df.sort_values('date', inplace=True)
