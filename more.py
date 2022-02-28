def main():
    # conditonals
    i=99
    # quit() # stop the program
    # exit()
    while i !=0:
        # print(i)
        i-=1 # same as i = i-1
        if i<50:
            pass # dead handy to satisfy indent requirements!!
            break # break out of the loop

    # range - here we populate a list from a range
    num_l = [ num for num in range(0, 100, 5) ]
    print(num_l, type(num_l))

    # generator - a range in a tuple with added features...
    num_g = ( num for num in range(0, 100, 5) ) # does not result in a tuple
    print(num_g, type(num_g))
    # we can iterate over members yielded by a generator
    print(num_g.__next__()) # 0 is yielded as the next member from the generator
    print(num_g.__next__()) # 5
    print(num_g.__next__()) # 10
    print(num_g.__next__()) # 15
    for item in num_g:
        print(item) # all the other members from the generator

    # print(num_g.__next__()) # no result - our generator has been exhausted

    # comprehension - comprehensively deal with each member
    odd_t  = (num for num in ( range(0,101) ) if num%2 == 1)
    even_l = [num for num in ( range(0,101) ) if num%2 == 0] # list comprehension

    # dictionary comprehension
    p = 'are we there yet'
    chars = {letter:p.count(letter) for letter in p} 
    print(chars)


if __name__ == '__main__':
    main()