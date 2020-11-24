sayi =int(input("Sayı giriniz:"))
sayistring =str(sayi)
toplamlari =0
for i in sayistring:
    kuvvetcarp =int(i) ** len(sayistring)
    print(kuvvetcarp,"= sayınızın basamak sayısı kadar kuvveti")
    toplamlari +=kuvvetcarp
    print(toplamlari,"Sayınızın basamak değerlerinin basamak sayısı kadar kuvvetlerinin toplamı")
if (toplamlari==sayi):
    print(sayi, "bir ARMSTRONG sayısıdır.")
else:
    print(sayi, "bir ARMSTRONG sayısı değildir.")
