import os
import shutil

# 设定大文件夹的路径
base_folder = 'E:\\Dataset_rock\\data2\\train'

# 设定目标文件夹路径
target_folders = {
    'sedimentary': os.path.join(base_folder, 'sedimentary'),
    'igneous': os.path.join(base_folder, 'igneous'),
    'metamorphic': os.path.join(base_folder, 'metamorphic')
}

# 创建目标文件夹（如果不存在）
for folder in target_folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# 遍历大文件夹下的所有子文件夹
for subfolder in os.listdir(base_folder):
    subfolder_path = os.path.join(base_folder, subfolder)
    
    # 检查是否是文件夹
    if os.path.isdir(subfolder_path):
        # 获取子文件夹中的第一个文件
        files = os.listdir(subfolder_path)
        if files:
            first_file = files[0]
            # 判断文件名，并移动子文件夹
            if 'sedimentary' in first_file:
                target_folder = target_folders['sedimentary']
            elif 'igneous' in first_file:
                target_folder = target_folders['igneous']
            elif 'metamorphic' in first_file:
                target_folder = target_folders['metamorphic']
            else:
                continue  # 如果文件名不包含任何关键字，跳过
            
            # 移动子文件夹到目标文件夹
            shutil.move(subfolder_path, os.path.join(target_folder, subfolder))
            print("move ")
