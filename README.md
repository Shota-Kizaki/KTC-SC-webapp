# KTC-SC-webapp

このリポジトリは、langchainとAzure OpenAIを使用したチャットbotの管理と実際にチャットができるwebサイトです。django

## 概要
このプロジェクトは、langchainとAzure OpenAIを組み合わせて作成されたチャットbotの管理と、実際にチャットを行うためのWebサイトです。Djangoフレームワークを使用して開発されています。

## インストール
以下の手順に従って、プロジェクトをローカル環境にセットアップしてください。

1. リポジトリをクローンします。
    ```shell
    git clone https://github.com/your-username/KTC-SC-webapp.git
    ```

2. 仮想環境を作成し、必要なパッケージをインストールします。
    ```shell
    cd KTC-SC-webapp
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. データベースをマイグレーションします。
    ```shell
    python manage.py migrate
    ```

4. サーバーを起動します。
    ```shell
    python manage.py runserver
    ```

5. ブラウザで `http://localhost:8000` にアクセスして、Webサイトを利用できます。

## 使用方法
1. Webサイトにアクセスすると、チャットbotの管理画面が表示されます。
2. チャットbotの設定やトレーニングデータの管理を行います。
3. チャットを行うには、Webサイト上でチャットボットと対話することができます。

## ライセンス
このプロジェクトは [MITライセンス](LICENSE)のもとで公開されています。

詳細な情報や貢献方法については、[CONTRIBUTING.md](CONTRIBUTING.md)を参照してください。
