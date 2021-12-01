# twitter-auto-good

## 準備

### Twitter APIの申請をおこなう

Twitterにログインした状態で下記URLからCreate an app
https://developer.twitter.com/en/apps/

### 必要情報を入力

```
Settings
App permissions　の項目を　Read + Post　へ変更する

Access Token and Secret
generate
```

表示された情報を`ConsumerKey/Secret/AccessToken/AccessTokenSecret`を取得し、
ソース内の`***`と置き換える

## 実行
python twitter.py 
