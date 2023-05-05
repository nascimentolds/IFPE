txt = "A casa é bonita, a casa é azul"

new = txt.split(' ')
tpl = ()

for i in new:
    if (i, new.count(i)) not in tpl:
        tpl = tpl + ((i, new.count(i)),)

print(tpl)