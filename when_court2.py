import pymysql.cursors

def accessDatabase(year,month,day,court):
    # Connect to the database
    connection = pymysql.connect(host='uvatennis.martyhumphrey.info',
                             port=3306,
                             user='UVATennisUser',
                             passwd='WR6V2vxjBbqNqbts',
                             db='tennis')
    s=""
    try:
        with connection.cursor() as cursor:
        # Read in the following columns and then use python to process
            sql = "SELECT `court`,`date`,`starttime`,`endtime` FROM `reservations`"
            cursor.execute(sql)
            result = cursor.fetchall()
            numrows = len(result)    
            list=[]
            for i in range(0,numrows):

                if ((int(result[i][0])-int(court))==0): 
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
                            print(j)
                            print(list[i]," ", list[j])
                            print(list[i]>list[j])
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

    finally:
        connection.close()
    
    if (s==""): return "Court " + court + " is not available today. (Operating hours of the tennis courts are 07:00-22:00 every day)"
    s="Court "+ court + " is open the following times:" +s + "(Operating hours of the tennis courts are 07:00-22:00 every day)"
    return s

if __name__ == '__main__':
    accessDatabase()
