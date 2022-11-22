# PostgreSQL_backup
# 備份設置流程

- 將pg_pass.conf 放在 APPDATA 路徑下 (APPDATA 路徑可以用`echo %APPDATA%`)
- `pg_pass.conf` 的內容有在folder 裏面
- `backup.exe` 可以不需要修改只要修改`psqlsetup.json`裡面的內容即可
- 時程設置路徑：控制台> 系統及安全> 排程 >建立工作 >命名>設定每天重複>動作放入我的exe擋並且要指定路徑到`psqlsetup.json`的folder

# 架設網頁

- 要先連外網將環境全部載下來 `pip install -r requirements.txt`
- cmd 輸入 `ipconfig`找IPV4 並且將之當作server
    - EX: `python [manage.py](http://manage.py) runserver  IP:8000`
- [`settings.py`](http://settings.py) 裡面的資料庫要改內容成現在的資料庫
