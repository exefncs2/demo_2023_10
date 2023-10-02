import requests

# 文件路径
file_path = '<要送的檔案>'

# 参数
params = {
    'dir': '<dir名稱>'
}

#  站點URL
url = 'http://127.0.0.1:8000/upload' # 使用main的api

# 發送請求
with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files, params=params)

# 檢查回應
if response.status_code == 200:
    print('文件上传成功！')
else:
    print('文件上传失败。')
    print(response.status_code)