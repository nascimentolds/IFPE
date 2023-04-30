txt = "A casa é bonita, a casa é azul"

new = txt.split(' ')
tpl = ()

for i in new:
    if (i, len(i)) not in tpl:
        tpl = tpl + ((i, len(i)),)

print(tpl)