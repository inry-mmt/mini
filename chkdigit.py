def chk():
  for i in range(100000):
    flg = eval('i is {}'.format(i))
    if not flg:
      return i

def main():
  print(chk())

if __name__ == '__main__':
  main()
