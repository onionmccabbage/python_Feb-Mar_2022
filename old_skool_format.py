# The old way of formatting strings in Python
# %s string
# %d decimal integer
# %x hex integer
# %o octal integer
# %f decimal float
# %e exponential float
# %g decimal or exponential float
##  %% a literal %

# An integer:
print ('%s' % 42) # '42'
print ('%d' % 42) # '42'
print ('%x' % 42) # '2a'
print ('%o' % 42) # '52'
# A float:
print ('%s' % 7.03) # '7.03'
print ('%f' % 7.03) # '7.030000'
print ('%e' % 7.03) # '7.030000e+00'
print ('%g' % 7.03) # '7.03'
# An integer with a literal percentage sign:
print ('%d%%' % 100) # '100%'
# Some string and integer interpolation:
lang = 'Python'
cat = 'Chester'
weight = 2.8
print("My favorite language is %s" % lang)
print("Our cat %s weighs %s kg" % (cat, weight))
