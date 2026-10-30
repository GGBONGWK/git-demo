"""我的第一个 Git 练习脚本。"""

import datetime


def greet(name: str = "世界") -> str:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{now}] 你好，{name}！这份代码已经被 Git 管理了。"


if __name__ == "__main__":
    print(greet())
