#coding=utf-8
from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np


def wordcloudplot(txt):
    path = r'ancient_style.ttf'
    # path = unicode(path, 'utf8').encode('gb18030')
    # path = str(path, 'utf8').encode('gb18030')
    alice_mask = np.array(PIL.Image.open('black.jpg'))
    wordcloud = WordCloud(font_path=path,
                          background_color="black",
                          margin=2, width=900, height=400, mask=alice_mask, max_words=2000, max_font_size=300,
                          random_state=42)
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('black7.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    # plt.show()


def main():
    # a = []
    f = open(r'../Day-4-comment_txt/红螺寺_comment.txt', 'r', encoding='utf-8', errors='ignore').read()
    words = jieba.lcut(f)
    # for word in words:
    #     if len(word) > 1:
    #         a.append(word)
    a = [word for word in words if len(word) > 1]
    txt = r' '.join(a)
    wordcloudplot(txt)
    #print(a)
    print(txt)


if __name__ == '__main__':
    main()

