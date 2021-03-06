# sps

![](https://github.com/shiotomo/sps/workflows/GitHub%20Actions/badge.svg)

## このアプリについて

speedtest-cliを利用して、ネットワーク回線の状態を集計・監視・分析するシステムです。
定期的にspeedtestを実行し、その結果をAPI経由やmonitor経由で確認できます。

## 使用技術

- Python3
- Flask
- React
- Yarn
- Node.js
- SQlite

## 利用方法

**.envの設定**

`.env.sample`をコピーして`.env`を作成します。  
`DATABASE_URL`は利用したいデータベースに合わせて設定してください。デフォルトはSQliteを利用しています。
`FLASK_ENV`は本番環境で利用する場合は、`production`を指定してください。

**build**

```
docker-compose build
```

**monitorの設定**

```
docker-compose run monitor
```

**apiとbatchの実行**
```
docker-compose up -d api batch
```