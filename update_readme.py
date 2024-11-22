import os

# 指定 img 目录和 README 文件路径
dir_path = 'img/'
readme_path = 'README.md'

# 获取 img 目录下的所有文件
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# 开始更新 README.md 文件
with open(readme_path, 'w', encoding='utf-8') as readme_file:    
    readme_file.write("    __  __            __       ___            \n")
    readme_file.write("   / / / /___  ____  / /______/ (_)___  ____ _\n")
    readme_file.write("  / /_/ / __ \/ __ \/ //_/ __  / / __ \/ __ `/\n")
    readme_file.write(" / __  / /_/ / /_/ / ,< / /_/ / / / / / /_/ / \n")
    readme_file.write("/_/ /_/\____/\____/_/|_|\__,_/_/_/ /_/\__, /  \n")
    readme_file.write("                                     /____/   \n")
    # readme_file.write("# A Repository for PicGO\n\n")
    readme_file.write("## img contents\n\n")
    for filename in files:
        file_path = os.path.join(dir_path, filename)
        # 写入每个文件的链接到 README.md
        readme_file.write(f"- [{filename}]({file_path})\n")
