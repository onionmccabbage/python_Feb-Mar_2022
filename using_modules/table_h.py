def table(rows, columns):
    t = {'rows':rows, 'columns':columns}
    return t

if __name__ == '__main__':
    a = table(300, 12)
    print('The table has {} rows and {} columns'.format(a['rows'], a['columns']))
