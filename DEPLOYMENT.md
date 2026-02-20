# iPhoneでの利用方法 & Web公開手順

iPhoneのホーム画面に追加してアプリのように使うには、まずインターネット上に公開する必要があります。
StreamlitCommunity Cloud（無料）を使うのが最も簡単です。

## ステップ1: GitHubへのアップロード

Streamlit Cloudを使うには、ソースコードをGitHubにアップロードする必要があります。

1.  [GitHub](https://github.com/)のアカウントを作成します。
2.  新しいリポジトリ（New Repository）を作成します（PublicでOK）。
3.  このフォルダ内のファイル（`app.py`, `requirements.txt`など）をアップロードします。

## ステップ2: Streamlit Cloudへのデプロイ（公開）

1.  [Streamlit Cloud](https://streamlit.io/cloud)にアクセスし、GitHubアカウントでログインします。
2.  「New app」ボタンを押します。
3.  先ほど作成したGitHubリポジトリを選択します。
4.  Main file path に `app.py` が設定されていることを確認し、「Deploy!」を押します。
5.  数分待つと、全世界からアクセスできるURL（例: `https://surf90chigasaki.streamlit.app`）が発行されます。

## ステップ3: iPhoneのホーム画面に追加

これが最終ゴールです。

1.  iPhoneのSafariで、発行されたURL（ステップ2のURL）を開きます。
2.  画面下部の「共有ボタン」（四角から矢印が出ているアイコン）をタップします。
3.  メニューをスクロールして「**ホーム画面に追加**」を選択します。
4.  名前（Surf90Chigasaki）を確認して「追加」をタップします。
5.  ホーム画面にアイコンが追加され、タップするとアプリのように全画面に近い状態で起動します。

---

### 注意点
*   Streamlit Cloudの無料版は、一定期間アクセスがないとスリープ状態になります（アクセスすれば再起動します）。
*   本アプリのデータは現在「モック（ダミーデータ）」です。実際の波情報を表示するには、外部APIとの連携が必要になります。
