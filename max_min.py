def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = my_max_min(a, b, c)

def my_max_min(a, b, c):
    if a>b:
        max_ = a
        min_ = b
    else:
        max_ = b
        min_ = a

    if  c > max_:
        max_ = c  
    if  c < min_:
        min_ = c
 
    print("max = %d" % max_)
    print("min = %d" % min_)

if __name__ == "__main__":
    main()

