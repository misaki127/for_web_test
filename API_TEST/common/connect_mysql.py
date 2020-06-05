import pymysql

#connection = pymysql.connect(host='192.168.2.214', user='jgw', password='Jgw*31500-2018.6',db='hydra_digital_village', charset='utf8mb4', port=3306,cursorclass=pymysql.cursors.DictCursor)

def run_one_sql(sql_info,sql):

    connection = pymysql.connect(host=sql_info['host'], user=sql_info['user'], password=sql_info['password'],
                                 db=sql_info['database'], charset='utf8mb4', port=['port'],
                                 cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    cursor.execute(sql)
    all_date = cursor.fetchall()
    cursor.close()
    return  all_date

def connect_sql(sql_info):
    connection = pymysql.connect(host=sql_info['host'], user=sql_info['user'], password=sql_info['password'],
                                 db=sql_info['database'], charset='utf8mb4', port=['port'],
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

