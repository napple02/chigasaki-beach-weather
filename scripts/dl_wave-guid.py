import urllib.request
import csv
import json
import io

# 取得したい海域のCSV URL
url = "https://www.data.jma.go.jp/waveinf/data/Guid/csv/wave_guid_19.csv"

# 1. データをダウンロード
response = urllib.request.urlopen(url)
raw_data = response.read()

# 文字化け対策（気象庁の海洋系データはShift-JISのケースがあるため念のためフォールバック）
try:
    csv_text = raw_data.decode('utf-8')
except UnicodeDecodeError:
    csv_text = raw_data.decode('shift_jis')

# 2. CSVを辞書型のリスト（JSONと同じ構造）に変換
reader = csv.DictReader(io.StringIO(csv_text))
data_list = [row for row in reader]

# 3. JSON文字列に変換
json_output = json.dumps(data_list, ensure_ascii=False, indent=2)

# 結果の確認（長くなるため最初の500文字だけ表示）
print("--- 変換されたJSONデータ ---")
print(json_output[:500])

# ==========================================
# （オプション）JSONファイルとしてローカルに保存する場合
# ==========================================
save_file = 'wave_guid_19.json'
with open(save_file, 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=2)
print(f"\n{save_file} としてJSON形式で保存しました。")
