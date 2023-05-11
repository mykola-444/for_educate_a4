import turtle as t


def go_snowy(len):
    if len < 5:
        t.forward(len)
    else:
        go_snowy(len / 3)
        t.left(60)
        go_snowy(len / 3)
        t.right(120)
        go_snowy(len / 3)
        t.left(60)
        go_snowy(len / 3)

t.speed(200)
go_snowy(200)
t.right(120)
go_snowy(200)
t.right(120)
go_snowy(200)


