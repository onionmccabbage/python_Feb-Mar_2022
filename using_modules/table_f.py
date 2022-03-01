def table(width, height):
    t = {'width':width, 'height':height}
    return t

if __name__ == '__main__':
    a = table(600, 1200)
    print('The table measures {} by {}'.format(a['width'], a['height']))
