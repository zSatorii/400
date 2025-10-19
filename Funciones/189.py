for Johan in range(2, 21):
    Sebastian = True
    for Castro in range(2, Johan):
        if Johan % Castro == 0:
            Sebastian = False
            break
    if Sebastian:
        print(Johan)