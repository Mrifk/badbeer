def frob(botl):
    print "%s bottles of beer on the wall," % botl
    print "%r bottles of beer," % botl
    print "You take one down, pass it around,"
    print "%i bottles of beer on the wall!\n" % len(range(1, botl)
    if botl > 1:
        frob(len(range(1, botl)))
    else:
        ""
frob(len(range(1, 99)))
