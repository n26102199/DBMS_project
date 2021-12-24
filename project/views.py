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
            sql = 'SELECT * FROM VENUE'
            cursor.execute(sql)
            # 獲取查詢結果
            result = cursor.fetchall()
            print(result)
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    finally:
        connection.close();

    return render(request, 'home.html', {'result': result})

def select_from_where_demo(request):
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

    temp = request.GET['selected form']
    error_flag = 0
    
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql = temp
            cursor.execute(sql)
            # 獲取查詢結果
            results = cursor.fetchall()
            print(results)
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except:
        error_flag = 1
        return render(request, 'select_from_where_demo.html', {'temp': temp,'error_flag': error_flag})
    finally:
        connection.close();

    return render(request, 'select_from_where_demo.html', {'results': results, 'sql': sql, 'temp': temp, 'error_flag': error_flag})
