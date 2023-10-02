# vue3安裝步驟

## 安裝npm
下載好官網的npm安裝
配置好環境變數

## 安裝npm套件
### 安裝vue本體
npm install vue@next
### 安裝指令功能
npm install -g @vue/cli
### 安裝連線用套件
npm install axios

## 使用指令
### 創建基礎專案
vue create <專案名稱>

### 後cd進到資料夾[編輯檔案]
* [vue.config.js](./origin/vue.config.js)
* components底下是組件
* 最後組合在[app.vue](./origin/src/App.vue)下

### 啟動服務
npm run serve  

# 連接API
範例[Apilnteraction.vue](./origin/src/components/ApiInteraction.vue)

詳細的註解
```
<template>
  <div>
    <h1>Vue 3 + Axios 範例</h1>
    <p>點擊按鈕以獲取數據</p>
    <button @click="getData">獲取數據</button>
    <div v-if="loading">
      <p>正在載入中...</p>
    </div>
    <div v-else>
      <h2>數據結果</h2>
      <ul>
        <li v-for="item in data" :key="item.id">{{ item.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const data = reactive([]); // 使用 reactive 函式將 data 變數轉換為響應式對象，用於儲存獲取到的數據
    const loading = reactive(false); // 使用 reactive 函式將 loading 變數轉換為響應式對象，用於控制載入狀態

    const getData = async () => {
      loading.value = true; // 設置 loading 為 true，顯示載入中的訊息
      try {
        const response = await axios.get('https://api.example.com/data'); // 使用 Axios 發送 GET 請求獲取數據
        data.value = response.data; // 將獲取到的數據存儲到 data 變數中
      } catch (error) {
        console.error(error); // 如果請求出錯，將錯誤訊息輸出到控制台
      }
      loading.value = false; // 請求完成後，將 loading 設置為 false，顯示數據結果
    };

    return {
      data,
      loading,
      getData,
    };
  },
};
</script>

```