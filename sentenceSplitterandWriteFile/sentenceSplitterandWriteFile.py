#for döngüsü sözlük içinde çevirmeyi denedim fakat çok hata verdiği için kullanmadan yazdım, kullanmadan fazla uzun olmuş olsa da problemsiz çalışıyor hocam :)
#Dosyayı .py dosyasının bulunduğu dizine kaydeder, bilgisayardan bilgisayara path kullanıcı isminden dolayı değişeceğinden eklemedim.
f = open("harf_indisleri_ve_sayilari.txt", "w")
cumle = "Gunes olamiyorsan yildiz ol"
print("'Gunes olamiyorsan yildiz ol'", file=f)
print("-------------------------------------", file=f)
a=cumle.count("a")
if a>0:
    print(a , "adet a aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("a", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("A harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


b=cumle.count("b")
if b>0:
    print(b , "adet b aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("b", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("B harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



c=cumle.count("c")
if c>0:
    print(c , "adet c aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("c", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("C harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



d=cumle.count("d")
if d>0:
    print(d , "adet d aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("d", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("D harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



e=cumle.count("e")
if e>0:
    print(e , "adet e aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("e", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("E harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



fa=cumle.count("f")
if fa>0:
    print(fa , "adet f aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("f", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("F harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



g=cumle.count("g")
if g>0:
    print(g , "adet g aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("g", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("G harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)




i=cumle.count("i")
if i>0:
    print(i , "adet i aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("i", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("İ harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



j=cumle.count("j")
if j>0:
    print(j , "adet j aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("j", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("J harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



k=cumle.count("k")
if k>0:
    print(k , "adet k aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("k", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("K harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



l=cumle.count("l")
if l>0:
    print(l , "adet l aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("l", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("L harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



m=cumle.count("m")
if m>0:
    print(m , "adet m aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("m", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("M harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)



n=cumle.count("n")
if n>0:
    print(n , "adet n aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("n", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("N harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


o=cumle.count("o")
if o>0:
    print(o , "adet o aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("o", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("O harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


p=cumle.count("p")
if p>0:
    print(p , "adet p aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("p", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("P harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


r=cumle.count("r")
if r>0:
    print(r , "adet r aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("r", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("R harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


s=cumle.count("s")
if s>0:
    print(s , "adet s aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("s", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("S harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


t=cumle.count("t")
if t>0:
    print(t , "adet t aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("t", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("T harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


u=cumle.count("u")
if u>0:
    print(u , "adet u aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("u", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("U harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


v=cumle.count("v")
if v>0:
    print(v , "adet v aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("v", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("V harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


y=cumle.count("y")
if y>0:
    print(y , "adet y aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("y", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("Y harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)


z=cumle.count("z")
if z>0:
    print(z , "adet z aşağıdaki indislerde var", file=f)
    try:
        for i in range(len(cumle)):
            if i == cumle.index("z", i):
               print(i+1 ,"indisinde", file=f)
    except ValueError:
      print("Bu harf için değerlerin sonu", file=f)
    print("-------------------------------------", file=f)
else:
    print("Z harfi cümlede bulunmamaktadır.", file=f)
    print("-------------------------------------", file=f)

