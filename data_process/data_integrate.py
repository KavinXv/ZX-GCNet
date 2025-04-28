import os
import shutil

def copy_images_between_folders(source_dir, target_dir):
    # 获取源文件夹中的子文件夹名称
    source_subfolders = os.listdir(source_dir)

    # 遍历源文件夹的子文件夹
    for source_subfolder in source_subfolders:
        source_subfolder_path = os.path.join(source_dir, source_subfolder)

        # 检查源子文件夹是否为文件夹
        if os.path.isdir(source_subfolder_path):
            # 对应的目标文件夹路径
            target_subfolder_path = os.path.join(target_dir, source_subfolder)
            
            # 如果目标文件夹中没有这个子文件夹，创建一个
            if not os.path.exists(target_subfolder_path):
                print(f"Creating target subfolder: {target_subfolder_path}")
                os.makedirs(target_subfolder_path)
            
            # 遍历源子文件夹中的文件
            for file_name in os.listdir(source_subfolder_path):
                source_file_path = os.path.join(source_subfolder_path, file_name)
                
                # 检查文件是否是图片类型
                if os.path.isfile(source_file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    target_file_path = os.path.join(target_subfolder_path, file_name)
                    print(f"Copying {file_name} to {target_subfolder_path}")
                    
                    # 复制文件到目标文件夹
                    shutil.copy(source_file_path, target_file_path)

# 示例用法
source_directory = r'D:\vscode_code\Deep_learning\DATASET\data2_2\test'  # 源文件夹路径
target_directory = r'D:\vscode_code\Deep_learning\DATASET\data2_2_final\test'  # 目标文件夹路径

copy_images_between_folders(source_directory, target_directory)

source_directory = r'D:\vscode_code\Deep_learning\DATASET\data2_2_1\test'  # 源文件夹路径
copy_images_between_folders(source_directory, target_directory)

source_directory = r'D:\vscode_code\Deep_learning\DATASET\data2_2_2\test'  # 源文件夹路径
copy_images_between_folders(source_directory, target_directory)

source_directory = r'D:\vscode_code\Deep_learning\DATASET\data2_2_3\test'  # 源文件夹路径
copy_images_between_folders(source_directory, target_directory)

source_directory = r'D:\vscode_code\Deep_learning\DATASET\data2_2_4\test'  # 源文件夹路径
copy_images_between_folders(source_directory, target_directory)

source_directory = r'D:\vscode_code\Deep_learning\DATASET\data2_2_5\test'  # 源文件夹路径
copy_images_between_folders(source_directory, target_directory)

source_directory = r'D:\vscode_code\Deep_learning\DATASET\data2_2_6\test'  # 源文件夹路径
copy_images_between_folders(source_directory, target_directory)