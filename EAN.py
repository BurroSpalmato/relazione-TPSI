modalita=int(input("inserire se si vuole avere un codice EAN13(inserire 1)o EAN 8(inserire 2)"))
if modalita==1:
    while 1:
        EAN=input("inserire l'ean: ")
        h=len(EAN)
        if(len(EAN)!=13):
            print(f"la lunghezza dell'ean era sbagliata la lunghezza era di {h} caratteri")
        else:
            break
        ean=str(EAN)
        i=0
        sd=0
        sp=0
        st=0
        c=0
        for i in range(12):
            if i%2==0:
                sp+=int(EAN[i])
            else:
                sd+=int(EAN[i])
                st=(sd*3)+sp
                if st%10==0:
                    c=0
                else:
                    st=st%10
                    c=10-st
                    if c==int(EAN[12]):
                        print("corretto")
                    else: print("sbagliato")
        else:
                        while 1:
                            EAN=input("inserire l'ean: ")
                            h=len(EAN)
                            if(len(EAN)!=8):
                                print(f"la lunghezza dell'ean era sbagliata la lunghezza era di {h} caratteri")
                            else:
                                break
                            EAN=str(EAN)
                            i=0
                            sd=0
                            sp=0
