import cv2
import numpy as np

# 讀取圖片
image = cv2.imread('a.jpg')
if image is None:
    print("圖片加載失敗，請檢查路徑是否正確")
else:
    height, width = image.shape[:2]

    # 創建一個同樣大小的透明圖層
    overlay = np.zeros((height, width, 4), dtype=np.uint8)

    # 定義盲點多邊形的頂點
    points = np.array([[0, height], [int(width * 0.15)+400, int(height * 0.5)], [width, int(height * 0.5)+100]])

    # 在透明圖層上畫填充的多邊形
    cv2.fillPoly(overlay, [points], (0, 0, 255, 127))  # 紅色, 127 是 alpha 透明度

    # 將透明圖層疊加到原始圖像上
    alpha = overlay[:, :, 3] / 255.0
    for c in range(0, 3):
        image[:, :, c] = (1 - alpha) * image[:, :, c] + alpha * overlay[:, :, c]

    # 顯示圖像
    cv2.imshow('Blind Spot Areas with Transparency', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
