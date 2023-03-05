import cv2
import time

videoWriter = cv2.VideoWriter('test3.avi', cv2.VideoWriter_fourcc(*'MJPG'), 25, (1920, 1080))
# retval = cv.VideoWriter.open(filename, fourcc, fps, frameSize[, isColor])
# - 保存视频为test.avi，可以选择mp4等
# - fps为25,即每秒25张图片
# - 视频尺寸大小为1920,1080
# - isColor可以为true,flase选择是否有颜色
# time.sleep(2)
for i in range(1, 8):
    # 加载图片，图片更多可以改变上面的10
    img = cv2.imread('../img/jnu/' + str(i) + '.jpg')
    img = cv2.resize(img, (1920, 1080))
    # 如果每张图片为只显示一下，就用如下代码
    # videoWriter.write(img)
    # 如下让每张图显示1秒，具体与fps相等
    a = 0
    while a < 25:
        videoWriter.write(img)
        a += 1
print('abb')
videoWriter.release()


