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
            print(result)
            print(result[1][1])
            print(result[1][1].day)
            print(result[1][2])
            # print(result[1][2].day)
    finally:
        connection.close()

if __name__ == '__main__':
    accessDatabase()
