import cv2
import os
import numpy as np

def add_gaussian_noise(image, mean=0, sigma=25):
    """
    对图像添加高斯噪声
    :param image: 输入图像
    :param mean: 噪声的均值
    :param sigma: 噪声的标准差
    :return: 添加噪声后的图像
    """
    noise = np.random.normal(mean, sigma, image.shape).astype(np.float32)
    noisy_image = image.astype(np.float32) + noise

    # 将图像的像素值限制在0到255之间，并转换为 uint8 类型
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image


def process_images_with_gaussian_noise(input_folder, output_folder, mean=0, sigma=25):
    # 遍历输入文件夹下的所有子文件夹和文件
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg", ".bmp")):  # 检查图像文件格式
                # 构建原始图像路径
                img_path = os.path.join(root, file)

                # 读取彩色图像
                img = cv2.imread(img_path)

                if img is None:
                    print(f"无法加载图像: {img_path}")
                    continue

                # 对图像添加高斯噪声
                noisy_img = add_gaussian_noise(img, mean, sigma)

                # 构建输出文件夹路径
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)

                # 如果输出文件夹不存在，创建它
                os.makedirs(output_dir, exist_ok=True)

                # 构建输出图像路径，并在文件名后加上 "1"
                file_name, file_ext = os.path.splitext(file)
                output_file_name = f"{file_name}_2{file_ext}"
                output_img_path = os.path.join(output_dir, output_file_name)

                # 保存添加噪声后的图像
                cv2.imwrite(output_img_path, noisy_img)

                print(f"图像保存到: {output_img_path}")

if __name__ == "__main__":
    # 输入大文件夹路径（原始图像所在位置）
    input_folder = r'D:\vscode_code\Deep_learning\DATASET\data2_2\test'  # 替换为你输入的大文件夹路径

    # 输出大文件夹路径（处理后的图像保存位置）
    output_folder = r'D:\vscode_code\Deep_learning\DATASET\data2_2_2\test'  # 替换为你输出的大文件夹路径

    # 高斯噪声的参数
    mean = 0  # 高斯噪声均值
    sigma = 50  # 高斯噪声标准差

    # 调用函数进行遍历和处理
    process_images_with_gaussian_noise(input_folder, output_folder, mean, sigma)
