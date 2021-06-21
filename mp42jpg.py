# mp4ファイルをpgに変換します
import os
import cv2

movie_path = './'
movie_name = 'dynamite'
movie = movie_path + movie_name + '.mp4'
cap = cv2.VideoCapture(movie)

dirname = movie_path + movie_name + '_imgs'

# 幅
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('width: {:.0f} px'.format(width))

# 高さ
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('height: {:.0f} px'.format(height))

# 総フレーム数
numFrame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('総フレーム数: {:.0f}'.format(numFrame))

fps = cap.get(cv2.CAP_PROP_FPS)
print('fps : {:f}'.format(fps))

# フォルダがない場合生成
if not os.path.exists(dirname):
    os.mkdir(dirname)

numFrameLength = len(str(int(numFrame)))
count = 0
while True:
    ret, frame = cap.read()
    if ret == True:
        count += 1

        cv2.imwrite(os.path.join(
            dirname,
            '{:s}_{:s}.jpg'.format(
                movie_name,
                str(count).zfill(numFrameLength))
        ), frame)
    else:
        break
