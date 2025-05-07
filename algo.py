a=int(input("ingrese la unidad (1=B - 2=KB - 3=MB - 4=GB): "))
b=int(input("ingrese la cantidad: "))
match a:
    case 1:
        c=int(input("ingrese la unidad a convertir ( 1=KB - 2=MB - 3=GB): "))
        match c:
            case 1:
                print("son",(b/1024),"KB")
            case 2:
                print("son",(b/1024/1024),"MB")
            case 3:
                print("son",(b/1024/1024/1024),"GB")
    case 2:
        c=int(input("ingrese la unidad a convertir ( 1=B - 2=MB - 3=GB): "))
        match c:
            case 1:
                print("son",(b*1024),"B")
            case 2:
                print("son",(b/1024),"MB")
            case 3:
                print("son",(b/1024/1024),"GB")
    case 3:
        c=int(input("ingrese la unidad a convertir ( 1=B - 2=KB - 3=GB): "))
        match c:
            case 1:
                print("son",(b*1024*1024),"B")
            case 2:
                print("son",(b*1024),"KB")
            case 3:
                print("son",(b/1024),"GB")
    case 4:
        c=int(input("ingrese la unidad a convertir ( 1=B - 2=KB - 3=MB): "))
        match c:
            case 1:
                print("son",(b*1024*1024*1024),"B")
            case 2:
                print("son",(b*1024*1024),"KB")
            case 3:
                print("son",(b*1024),"MB")
    case _:
        print("invalido")
        exit