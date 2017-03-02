import pymysql.cursors

def accessDatabase(year,month,day,start, end):
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
            

            a = [True] * 7
            for i in range(0,numrows):
                if (result[i][1].year==year and result[i][1].month==month and result[i][1].day==day) :
                    #remove seconds because humans don't book tennis courts to the second
                    rs=str(result[i][2])[:-3]
                    re=str(result[i][3])[:-3]
                    if len(rs)==4: rs="0"+rs
                    if len(re)==4: re="0"+re
                    if ((rs<start and re>end) or (rs<end and re>end) or (rs<start and re>start)):
                        a[result[i][0]]=False
            for k in range(1,7):
                if (a[k]==True) :
                    if (s!=""):
                        s=s+", "
                    s=s+str(k)

    finally:
        connection.close()
    if (s==""): return "No court is open"
    s="Open courts today are: "+s
    return s

if __name__ == '__main__':
    accessDatabase()
