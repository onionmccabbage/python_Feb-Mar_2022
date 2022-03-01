# file input and file output
def simpleOutput(): # writing out to a file
    '''
    Python uses file access objects
    If a file access object points to a non-existant file
    then it will create the file 'a' means append (or create)
    'w' means (over)write 'x' means exclusive - fails if file exists
    '''
    fout = open('output.txt', 'at') # default output format is 't' text
    # we can write to a file using print
    print('here is some interesting content', file=fout) # python 3 only
    fout.close() # we MUST tidy up!!

def simpleInput(): # read back from a file
    try: # careful - file may be up one level
        fin = open('output.txt', 'rt') # 'r' will read 't' for text (default)
        received = fin.read() # reads the entire file
        print(received)
    except Exception as e:
        print(e)
    finally:
        fin.close()

def fileWriter(t = 'default'):
    try: # try the following block, but if an exception occurs....
        fout   = open('mylog.txt', 'at') # if this was 'xt' the FileExistsError exception would occur
        size   = len(t)
        offset = 0
        chunk  = 24
        while True:
            if offset > size:
                fout.write('\n') # append a new line character when we have finished writing out all the content
                break
            else:
                fout.write(t[offset:offset+chunk])
                offset += chunk
    except FileExistsError as fe:
        print('The file already exists {}'.format(fe))
    except Exception as e: # handle any exception in this code block
        print(e)
    finally: # always run this block, whether or not we had an exception
        fout.close() # always good to tidy up
        print('all done')

def fileReader():
    with open('mylog.txt', 'rt') as fin: # 'with' will close the file access object when done
        retrieved = fin.readlines() # read into a list of lines
        print(retrieved)

def main():
    # simpleOutput()
    # simpleInput()
    fileReader()
    # fileWriter('this is a long piece of text which will be written in chunks to the log')

if __name__ == '__main__':
    main()