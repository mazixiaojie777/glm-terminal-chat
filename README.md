\# Python 终端 AI 对话



用 Python 和 `requests` 调用智谱 GLM-4.7-Flash。支持在同一次运行中连续追问，输入 `exit` 退出。退出后，本次对话历史会清空。



\## 安装依赖



在项目目录打开 PowerShell，运行：



```powershell

python -m pip install -r .\\requirements.txt

```



\## 配置



```powershell

Copy-Item .\\.env.example .\\.env

```



在新建的 `.env` 里填写 `BIGMODEL\_API\_KEY`。如果已经有 `.env`，直接编辑现有文件，跳过复制命令。分享项目时，只分享 `.env.example`，真实密钥保留在本地。



\## 运行



```powershell

python .\\main.py

```



如果 `python` 命令没有输出，改用本机实际安装的 `python.exe` 路径。



\## 常见错误



\- `401`：检查 `.env` 里的 API Key。

\- `400` 且详情包含 `1211`：检查 `.env` 里的 `BIGMODEL\_MODEL`。

\- `429`：看响应体里的错误码。`1305` 表示模型繁忙，`1302` 表示请求频率达到限制。

