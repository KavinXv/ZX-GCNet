import os
import shutil

# 定义支持的图片格式
IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff']

# 定义提取图片的函数
def extract_images_to_parent_folder(parent_folder):
    # 遍历所有的子文件夹
    for root, dirs, files in os.walk(parent_folder):
        # 如果当前目录不是父文件夹本身
        if root != parent_folder:
            for file in files:
                # 检查文件的扩展名是否是图片格式
                if any(file.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
                    source_path = os.path.join(root, file)
                    destination_path = os.path.join(parent_folder, file)
                    
                    # 如果目标文件已存在，可以选择重命名或覆盖
                    if os.path.exists(destination_path):
                        print(f"文件 {file} 已存在，正在重命名...")
                        name, ext = os.path.splitext(file)
                        new_name = f"{name}_copy{ext}"
                        destination_path = os.path.join(parent_folder, new_name)
                    
                    # 移动文件到父文件夹
                    shutil.move(source_path, destination_path)
                    print(f"已移动文件: {file}")

# 调用函数并传入父文件夹路径
parent_folder = r'D:\vscode_code\Deep_learning\DATASET\data_rock\data2_1\test'
extract_images_to_parent_folder(parent_folder)

parent_folder = r'D:\vscode_code\Deep_learning\DATASET\data_rock\data2_1\val'
extract_images_to_parent_folder(parent_folder)

parent_folder = r'D:\vscode_code\Deep_learning\DATASET\data_rock\data2_1\train'
extract_images_to_parent_folder(parent_folder)
