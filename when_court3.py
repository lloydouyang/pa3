import pymysql.cursors

def accessDatabase(year,month,day):
    # Connect to the database
    connection = pymysql.connect(host='uvatennis.martyhumphrey.info',
                             port=3306,
                             user='UVATennisUser',
                             passwd='WR6V2vxjBbqNqbts',
                             db='tennis')
    s=""
    try:
        with connection.cursor() as cursor:
        # Read a single record
            sql = "SELECT `court`,`date`,`starttime`,`endtime` FROM `reservations`"
            cursor.execute(sql)
            result = cursor.fetchall()
            numrows = len(result)  
            ss = [""] * 7  
            a=[0,1,2,3,4,5,6]
            for k in range(1,7):
                list=[]
                s=""
                for i in range(0,numrows):

                    if ((int(result[i][0])-k)==0): 
                        if (result[i][1].year==year and result[i][1].month==month and result[i][1].day==day) :
                            # formatting time to facilitate comparison later
                            rs=str(result[i][2])[:-3]
                            re=str(result[i][3])[:-3]
                            if len(rs)==4: rs="0"+rs
                            if len(re)==4: re="0"+re
                            #add in the reserved times to list
                            list.append(rs)
                            list.append(re)
           
                for i in range(0,len(list)):
                    if (i % 2==0):
                        for j in range(i+1,len(list)):
                            if (j % 2==0):
                                if (list[i]>list[j]):
                                    temp=list[i]
                                    temp2=list[i+1]
                                    list[i]=list[j]
                                    list[i+1]=list[j+1]
                                    list[j]=temp
                                    list[j+1]=temp2
                i=0
                st="07:00"
          
                if (len(list)==0): 
                    s="07:00 - 22:00"
                else:
                    while i<len(list):
                        if (st<list[i]):
                            s=s+ " " + st + "-" +list[i]
                        st=list[i+1]
                        i=i+2
                    if  (list[i-1]<"22:00"):
                        s=s+" " + list[i-1] + "-22:00"
                ss[k]=s

    finally:
        connection.close()
    for i in range(1,7):
        for j in range(i+1,7):
            if (ss[i]>ss[j]):
                temp=ss[i]
                temp2=a[i]
                ss[i]=ss[j]
                a[i]=a[j]
                ss[j]=temp
                a[j]=temp2
   
    return "Court " + str(a[1]) +" is one of the earliest available tomorrow with opening times: "+ss[1]

if __name__ == '__main__':
    accessDatabase()
