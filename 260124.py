fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# 글자수 변동
sns.lineplot(data=period_df, x='date', y='text_len', ax=ax1)
ax1.set_title('Text Length Over Time')
ax1.grid(True)

# 작성시간 (write_time을 hour로 변환 가정)
period_df['hour'] = pd.to_datetime(period_df['write_time']).dt.hour
sns.boxplot(data=period_df, x='weekday', y='hour', ax=ax2)  # weekday 컬럼 추가 필요
ax2.set_title('Write Time by Weekday')

plt.tight_layout()
plt.show()
