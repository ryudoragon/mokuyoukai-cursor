from datetime import datetime, timedelta

# 2025-11-08が土曜日か確認
base_date = datetime(2025, 11, 8)
print(f"2025-11-08: {base_date.strftime('%Y-%m-%d %A')}")

# 過去7日間の日付を計算
dates = []
for i in range(7):
    date = base_date - timedelta(days=i)
    dates.append({
        'date': date.strftime('%Y-%m-%d'),
        'weekday': date.strftime('%A'),
        'weekday_jp': ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日'][date.weekday()]
    })

print("\n過去7日間:")
for d in dates:
    print(f"{d['date']} ({d['weekday_jp']})")

