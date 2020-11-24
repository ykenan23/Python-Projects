#A veB şıklarını tek programda işlevsel hale getirebilir bir biçimde yazdım.
#Renk değerlerini programa stabil hale uyarlama adına hsv üzerinde çok fazla değer deneyip smoothing işlemiyle tamamladım.
import cv2
import numpy as np
font1= cv2.FONT_HERSHEY_PLAIN
f = open("sekil_renk.txt", "w")
def nothing(x):
    pass


img = cv2.imread("resim.jpg")

while 1:

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lhb = 94
    lsb = 65
    lvb = 98
    uhb = 115
    usb = 255
    uvb = 255

    lower_blue = np.array([lhb, lsb, lvb])
    upper_blue = np.array([uhb, usb, uvb])

    lhg = 54
    lsg = 132
    lvg = 70
    uhg = 95
    usg = 251
    uvg = 200

    lower_green = np.array([lhg, lsg, lvg])
    upper_green = np.array([uhg, usg, uvg])

    lhr = 112
    lsr = 223
    lvr = 0
    uhr = 179
    usr = 255
    uvr = 360

    lower_red = np.array([lhr, lsr, lvr])
    upper_red = np.array([uhr, usr, uvr])

    maskblu = cv2.inRange(hsv, lower_blue, upper_blue)
    ret, thresh = cv2.threshold(maskblu, 240, 255, cv2.THRESH_BINARY)
    maskblu[thresh == 0] = 254
    maskblu[thresh == 255] = 0
    maskblu[thresh == 254] = 255

    maskre = cv2.inRange(hsv, lower_red, upper_red)
    ret, thresh = cv2.threshold(maskre, 240, 255, cv2.THRESH_BINARY)
    maskre[thresh == 0] = 254
    maskre[thresh == 255] = 0
    maskre[thresh == 254] = 255

    maskgree = cv2.inRange(hsv, lower_green, upper_green)
    ret, thresh = cv2.threshold(maskgree, 240, 255, cv2.THRESH_BINARY)
    maskgree[thresh == 0] = 254
    maskgree[thresh == 255] = 0
    maskgree[thresh == 254] = 255

    kernel = np.ones((5, 5), np.uint8)
    maskblue = cv2.erode(maskblu, kernel, iterations = 1)
    maskgreen = cv2.erode(maskgree, kernel, iterations = 1)
    maskr = cv2.erode(maskre, kernel, iterations = 1)
    maskred = cv2.bilateralFilter(maskr,3, 141, 141)





    _, thresholdblue = cv2.threshold(maskblue, 240, 255, cv2.THRESH_BINARY)

    contoursb, _ = cv2.findContours(maskblue, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    _, thresholdred = cv2.threshold(maskred, 240, 255, cv2.THRESH_BINARY)
    contoursr, _ = cv2.findContours(maskred, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    _, thresholdgreen = cv2.threshold(maskgreen, 240, 255, cv2.THRESH_BINARY)

    contoursg, _ = cv2.findContours(maskgreen, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    try:
        for cntb in contoursb:
            epsilonb = 0.001 * cv2.arcLength(cntb, True)
            approxb = cv2.approxPolyDP(cntb, epsilonb, True)
            x = approxb.ravel()[0]
            y = approxb.ravel()[1]
        centres = []
        for i in range(len(contoursb)):
            momentsb = cv2.moments(contoursb[i])
            centres.append((int(momentsb['m10'] / momentsb['m00']), int(momentsb['m01'] / momentsb['m00'])))
            cv2.circle(img, centres[-1], 3, 0, -1)
        _, threshold = cv2.threshold(maskblue, 240, 255, cv2.THRESH_BINARY)
    except ZeroDivisionError:
        continue

    contoursb, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mavi_ucgen_sayaci = 0
    mavi_dortgen_sayaci = 0
    mavi_daire_sayaci = 0
    kirmizi_ucgen_sayaci = 0
    kirmizi_dortgen_sayaci = 0
    kirmizi_daire_sayaci = 0
    yesil_ucgen_sayaci = 0
    yesil_dortgen_sayaci = 0
    yesil_daire_sayaci = 0

    for cntb in contoursb:
        approxb = cv2.approxPolyDP(cntb, 0.01 * cv2.arcLength(cntb, True), True)
        x = approxb.ravel()[0]
        y = approxb.ravel()[1]

        if len(approxb) == 3:
            mavi_ucgen_sayaci = mavi_ucgen_sayaci + 1
            cv2.putText(img, "Ucgen", (x, y), font1, 1, (0))
        elif len(approxb) == 4:
            mavi_dortgen_sayaci = mavi_dortgen_sayaci + 1
            cv2.putText(img, "Dortgen", (x, y), font1, 1, (0))
        elif len(approxb) == 5:
            mavi_ucgen_sayaci = mavi_ucgen_sayaci + 1
            cv2.putText(img, "Ucgen", (x, y), font1, 1, (0))
        elif len(approxb) >= 6 and len(approxb) <= 10:
            mavi_ucgen_sayaci = mavi_ucgen_sayaci + 1
            cv2.putText(img, "Ucgen", (x, y), font1, 1, (0))
        else:
            mavi_daire_sayaci = mavi_daire_sayaci + 1
            cv2.putText(img, "Daire", (x, y), font1, 1, (0))
    # ---------------------------------------------------------------
    for cntg in contoursg:
        epsilong = 0.001 * cv2.arcLength(cntg, True)
        approxg = cv2.approxPolyDP(cntg, epsilong, True)
        x = approxg.ravel()[0]
        y = approxg.ravel()[1]
    centres = []
    for i in range(len(contoursg)):
        momentsg = cv2.moments(contoursg[i])

        centres.append((int(momentsg['m10'] / momentsg['m00']), int(momentsg['m01'] / momentsg['m00'])))
        cv2.circle(img, centres[-1], 3, 0, -1)
    _, threshold = cv2.threshold(maskgreen, 240, 255, cv2.THRESH_BINARY)

    contoursg, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for cntg in contoursg:
        approxg = cv2.approxPolyDP(cntg, 0.01 * cv2.arcLength(cntg, True), True)
        x = approxg.ravel()[0]
        y = approxg.ravel()[1]

        if len(approxg) == 3:
            yesil_ucgen_sayaci = yesil_ucgen_sayaci + 1
            cv2.putText(img, "Ucgen", (x, y), font1, 1, (0))
        elif len(approxg) == 4:
            yesil_dortgen_sayaci = yesil_dortgen_sayaci + 1
            cv2.putText(img, "Dortgen", (x, y), font1, 1, (0))
        elif len(approxg) == 5:
            yesil_dortgen_sayaci = yesil_dortgen_sayaci + 1
            cv2.putText(img, "Dortgen", (x, y), font1, 1, (0))
        elif len(approxg) >= 6 and len(approxg) <= 9:
            yesil_ucgen_sayaci = yesil_ucgen_sayaci + 1
            cv2.putText(img, "Ucgen", (x, y), font1, 1, (0))
        else:
            yesil_daire_sayaci = yesil_daire_sayaci + 1
            cv2.putText(img, "Daire", (x, y), font1, 1, (0))
    # ---------------------------------------------------------------
    for cntr in contoursr:
        epsilonr = 0.001 * cv2.arcLength(cntr, True)
        approx = cv2.approxPolyDP(cntr, epsilonr, True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
    centres = []
    for i in range(len(contoursr)):
        momentsr = cv2.moments(contoursr[i])

        centres.append((int(momentsr['m10'] / momentsr['m00']), int(momentsr['m01'] / momentsr['m00'])))
        cv2.circle(img, centres[-1], 3, 0, -1)
    _, threshold = cv2.threshold(maskred, 240, 255, cv2.THRESH_BINARY)

    contoursr, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for cntr in contoursr:
        approxr = cv2.approxPolyDP(cntr, 0.01 * cv2.arcLength(cntr, True), True)
        x = approxr.ravel()[0]
        y = approxr.ravel()[1]

        if len(approxr) == 3:
            kirmizi_ucgen_sayaci = kirmizi_ucgen_sayaci + 1
            cv2.putText(img, "Ucgen", (x, y), font1, 1, (0))
        elif len(approxr) == 4:
            kirmizi_dortgen_sayaci = kirmizi_dortgen_sayaci + 1
            cv2.putText(img, "Dortgen", (x, y), font1, 1, (0))
        elif len(approxr) == 5:
            kirmizi_dortgen_sayaci = kirmizi_dortgen_sayaci + 1
            cv2.putText(img, "Dortgen", (x, y), font1, 1, (0))
        elif len(approxr) >= 6 and len(approxr) <= 10:
            kirmizi_ucgen_sayaci = kirmizi_ucgen_sayaci + 1
            cv2.putText(img, "Ucgen", (x, y), font1, 1, (0))
        else:
            kirmizi_daire_sayaci = kirmizi_daire_sayaci + 1
            cv2.putText(img, "Daire", (x, y), font1, 1, (0))

    print("Mavi Ucgen Sayisi:", mavi_ucgen_sayaci, file=f)
    print("Mavi Dortgen Sayisi:", mavi_dortgen_sayaci-1, file=f)
    print("Mavi Daire Sayisi:", mavi_daire_sayaci, file=f)
    print("Kirmizi Ucgen Sayisi:", kirmizi_ucgen_sayaci, file=f)
    print("Kirmizi Dortgen Sayisi:", kirmizi_dortgen_sayaci-1, file=f)
    print("Kirmizi Daire Sayisi:", kirmizi_daire_sayaci, file=f)
    print("Yesil Ucgen Sayisi:", yesil_ucgen_sayaci, file=f)
    print("Yesil Dortgen Sayisi:", yesil_dortgen_sayaci-1, file=f)
    print("Yesil Daire Sayisi:", yesil_daire_sayaci, file=f)

    #Buraya yazdigi gibi dosyaya da yazmaktadir.
    print("Mavi Ucgen Sayisi:", mavi_ucgen_sayaci)
    print("Mavi Dortgen Sayisi:", mavi_dortgen_sayaci-1)
    print("Mavi Daire Sayisi:", mavi_daire_sayaci)
    print("Kirmizi Ucgen Sayisi:", kirmizi_ucgen_sayaci)
    print("Kirmizi Dortgen Sayisi:", kirmizi_dortgen_sayaci-1)
    print("Kirmizi Daire Sayisi:", kirmizi_daire_sayaci)
    print("Yesil Ucgen Sayisi:", yesil_ucgen_sayaci)
    print("Yesil Dortgen Sayisi:", yesil_dortgen_sayaci-1)
    print("Yesil Daire Sayisi:", yesil_daire_sayaci)
    f.close()
    #Dortgenlere -1 eklememin sebebi ortada bir nokta daha masıyor olması.(Ana Resim Merkezi)
    cv2.imshow("img",img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break