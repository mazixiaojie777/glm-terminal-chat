import requests
from api_client import send_chat_request
from config import load_config

api_key, url, model = load_config()
system_message = {
    "role": "system",
    "content": "你是 Python 学习助手。用适合初学者的中文回答，控制在三句话以内。",
}
history = []
while True:
    question = input("你（输入 exit 退出）：").strip()
    if question == "exit":
        break
    if not question:
        continue

    user_message = {"role": "user", "content": question}

    messages = [system_message] + history + [user_message]

    try:
        response = send_chat_request(api_key, url, model, messages)
    except requests.exceptions.Timeout:
        print("请求超时，请稍后再试。")
        continue
    except requests.exceptions.ConnectionError:
        print("连接失败，请检查网络后再试。")
        continue
    if response.status_code == 200:
        try:
            result = response.json()
        except requests.exceptions.JSONDecodeError:
            print("无法读取模型回答：响应体不是有效的 JSON。")
            continue

        try:
            answer = result["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError):
            print("无法读取模型回答：响应数据的结构不符合预期。")
            continue

        history.append(user_message)
        history.append({"role": "assistant", "content": answer})
        print("AI：", answer)
    else:
        print("请求失败，HTTP 状态码：", response.status_code)
        if response.status_code == 401:
            print("身份验证失败，请检查 .env 中的 API Key。")
        elif response.status_code == 400:
            print("请求参数有误。如果错误详情包含 1211，请检查模型名。")
        elif response.status_code == 429:
            print("调用受到限制，请根据下方错误详情判断原因。")
        print("错误详情：", response.text)
