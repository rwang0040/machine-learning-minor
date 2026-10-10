# 环境与启动

本包使用Python 3.13.16和根目录uv.lock中的固定依赖。不要自行更换版本；已有教师配置的课程环境可以直接使用。

## Debian WSL或Cloud Studio

在课程根目录执行：

```bash
# Cloud Studio：保持平台默认下载源
bash runtime/cloudstudio/setup-remote.sh
# 本机需要沿用个人uv镜像时，改用下面这一条
# bash runtime/cloudstudio/setup-local.sh
bash runtime/cloudstudio/start-lab.sh
```

首次安装需要网络和下载时间。启动脚本显示Jupyter访问地址；本机默认只监听127.0.0.1。Cloud Studio按平台预览方式访问；如平台要求绑定全部接口，可设置`ML_JUPYTER_IP=0.0.0.0`后启动。不要公开访问令牌。

## Windows原生终端

已有uv时，在课程根目录执行：

```powershell
uv sync --locked
.\.venv\Scripts\python.exe -m ipykernel install --prefix .venv --name ml-course --display-name "机器学习 · Python 3.13"
.\.venv\Scripts\python.exe -m jupyterlab
```

选择“机器学习 · Python 3.13”内核。安装受限或网络慢时，按教师安排改用WSL或Cloud Studio，不要求为一次作业重装环境。

## 课件HTTP浏览

不需要安装Quarto或LaTeX。在课程根目录使用已安装的Python启动静态服务：

```bash
# WSL / Cloud Studio
.venv/bin/python -m http.server 8000 --bind 127.0.0.1
```

Windows使用`.\.venv\Scripts\python.exe -m http.server 8000 --bind 127.0.0.1`。本机浏览器打开`http://127.0.0.1:8000/`，从首页进入课件。Cloud Studio可通过平台端口预览；按平台要求调整绑定地址。不要仅上传HTML，需保留对应资源目录。交互运行要下载Pyodide，首次可能较慢；讲义、纸笔题和静态核对不依赖交互运行。
