# 請說明 P, NP, NP-Complete, P=?NP 是什麼意思？愈詳細愈好

## P(Polynomial Time)
+ P 是指那些可以在「多項式時間」內解決的問題集合。
+ 如果演算法的運行時間以演算法輸入大小的多項式表達式為上限，即對於某個正常數 k，T(n)=O(nᵏ)，則稱該演算法具有多項式時間。
+ 常見例子:各類排序問題、圖的最短路徑、矩陣相乘。

## NP（Nondeterministic Polynomial Time）
+ NP 是指可以在多項式時間內驗證解答正確性的問題集合。
+ 這些問題的解可以在一個假設的「非確定性圖靈機」上在多項式時間內找到。這種非確定性機器能夠「猜測」正確的解，並立即驗證這個解。儘管現實中的計算機不能進行這種「猜測」，但仍然能夠有效地驗證已給出的解。
+ 常見例子:旅行商問題、背包問題、SAT問題（布爾滿足問題）。
### NP 與 P
P 包含在 NP 中，因為如果一個問題在多項式時間內可解決，則解決方案透過簡單地解決問題，也可以在多項式時間內驗證。
目前尚未證明P < NP，即存在無法在多項式時間內解決的決策問題，雖然可以在多項式時間內檢查其解決方案。

## NP-Complete(NP-C或NPC)
+ 是計算複雜度理論中決定性問題的等級之一。
+ NP 問題的子集合，代表難度最高的 NP 問題。
+ 是NP與NP-hard的交集。
+ 所有NP問題都可以在多項式時間內被歸約（reduce to）為NP完備問題。
+ 常見例子：旅行商問題 (TSP)、背包問題 (Knapsack Problem)、頂點覆蓋問題（Vertex cover）

## P=?NP
P=NP 是計算理論中尚未解決的問題之一，被認為是數學和計算科學中最重要的公開問題之一。

問題核心：所有在多項式時間內能夠驗證的問題（NP）是否也能在多項式時間內解決（P）。

### 如果 P=NP
+ 每個 NP 問題都能找到一個多項式時間的解法。
+ 即許多實際中困難的問題將能被快速解決。
### 如果 P≠NP
+ 有些問題在多項式時間內可以驗證解答，卻無法解決。
+ 計算複雜性理論將維持現有的結構。
### 目前的狀態
+ P=NP 與 P≠NP，皆尚未成功證明。
+ P=NP 問題被列為克雷數學研究所的七個「千禧年懸賞問題」之一。

## 參考資料
- [Wikipedia: Cook–Levin theorem ](https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem)
- [ChatGPT: P / NP / NP-Complete問答錄 ](https://chatgpt.com/share/67453247-61ac-8012-8f48-49838d9c52e8)
- [NP完備](https://zh.wikipedia.org/zh-tw/NP%E5%AE%8C%E5%85%A8)