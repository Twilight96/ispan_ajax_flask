### Fork 本專案
1. 登入你的 GitHub 帳號。
2. 在本專案頁面的右上方，找到並點擊 「Fork」 按鈕。
3. 選擇你的個人帳號作為目的地。
4. （選擇性）你可以修改 Repository name。
5. 點擊 Create fork。

### 將專案 Clone 到本地電腦
回到你個人帳號下的該專案頁面（網址應該是 https://github.com/你的帳號/專案名稱），執行以下指令：
請將網址替換成你自己 Fork 後的專案網址

<pre>
git clone https://github.com/你的帳號/專案名稱.git
</pre>
進入專案資料夾
<pre>
cd 專案名稱
</pre>




### 如何執行本專案
1. 建立虛擬環境：`python -m venv venv`
2. 啟動環境：`venv\Scripts\activate` (Windows)
3. 安裝套件：`pip install -r requirements.txt`
4. 執行程式：`python app.py`
5. 專案架構
* models/：定義資料庫模型（SQLAlchemy Classes）。存放資料表結構與屬性定義的檔案。

* resources/：存放 Flask-RESTful 的 Resource 類別。這裡負責編寫 API 的邏輯處理，例如 GET、POST 等方法的具體實作。

* routes/：定義應用程式的路由與 Blueprint（藍圖）。負責將網址路徑（URL）映射到對應的處理函式或 Resource。

* static/：存放靜態資源檔案。包括 CSS 樣式表、JavaScript 腳本、圖片以及前端上傳的檔案等。

* templates/：存放 Jinja2 HTML 模板檔案。這是後端渲染網頁時所使用的 HTML 範本。

* venv/：Python 虛擬環境。存放專案獨立的套件庫，確保開發環境的一致性（此目錄通常不進行版本控制）。

* .env：環境變數設定檔。用於存放敏感資訊（如 Secret Key、資料庫連線字串、API 密鑰等）。

* .gitignore：Git 忽略清單。指定哪些檔案（如 venv/、__pycache__/、.env、.db 等）不應上傳至 GitHub。

* app.py：應用程式的入口點。負責初始化 Flask App、載入配置、註冊藍圖（Blueprint）並啟動伺服器。

* mydb.db：SQLite 資料庫檔案。存放專案的實體資料。

* README.md：專案說明文件（即本檔案）。

* requirements.txt：專案依賴套件清單。記錄專案運行所需的所有 Python 套件及其版本，方便環境部署。
