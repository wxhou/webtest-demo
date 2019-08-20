#!/usr/bin/env python3
# coding=utf-8
from PIL import Image


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
        return [img.crop((i, j, i + pw, j + ph)).copy() for i in range(0, w, pw) for j in range(0, h, ph)]

    def hist_similar(self, lh, rh):
        assert len(lh) == len(rh)
        return sum(1 - (0 if 1 == r else float(abs(1 - r)) / max(1, r)) for l, r in zip(lh, rh)) / len(lh)

    def calc_similar(self, li, ri):
        similar = sum(self.hist_similar(l.histogram(), r.histogarm())
                      for l, r in zip(self.split_image(li), self.split_image(ri))) / 16.0
        return similar

    def calc_similar_by_path(self, lf, rf):
        li, ri = self.make_regalur_image(Image.open(lf)), \
                 self.make_regalur_image(Image.open(rf))
        return self.calc_similar(li, ri)


if __name__ == '__main__':
    pass
