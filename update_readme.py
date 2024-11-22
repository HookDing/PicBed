import os

# 指定 img 目录和 README 文件路径
dir_path = 'img/'
readme_path = 'README.md'

# 获取 img 目录下的所有文件
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# 开始更新 README.md 文件
with open(readme_path, 'w', encoding='utf-8') as readme_file:    
    # 添加 ASCII 艺术和标题
    readme_file.write("\n")
    readme_file.write("```\n")
    readme_file.write("HHHHHHHHH     HHHHHHHHH                                  kkkkkkkk                    d::::::d  iiii                                       \n")
    readme_file.write("H:::::::H     H:::::::H                                  k::::::k                    d::::::d i::::i                                      \n")
    readme_file.write("H:::::::H     H:::::::H                                  k::::::k                    d::::::d  iiii                                       \n")
    readme_file.write("HH::::::H     H::::::HH                                  k::::::k                    d:::::d                                              \n")
    readme_file.write("  H:::::H     H:::::H     ooooooooooo      ooooooooooo    k:::::k    kkkkkkk ddddddddd:::::d iiiiiiinnnn  nnnnnnnn       ggggggggg   ggggg\n")
    readme_file.write("  H:::::H     H:::::H   oo:::::::::::oo  oo:::::::::::oo  k:::::k   k:::::kdd::::::::::::::d i:::::in:::nn::::::::nn    g:::::::::ggg::::g\n")
    readme_file.write("  H::::::HHHHH::::::H  o:::::::::::::::oo:::::::::::::::o k:::::k  k:::::kd::::::::::::::::d  i::::in::::::::::::::nn  g:::::::::::::::::g\n")
    readme_file.write("  H:::::::::::::::::H  o:::::ooooo:::::oo:::::ooooo:::::o k:::::k k:::::kd:::::::ddddd:::::d  i::::inn:::::::::::::::ng::::::ggggg::::::gg\n")
    readme_file.write("  H:::::::::::::::::H  o::::o     o::::oo::::o     o::::o k::::::k:::::k d::::::d    d:::::d  i::::i  n:::::nnnn:::::ng:::::g     g:::::g \n")
    readme_file.write("  H::::::HHHHH::::::H  o::::o     o::::oo::::o     o::::o k:::::::::::k  d:::::d     d:::::d  i::::i  n::::n    n::::ng:::::g     g:::::g \n")
    readme_file.write("  H:::::H     H:::::H  o::::o     o::::oo::::o     o::::o k:::::::::::k  d:::::d     d:::::d  i::::i  n::::n    n::::ng:::::g     g:::::g \n")
    readme_file.write("  H:::::H     H:::::H  o::::o     o::::oo::::o     o::::o k::::::k:::::k d:::::d     d:::::d  i::::i  n::::n    n::::ng::::::g    g:::::g \n")
    readme_file.write("HH::::::H     H::::::HHo:::::ooooo:::::oo:::::ooooo:::::ok::::::k k:::::kd::::::ddddd::::::ddi::::::i n::::n    n::::ng:::::::ggggg:::::g \n")
    readme_file.write("H:::::::H     H:::::::Ho:::::::::::::::oo:::::::::::::::ok::::::k  k:::::kd:::::::::::::::::di::::::i n::::n    n::::n g::::::::::::::::g \n")
    readme_file.write("H:::::::H     H:::::::H oo:::::::::::oo  oo:::::::::::oo k::::::k   k:::::kd:::::::::ddd::::di::::::i n::::n    n::::n  gg::::::::::::::g \n")
    readme_file.write("HHHHHHHHH     HHHHHHHHH   ooooooooooo      ooooooooooo   kkkkkkkk    kkkkkkkddddddddd   dddddiiiiiiii nnnnnn    nnnnnn    gggggggg::::::g \n")
    readme_file.write("```\n\n")
    # readme_file.write("# A Repository for PicGO\n\n")
    readme_file.write("## img contents\n\n")
    for filename in files:
        file_path = os.path.join(dir_path, filename)
        # 写入每个文件的链接到 README.md
        readme_file.write(f"- [{filename}]({file_path})\n")
