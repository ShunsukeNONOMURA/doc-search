# ドキュメント検索アプリ
ドキュメントを登録してそのドキュメントを検索するアプリケーションを構築する。  
将来的にはRAGアプローチによるチャットベースでの検索等を実現する。

## 構築サーバー
- 8080 pgadmin
- 5432 postgresql
- 9200 opensearch
- 5601 opensearch dashboards

## やること
- [ ] ドキュメント構造定義
- [ ] ドキュメント手動登録（テキストのみ）
- [ ] 全文検索動作確認
- [ ] k-nn検索検証
- [ ] k-nn検索機能のアプリ化
- [ ] LLM利用検証
- [ ] LangChain検証
- [ ] ドキュメント登録機能作成

## 今がんばらないこと
- コードの精査（後でリファクトなりする）

## メモ
### max virtual memory areas vm.max_map_count [65530] is too low
https://blog.interfamilia.co.jp/2021/05/11/Docker%E4%B8%8A%E3%81%AE-Elasticsearch-%E3%81%8C%E8%B5%B7%E5%8B%95%E3%81%A7%E3%81%8D%E3%81%AA%E3%81%84%E3%81%A8%E3%81%8D%E3%81%AE%E5%AF%BE%E5%87%A6%E6%B3%95/

```
sudo echo "262144" | sudo tee /proc/sys/vm/max_map_count
```