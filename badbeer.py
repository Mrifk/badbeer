def puts(QUUX):
    from os import system as printf
    printf("echo %s" % QUUX)
def beer(SPAM):
    puts("%i bottles of beer on the wall," % SPAM)
    puts("%i bottles of beer," % SPAM)
    puts("You take one down, pass it around,")
    if ((SPAM - 1) == (1) == True):
        puts("%i bottle of beer on the wall!" % (SPAM - 1))
    else:
        puts("%i bottles of beer on the wall!" % (SPAM - 1))
    print""
    if ((SPAM - 1) > (1)):
        beer((SPAM - 1))
    else:
        foo = "bar"
beer(99)
puts("1 bottle of beer on the wall, && echo 1 bottle of beer, && echo And if that one bottle should happen to fall, && echo What a waste of alcohol!")