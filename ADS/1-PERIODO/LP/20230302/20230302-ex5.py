sal = float(input("Digite o salário: "))
cargo = int(input("Digite o código do cargo: "))
sal_aumento = 0

if cargo == 310:
    sal_aumento = sal + (sal * 0.05)
    print(sal, sal_aumento, sal_aumento - sal)
elif cargo == 456:
    sal_aumento = sal + (sal * 0.075)
    print(sal, sal_aumento, sal_aumento - sal)
elif cargo == 885:
    sal_aumento = sal + (sal * 0.1)
    print(sal, sal_aumento, sal_aumento - sal)
else:
    sal_aumento = sal + (sal * 0.15)
    print(sal, sal_aumento, sal_aumento - sal)