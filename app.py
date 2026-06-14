import os
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

# --- WSGIアプリ本体 ---
def app(environ, start_response):
    method = environ.get("REQUEST_METHOD", "GET")
    result = ""

    if method == "POST":
        try:
            size = int(environ.get("CONTENT_LENGTH", 0))
            body = environ["wsgi.input"].read(size).decode("utf-8")
            params = parse_qs(body)

            height = float(params.get("height", ["0"])[0])
            weight = float(params.get("weight", ["0"])[0])

            if height < 0 or weight < 0:
                result = "<p style='color:red;'>0以上の数値を入力してください。</p>"
            elif height == 0 or weight == 0:
                result = "<p style='color:red;'>身長と体重は0より大きい数値を入力してください。</p>"
            else:
                h_m = height / 100
                bmi = weight / (h_m ** 2)

                if bmi < 18.5:
                    category = "低体重（やせ）"
                elif bmi < 25:
                    category = "普通体重"
                elif bmi < 30:
                    category = "肥満（1度）"
                elif bmi < 35:
                    category = "肥満（2度）"
                elif bmi < 40:
                    category = "肥満（3度）"
                else:
                    category = "肥満（4度）"

                result = f"<p>BMI: {bmi:.1f}（{category}）</p>"

        except Exception as e:
            result = f"<p style='color:red;'>入力エラー: {e}</p>"

    html = f"""<!DOCTYPE html>
    <html lang="ja">
      <head>
        <meta charset="utf-8">
        <title>あなたのBMIを測定してみましょう</title>
        <style>
          body {{ font-family: sans-serif; margin: 40px; background: #f9f9f9; }}
          h1 {{ background: #cde; padding: 10px; border-radius: 8px; }}
          form {{ margin-top: 20px; }}
          input[type=number] {{ width: 100px; margin-right: 10px; }}
          button {{ margin-right: 10px; }}
        </style>
        <script>
          function clearForm() {{
            document.getElementById('height').value = '';
            document.getElementById('weight').value = '';
          }}
        </script>
      </head>
      <body>
        <h1>あなたのBMIを測定してみましょう</h1>
        <p>このアプリでは、身長と体重を入力するだけであなたのBMIと肥満度が判定できます。</p>

        <form method="post">
          <label>身長(cm): 
            <input type="number" id="height" name="height" min="0" step="any" required>
          </label><br><br>

          <label>体重(kg): 
            <input type="number" id="weight" name="weight" min="0" step="any" required>
          </label><br><br>

          <button type="submit">計算</button>
          <button type="button" onclick="clearForm()">入力をリセット</button>
        </form>

        <div style="margin-top:20px;">{result}</div>
      </body>
    </html>"""

    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    return [html.encode("utf-8")]


# --- メイン起動部 ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    print(f"Server running on http://localhost:{port}")
    with make_server(host, port, app) as httpd:
        httpd.serve_forever()