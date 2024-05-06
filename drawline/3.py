import cv2
import numpy as np

# 讀取圖片
# image = cv2.imread('a.png')
image = cv2.imread('d.jpg')
# 將圖片轉換為灰度圖像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny邊緣檢測
edges = cv2.Canny(blur, 50, 150)

# 定義感興趣區域（ROI）
height, width = edges.shape
mask = np.zeros_like(edges)
polygon = np.array([[(100, height), (width // 2, height // 2), (width - 100, height)]], dtype=np.int32)
cv2.fillPoly(mask, polygon, 255)
masked_edges = cv2.bitwise_and(edges, mask)

lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=50)

# 檢查是否有找到線段
if lines is not None:
    # 在原始圖像上繪製線條
    line_image = np.copy(image)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # 將線條合併到原始圖像中
    result = cv2.addWeighted(image, 0.8, line_image, 1, 0)

    # 顯示結果
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No lines found.")
