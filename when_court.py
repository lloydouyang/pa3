import pymysql.cursors

def accessDatabase():
    # Connect to the database
    connection = pymysql.connect(host='uvatennis.martyhumphrey.info',
                             port=3306,
                             user='UVATennisUser',
                             passwd='WR6V2vxjBbqNqbts',
                             db='tennis')
    try:
        with connection.cursor() as cursor:
        # Read a single record
        # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        # cursor.execute(sql, ('webmaster@python.org',))
        # result = cursor.fetchone()
            print("1234566")
    finally:
        connection.close()
        print("66")

if __name__ == '__main__':
    accessDatabase()
