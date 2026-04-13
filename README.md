# chigasaki-beach-weather (Streamlit Version)

茅ヶ崎ヘッドランド（Tバー）の波情報・天気・潮汐を表示するWebアプリです。
Windows環境で動作確認を行い、iPhoneなどのスマートフォンからも利用可能です。

## 必要要件

- Windows PC
- Python 3.8以上

## セットアップ手順（Windows）

1.  **Pythonのインストール**
    *   まだインストールしていない場合は、[Python公式サイト](https://www.python.org/downloads/)からインストーラーをダウンロードして実行してください。
    *   **重要**: インストール時に "Add Python to PATH" にチェックを入れてください。

2.  **プロジェクトフォルダへの移動**
    *   コマンドプロンプト（またはPowerShell）を開きます。
    *   このフォルダ (`Surf90Chigasaki_Streamlit`) まで移動します。
        ```cmd
        cd path\to\Surf90Chigasaki_Streamlit
        ```

3.  **ライブラリのインストール**
    *   以下のコマンドを実行して、必要なツール（Streamlitなど）をインストールします。
        ```cmd
        pip install -r requirements.txt
        ```

## アプリの起動方法

1.  **アプリの実行**
    *   以下のコマンドを入力します。
        ```cmd
        streamlit run app.py
        ```

2.  **ブラウザで確認**
    *   自動的にブラウザが立ち上がり、アプリが表示されます。
    *   もし立ち上がらない場合は、画面に表示されるURL（例: `http://localhost:8501`）をブラウザのアドレスバーに入力してください。

## アプリの終了

*   コマンドプロンプトの画面で `Ctrl + C` を押すと終了します。
