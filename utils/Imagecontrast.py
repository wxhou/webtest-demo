#!/usr/bin/env python3
# coding=utf-8
from fuzzywuzzy import fuzz
from PIL import Image
import base64


class ImageCompare:
    """
    本类实现了两个图片的相似度百分比
    """

    def make_regalur_image(self, img, size=(256, 256)):
        return img.resize(size).convert('RGB')

    def split_image(self, img, part_size=(64, 64)):
        w, h = img.size
        pw, ph = part_size
        assert w % pw == h % ph == 0
        return [img.crop((i, j, i + pw, j + ph)).copy()
                for i in range(0, w, pw) for j in range(0, h, ph)]

    def hist_similar(self, lh, rh):
        assert len(lh) == len(rh)
        return sum(1 - (0 if 1 == r else float(abs(1 - r)) / max(1, r))
                   for l, r in zip(lh, rh)) / len(lh)

    def calc_similar(self, li, ri):
        similar = sum(self.hist_similar(l.histogram(), r.histogram())
                      for l, r in zip(self.split_image(li), self.split_image(ri))) / 16.0
        return similar

    def calc_similar_by_path(self, lf, rf):
        li, ri = self.make_regalur_image(Image.open(lf)), \
                 self.make_regalur_image(Image.open(rf))
        return self.calc_similar(li, ri)


class BaseComparison:

    def comparison(self, path):
        with open(path, 'rb') as f:
            basedata = base64.b64encode(f.read())
        return basedata

    def calc_similar(self, path1, path2):
        li, ri = self.comparison(path1), \
                 self.comparison(path2)
        if fuzz.ratio(li, ri) > 90:
            return True
        else:
            return False


if __name__ == '__main__':
    import os
    from config.conf import root_dir

    img = BaseComparison()
    path1 = os.path.join(root_dir, 'screenshot', '123.png')
    path2 = os.path.join(root_dir, 'screenshot', '一下.png')
    imgs = img.calc_similar(path1, path2)
    print(imgs)
