import os
import shutil

# 定义提取和合并子文件夹的函数
def extract_and_merge_subfolders(parent_folder):
    # 获取父文件夹中的所有子文件夹
    for root, dirs, files in os.walk(parent_folder, topdown=False):
        # 如果当前目录不是父文件夹本身
        if root != parent_folder:
            for dir_name in dirs:
                source_path = os.path.join(root, dir_name)
                destination_path = os.path.join(parent_folder, dir_name)
                
                # 如果目标子文件夹已存在，则合并内容
                if os.path.exists(destination_path):
                    print(f"文件夹 {dir_name} 已存在，正在合并...")
                    for item in os.listdir(source_path):
                        item_source = os.path.join(source_path, item)
                        item_destination = os.path.join(destination_path, item)
                        
                        # 如果文件或文件夹已经存在目标文件夹中，可以选择重命名或覆盖
                        if os.path.exists(item_destination):
                            if os.path.isdir(item_source):
                                # 合并文件夹
                                print(f"合并文件夹 {item_source} 到 {item_destination}...")
                                extract_and_merge_subfolders(item_source)  # 递归合并子文件夹
                            else:
                                # 重命名或覆盖文件
                                print(f"文件 {item} 已存在，正在重命名...")
                                name, ext = os.path.splitext(item)
                                new_name = f"{name}_copy{ext}"
                                shutil.move(item_source, os.path.join(destination_path, new_name))
                        else:
                            shutil.move(item_source, item_destination)
                else:
                    # 如果目标子文件夹不存在，直接移动
                    shutil.move(source_path, destination_path)
                    print(f"已移动文件夹: {dir_name}")

# 调用函数并传入父文件夹路径
parent_folder = r'D:\vscode_code\Deep_learning\DATASET\data_rock'
extract_and_merge_subfolders(parent_folder)
