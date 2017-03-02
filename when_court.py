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
            print(str(result[i][2])
            a = [True] * 7
            for i in range(0,numrows):
                if (result[i][1].year==year and result[i][1].month==month and result[i][1].day==day) :
                    if ((str(result[i][2])<start and str(result[i][3])>end) or (str(result[i][2])<end and str(result[i][3])>end) or (str(result[i][2])<start and str(result[i][3])>start)):
                        a[result[i][0]]=False
            for k in range(1,7):
                if (a[k]==True) :
                    if (s!=""):
                        s=s+", "
                    s=s+str(k)

    finally:
        connection.close()
    if (s==""): return "No court is open"
    s="Open courts: "+s
    return s

if __name__ == '__main__':
    accessDatabase()
