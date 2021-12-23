from django.shortcuts import render
import pymysql.cursors

def home(request):
    config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'n26102199',
    'db':'DBMS_project_server',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
    }
    # Connect to the database
    connection = pymysql.connect(**config)
    
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql = 'SELECT * FROM TEST_TABLE'
            cursor.execute(sql)
            # 獲取查詢結果
            result = cursor.fetchall()
            print(result)
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    finally:
        connection.close();

    return render(request, 'home.html', {'result': result})
