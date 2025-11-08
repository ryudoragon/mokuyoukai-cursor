# 日報・週報生成システム

Cursor講座で作成した日報・週報の自動生成システムです。

## プロジェクト構成

```
プロジェクトルート/
├── input/              # 入力データ
│   ├── 日報テンプレ.md
│   └── 2025-11-08.md
├── output/             # 出力データ
│   ├── 2025-11-03_日報.md
│   ├── 2025-11-03_週報.md
│   ├── 2025-11-04_日報.md
│   ├── task_analysis.html
│   └── プロジェクト説明資料.md
├── calculate_dates.py  # 日付計算スクリプト
└── fix_dates.py        # 日付修正スクリプト
```

## 機能

- 日報の自動生成
- 週報の自動生成
- タスク分析の可視化（HTML）
- Marp形式のプレゼンテーション資料

## GitHub Pagesでの公開方法

### 方法1: リポジトリのSettingsから設定（推奨）

1. リポジトリの **Settings** タブを開く
2. 左メニューの **Pages** を選択
3. **Source** セクションで以下を設定：
   - **Branch**: `master` を選択
   - **Folder**: `/ (root)` を選択
4. **Save** をクリック

数分後、以下のURLでアクセスできます：
`https://ryudoragon.github.io/mokuyoukai-cursor/`

### 方法2: docsフォルダを使用

1. `output`フォルダを`docs`にリネーム（または`docs`フォルダを作成してファイルをコピー）
2. リポジトリのSettings > Pagesで：
   - **Branch**: `master` を選択
   - **Folder**: `/docs` を選択
3. **Save** をクリック

### 公開されるファイル

- `output/task_analysis.html` - タスク分析ページ
- `output/プロジェクト説明資料.md` - Marp形式のプレゼンテーション資料
- その他の日報・週報ファイル

## 使用方法

### 日付計算

```bash
python calculate_dates.py
```

### 日付修正

```bash
python fix_dates.py
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

