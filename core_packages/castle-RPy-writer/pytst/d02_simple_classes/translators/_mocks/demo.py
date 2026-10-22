def demo(a,b):
    return a+b

def main(argv):
    c = demo(1,2)
    print (c)
    return 0

def target(*args):
  return main, None

if __name__ == '__main__':
  import sys
  main(sys.argv)


