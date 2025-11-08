from datetime import datetime, timedelta

# 2025-11-08が土曜日か確認
base_date = datetime(2025, 11, 8)
print(f"2025-11-08: {base_date.strftime('%Y-%m-%d %A')}")

# 過去7日間の日付を計算（平日のみ）
dates = []
for i in range(7):
    date = base_date - timedelta(days=i)
    weekday = date.weekday()  # 0=月曜日, 6=日曜日
    if weekday < 5:  # 平日のみ（月曜日～金曜日
        dates.append({
            'date': date.strftime('%Y-%m-%d'),
            'weekday': weekday,
            'weekday_jp': ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日'][weekday]
        })

print("\n過去一週間の平日:")
for d in dates:
    print(f"{d['date']} ({d['weekday_jp']})")

# ファイル名のマッピング
print("\nファイル名のマッピング:")
current_files = ['2025-11-04', '2025-11-05', '2025-11-06', '2025-11-07', '2025-11-08']
for i, d in enumerate(dates):
    if i < len(current_files):
        print(f"{current_files[i]}_日報.md -> {d['date']}_日報.md ({d['weekday_jp']})")

