import cv2
import numpy as np

# 讀取圖片
image = cv2.imread('image.jpg')

# 轉換為灰度圖
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 高斯模糊
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny 邊緣檢測
edges = cv2.Canny(blur, 0, 75)  # 調整低閾值和高閾值

# 二值化
_, binary = cv2.threshold(edges, 10, 255, cv2.THRESH_BINARY)

# 定義膨脹核心
kernel = np.ones((3, 3), np.uint8)

# 膨脹操作
dilated_image = cv2.dilate(binary, kernel, iterations=5)

resized_dilated_image = cv2.resize(binary, (800, 600))
cv2.imshow('binary', resized_dilated_image)

# 創建一個感興趣的區域遮罩(mask)，這樣霍夫變換只會在這個區域內檢測線條
# 這個遮罩取決於圖片的具體情況，你可能需要手動調節座標
height, width = dilated_image.shape
mask = np.zeros_like(dilated_image)
extend_length =40
polygon = np.array([[
    (970, 450),
    (1020, 450),
    (400, 1050),
    (1650, 1050)
]], np.int32)
# 填充多邊形
cv2.fillPoly(mask, polygon, 255)

# 將遮罩應用於 Canny 邊緣檢測的輸出
masked_edges = cv2.bitwise_and(dilated_image, mask)

resized_masked_edges = cv2.resize(masked_edges, (800, 600))  # 將圖像調整為 800x600 的大小
cv2.imshow('mask', resized_masked_edges)

# 霍夫變換檢測線條
lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, threshold=250, minLineLength=400, maxLineGap=300)

# 繪製線條
if lines is not None:
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 5)


'''
# 標記藍色圓點的位置 900, 520   1020, 520     400, 1050
blue_dot_position = (1650, 1050)  # 這裡是示例位置，您可以根據需要更改位置

# 設置藍色顏色 (BGR 格式)
blue_color = (255, 0, 0)

# 繪製藍色圓點
radius = 10  # 圓點半徑
cv2.circle(image, blue_dot_position, radius, blue_color, -1)  # -1 表示填充整個圓
# 顯示結果圖片
'''
resized_image = cv2.resize(image, (800, 600))  # 將圖像調整為 800x600 的大小
cv2.imshow('Lane Lines', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存結果圖片
cv2.imwrite('/mnt/data/lane_lines_image.png', image)