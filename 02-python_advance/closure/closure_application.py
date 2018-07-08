def line_conf(a, b):
    def line_in(x):
        print(a*x + b)

    return line_in

line1 = line_conf(1, 1)
line1(0)
