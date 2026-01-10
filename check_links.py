import requests
import re

# 定义需要检测的资源链接
links = {
    "DeepSeek": "https://www.deepseek.com/",
    "DuckDuckGo AI": "https://duckduckgo.com/",
    "Google AI Studio": "https://aistudio.google.com/",
    "Groq": "https://groq.com/"
}

def check_status():
    report = "### ⚡ 实时链路监控\n\n| 资源 | 状态 | 最后检测时间 |\n| :--- | :--- | :--- |\n"
    for name, url in links.items():
        try:
            res = requests.get(url, timeout=10)
            status = "🟢 正常" if res.status_code == 200 else "🟡 异常"
        except:
            status = "🔴 失效"
        report += f"| {name} | {status} | 2026-01-10 |\n"
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # 替换 README 中的监控模块（需在 README 中预留占位符）
    new_content = re.sub(r"## 📊 链路监控.*?(?=##)", f"## 📊 链路监控\n\n{report}\n", content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    check_status()
