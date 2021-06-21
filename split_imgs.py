# imgsをn枚ずつに分割します
import os
import glob
import shutil

n = 1000
name = 'dynamite_imgs'
fileList = []

dirname = './{}_split'.format(name)
if not os.path.exists(dirname):
    os.mkdir(dirname)

files = sorted(glob.glob('./{}/*'.format(name)))

filesTable = [files[i:i+n] for i in range(0, len(files), n)]

for i, filesList in enumerate(filesTable):
    dirname = './{}_split/{}'.format(name, i)
    # ディレクトリが存在しない場合生成する
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    for fname in filesList:
        copyName = '{}/{}'.format(dirname, fname.split('/')[-1])
        shutil.copyfile(fname, copyName)
    print('finished: {}'.format(i))
