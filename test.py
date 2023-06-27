def show_pk(lines):
    a = []
    b = []
    #ip คือที่เก็บค่า ip address ใน log
    ip=[] 
    #date 
    date = []
    for i in lines:
        splited = i.split()
        if len(splited) > 0:
            a.append(splited)

    # for i in lines:
    #     if len(i.split()) != 23:
    #         b.append(i)
    #     else:
    #         b.append("NO")

    for i in a:
        
        ip.append(i[0])
        date.append(i[3]+i[4])
        
    
    return date