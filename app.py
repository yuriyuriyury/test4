import os
import gradio as gr

# Gradioアプリケーションの定義
def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

# ポートを環境変数から取得
port = int(os.environ.get('PORT', 8000))

# Gradioアプリケーションの起動
iface.launch(server_name="0.0.0.0", server_port=port)