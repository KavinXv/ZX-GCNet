import cv2
import os

def apply_gaussian_blur(image, kernel_size=(5, 5), sigma=0):
    """
    对图像进行高斯模糊处理
    :param image: 输入图像
    :param kernel_size: 高斯核大小，必须为奇数
    :param sigma: 高斯函数的标准差，0 表示根据核大小自动计算
    :return: 处理后的模糊图像
    """
    blurred_image = cv2.GaussianBlur(image, kernel_size, sigma)
    return blurred_image

def process_images_with_blur(input_folder, output_folder, kernel_size=(9, 9), sigma=10.0):
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

                # 对图像进行高斯模糊处理
                blurred_img = apply_gaussian_blur(img, kernel_size, sigma)

                # 构建输出文件夹路径
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)

                # 如果输出文件夹不存在，创建它
                os.makedirs(output_dir, exist_ok=True)

                # 构建输出图像路径，并在文件名后加上 "1"
                file_name, file_ext = os.path.splitext(file)
                output_file_name = f"{file_name}_3{file_ext}"
                output_img_path = os.path.join(output_dir, output_file_name)

                # 保存模糊处理后的图像
                cv2.imwrite(output_img_path, blurred_img)

                print(f"图像保存到: {output_img_path}")

if __name__ == "__main__":
    # 输入大文件夹路径（原始图像所在位置）
    input_folder = r'D:\vscode_code\Deep_learning\DATASET\data2_2\test'  # 替换为你输入的大文件夹路径

    # 输出大文件夹路径（处理后的图像保存位置）
    output_folder = r'D:\vscode_code\Deep_learning\DATASET\data2_2_3\test'  # 替换为你输出的大文件夹路径

    # 高斯模糊的参数
    kernel_size = (5, 5)  # 高斯核大小，必须为奇数
    sigma = 0  # 高斯函数的标准差，0 表示根据核大小自动计算

    # 调用函数进行遍历和处理
    process_images_with_blur(input_folder, output_folder, kernel_size, sigma)
