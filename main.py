# we can import from packages as namespaces
import using_modules.table_f as furniture
import using_modules.table_h as web

# every module haas its own global namespace
g = 'this is in the global namespace for this module'

def main():
    global g # we should try to avoid using globals
    g = 'altered' # now 'g' refers to the global value
    f = furniture.table(400, 800)
    w = web.table(3,4)
    print(f, w)

if __name__ == '__main__':
    main()
    print(g)