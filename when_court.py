import pymysql.cursors

def accessDatabase(year,month,day,start, end):
    # Connect to the database
    connection = pymysql.connect(host='uvatennis.martyhumphrey.info',
                             port=3306,
                             user='UVATennisUser',
                             passwd='WR6V2vxjBbqNqbts',
                             db='tennis')
    try:
        with connection.cursor() as cursor:
        # Read a single record
            sql = "SELECT `court`,`date`,`starttime`,`endtime` FROM `reservations`"
            cursor.execute(sql)
            result = cursor.fetchall()
            numrows = len(result)    
            a[:5]=true
            for i in range(0,numrows-1):
                if (result[i][1].year=year and result[i][1].month=month and result[i][1].day=day) :
                    if ((result[i][2]<start and result[i][3]>end) or (result[i][2]<end and result[i][3]>end) or (result[i][2]<start and result[i][3]>start):
                        a[result[i][0]]=False
            for k in range(0,5):
                if (a[k]==true) :
                    print(k)

    finally:
        connection.close()

if __name__ == '__main__':
    accessDatabase()
