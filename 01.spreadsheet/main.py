import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(creds)

#編集するスプレッドシートを設定
# sheet_id = 'ID' (IDで取得)
sheet_url = 'URL'  # URLで取得

#設定したスプレッドシートを開く
# wb = gc.open_by_key(sheet_id) (スプレッドシートのIDを指定してワークブックを選択)
wb = gc.open_by_url(sheet_url)  # URLを指定してワークブックを開く

#対象のスプレッドシートから1番目に当たるシートを取得
ws0 = wb.get_worksheet(0)

#シートの複製
wb.duplicate_sheet(source_sheet_id=ws0.id, new_sheet_name='sheet', insert_sheet_index=1)

ws1 = wb.get_worksheet(1)
date = ['2022/01', '2022/02', '2022/03', '2022/04', '2022/05', '2022/06']

for n in range(len(date) -1):
  value = date[n]
  for m in [chr(ord("B") + n)]:
    row1 = f'{m}2'
    ws1.update_acell(row1, value)

