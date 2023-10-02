# buckets站點API

## 使用python fastAPI建立站點
! 此站點必須建立在Google GCP上，並建立PVC網路

### [fastAPI檔](main.py) 建立一個upload站點進行處理
* 參數給dir名可以用登入等等做設定，這裡直接作為參數傳送

* 上傳檔案在特定位置用字串給予可以用瀏覽器上傳後直接使用。

* 檔案檔名直接搬用，也能用其他固定檔名代替。

* 參數與檔案最後串成字串
  '{dir}/{file.filename}'

### 使用[upload_file](upload_file.py)進行連接呼叫把檔案上傳
透過建好的API上傳檔案，用2進制大部分檔案都支援。
* 上傳檔案會用2進制open('rb')


### 使用[get_file](get_file.py) 直接從buckets下取得檔案
直接使用GCP的基本驗證取得資料(目前設定似乎只有取得檔案可以不用驗證檔上傳不行)
* 這裡用預設認證方式可以直接通過進行下載