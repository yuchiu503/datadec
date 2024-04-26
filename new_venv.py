import subprocess
from pathlib import Path
import sys
import os

project_name = "datadec"
project_path = f"{Path(__file__).parent}/{project_name}"
venv_name = f".venv_{project_name}"
venv_path = f"{project_path}/{venv_name}"
project_structure = {
    venv_name: {},
    # "venv_activate.sh": ""
}


error_col = "\033[91m"
succeed_col = "\033[92m"
info_col = "\033[93m"
reset_col = "\033[0m"

commands = {
    "View_catalog": {"command": "ls", "description": "查看当前文件夹"},
    "update": {
        "command": "sudo apt update",
        "description": "更新本地软件包索引",
    },
    "upgrade": {
        "command": "sudo apt upgrade -y",
        "description": "升级的软件包",
    },
    "apt_install": {
        "command": "sudo apt install postgresql postgresql-contrib python3.11-venv -y",
        "description": "安装包及依赖",
    },
    "create_venv": {
        "command": f"python3 -m venv {venv_path}",
        "description": "创建python虚拟环境",
    },
    "deactivate": {
        "command": "deactivate",
        "description": "退出当前虚拟环境",
    },
}


class Config:
    def __init__(self):
        # 更新及安装依赖、新建数据库账户、搭建虚拟环境
        list(map(self.shell, ["update", "upgrade", "apt_install", "create_venv"]))
        # 构建虚拟环境
        self.create_file_structure(project_structure, project_path)
        print(f"{info_col}激活路径：\n source {venv_path}/bin/activate{reset_col}")

    def shell(self, command_key):
        command_obj = commands[command_key]
        try:
            print(f"{info_col}执行---{command_obj['description']}{reset_col}")
            result = subprocess.run(command_obj["command"].split(), check=True)
            print(f"{succeed_col}{command_obj['description']}---成功执行{reset_col}")
        except subprocess.CalledProcessError as e:
            print(f"{error_col}执行失败: {command_obj['description']}{reset_col}")
            return False
        return True

    def create_file_structure(self, structure, base_path):
        base_path = Path(base_path)
        for folder_name, content in structure.items():
            folder_path = base_path / folder_name

            # 如果 content 是字典，则递归创建子目录
            if isinstance(content, dict):
                if not folder_path.exists():
                    folder_path.mkdir(parents=True, exist_ok=True)
                self.create_file_structure(content, folder_path)
            # 如果 content 是字符串，则在 folder_path 下创建文件
            elif isinstance(content, str):
                # 文件路径是文件夹路径加上文件名
                file_path = folder_path / content
                if not file_path.exists():
                    # 创建空文件
                    file_path.open("w").close()
            else:
                raise ValueError(f"Unsupported content type: {type(content)}")


if __name__ == "__main__":

    Config()
