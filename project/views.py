from django.shortcuts import render, redirect
import pymysql.cursors

def home(request):
    if request.method == "POST":
        sql = request.POST['sql_query']
        if sql == "select * from VENUE":
            return redirect('select_from_where_demo')
        # elif sql == "delete from TEST_TABLE where TEST_name='test_name2'":
        else:
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})

def connect_to_DB():
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
    return connection

def select_from_where_demo(request):
    connection = connect_to_DB()

    temp = "select * from VENUE"
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
    except Exception as e:
        error_flag = 1
        return render(request, 'select_from_where_demo.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'select_from_where_demo.html', {'results': results, 'sql': sql, 'temp': temp, 'error_flag': error_flag})

def delete_demo(request):
    connection = connect_to_DB()

    # get selected sql
    sql = "delete from TEST_TABLE where TEST_name='test_name2'"
    error_flag = 0

    # get sql result (before delete)
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from TEST_TABLE"
            cursor.execute(sql_)
            # 獲取查詢結果
            before_delete_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    # finally:
    #     connection.close();

    # execute delete action
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行刪除
            cursor.execute(sql)
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    # finally:
    #     connection.close();

    # get sql result (after delete)
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from TEST_TABLE"
            cursor.execute(sql_)
            # 獲取查詢結果
            after_delete_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'delete_demo.html', {'before_delete_results': before_delete_results, 
                                                            'after_delete_results': after_delete_results,
                                                            'sql': sql, 
                                                            'error_flag': error_flag,
                                                            })

def insert_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "insert into TEST_TABLE values('django1')"
    error_flag = 0

    # get sql result (before delete)
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from TEST_TABLE"
            cursor.execute(sql_)
            # 獲取查詢結果
            before_insert_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    # finally:
    #     connection.close();

    # execute delete action
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行插入
            cursor.execute(sql)
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    # finally:
    #     connection.close();

    # get sql result (after delete)
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from TEST_TABLE"
            cursor.execute(sql_)
            # 獲取查詢結果
            after_insert_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'insert_demo.html', {'before_insert_results': before_insert_results, 
                                                'after_insert_results': after_insert_results,
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def update_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "update TEST_TABLE set TEST_name='update' where TEST_name='test_name2'"
    error_flag = 0

    # get sql result (before delete)
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from TEST_TABLE"
            cursor.execute(sql_)
            # 獲取查詢結果
            before_update_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    # execute update action
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行更新
            cursor.execute(sql)
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    # get sql result (after delete)
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from TEST_TABLE"
            cursor.execute(sql_)
            # 獲取查詢結果
            after_update_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'update_demo.html', {'before_update_results': before_update_results, 
                                                'after_update_results': after_update_results,
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def count_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select count(SSSN) as count_amount from STUDENT"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            count_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'count_demo.html', {'count_results': count_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def sum_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select sum(amount) as fund_amount from FUND"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            sum_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'sum_demo.html', {'sum_results': sum_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def max_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select max(amount) as max_amount from FUND"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            max_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'max_demo.html', {'max_results': max_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def min_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select min(amount) as min_amount from FUND"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            min_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'min_demo.html', {'min_results': min_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def avg_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select avg(vfee) as avg_vfee from VENUE"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            avg_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'avg_demo.html', {'avg_results': avg_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def in_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select TNAME from TEAM where TID in (select TID from FUND where amount>500)"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            in_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'in_demo.html', {'in_results': in_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def not_in_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select TNAME from TEAM where TID not in (select TID from FUND where amount>500)"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            not_in_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'not_in_demo.html', {'not_in_results': not_in_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def exists_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select SNAME from STUDENT where exists (select * from BELONG where STUDENT.SSSN=BELONG.SSSN && STARTDATE > '2021-10-05')"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            exists_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'exists_demo.html', {'exists_results': exists_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def not_exists_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select SNAME from STUDENT where not exists (select * from BELONG where STUDENT.SSSN=BELONG.SSSN && STARTDATE > '2021-10-05')"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            not_exists_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'not_exists_demo.html', {'not_exists_results': not_exists_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })

def having_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "select TNAME, SCORE from TEAM, COMPETITION where (TEAM.TID=COMPETITION.TID) having SCORE > 3"
    error_flag = 0

    # get sql result
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            cursor.execute(sql)
            # 獲取查詢結果
            having_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return render(request, 'having_demo.html', {'having_results': having_results, 
                                                'sql': sql, 
                                                'error_flag': error_flag,
                                                })