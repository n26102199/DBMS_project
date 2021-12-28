from django.shortcuts import render, redirect
import pymysql.cursors
from django.contrib import messages

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

def get_all_DB():
    connection = connect_to_DB()

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from REFEREE"
            cursor.execute(sql_)
            # 獲取查詢結果
            referee_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from VENUE"
            cursor.execute(sql_)
            # 獲取查詢結果
            venue_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from TEAM"
            cursor.execute(sql_)
            # 獲取查詢結果
            team_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from STUDENT"
            cursor.execute(sql_)
            # 獲取查詢結果
            student_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from FUNDER"
            cursor.execute(sql_)
            # 獲取查詢結果
            funder_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from COMPETITION"
            cursor.execute(sql_)
            # 獲取查詢結果
            competition_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from MANAGE"
            cursor.execute(sql_)
            # 獲取查詢結果
            manage_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from BELONG"
            cursor.execute(sql_)
            # 獲取查詢結果
            belong_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行查詢
            sql_ = "select * from FUND"
            cursor.execute(sql_)
            # 獲取查詢結果
            fund_results = cursor.fetchall()
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})

    return referee_results, venue_results, team_results, student_results, funder_results, competition_results, manage_results, belong_results, fund_results


def home(request):
    referee_results, venue_results, team_results, student_results, funder_results, competition_results, manage_results, belong_results, fund_results = get_all_DB()
    if request.method == "POST":
        sql = request.POST['sql_query']
        if sql == "select * from VENUE":
            return redirect('select_from_where_demo')
        elif sql == "delete from referee where rname='裁判J'":
            return redirect('delete_demo')
        elif sql == "insert into referee value('J123456789', '裁判J', 'J')":
            return redirect('insert_demo')
        elif sql == "update referee set RLEVEL='S' where RLEVEL='J'":
            return redirect('update_demo')
        elif sql == "select count(SSSN) as count_amount from STUDENT":
            return redirect('count_demo')
        elif sql == "select sum(amount) as fund_amount from FUND":
            return redirect('sum_demo')
        elif sql == "select max(amount) as max_amount from FUND":
            return redirect('max_demo')
        elif sql == "select min(amount) as min_amount from FUND":
            return redirect('min_demo')
        elif sql == "select avg(vfee) as avg_vfee from VENUE":
            return redirect('avg_demo')
        elif sql == "select TNAME from TEAM where TID in (select TID from FUND where amount>500)":
            return redirect('in_demo')
        elif sql == "select TNAME from TEAM where TID not in (select TID from FUND where amount>500)":
            return redirect('not_in_demo')
        elif sql == "select SNAME from STUDENT where exists (select * from BELONG where STUDENT.SSSN=BELONG.SSSN && STARTDATE > '2021-10-05')":
            return redirect('exists_demo')
        elif sql == "select SNAME from STUDENT where not exists (select * from BELONG where STUDENT.SSSN=BELONG.SSSN && STARTDATE > '2021-10-05')":
            return redirect('not_exists_demo')
        elif sql == "select TNAME, SCORE from TEAM, COMPETITION where (TEAM.TID=COMPETITION.TID) having SCORE > 3":
            return redirect('having_demo')
        else:
            connection = connect_to_DB()

            sql="..."
            error_flag = 0
    
            try:
                with connection.cursor() as cursor:
                # 執行sql語句，進行查詢
                    cursor.execute(sql)
                    # 獲取查詢結果
                    results = cursor.fetchall()
                    # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
                    connection.commit()
            except Exception as e:
                error_flag = 1
                return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
            finally:
                connection.close();
            return render(request, 'not_supported_sql.html', {'not_supported_results': not_supported_results,
                                                            'sql': sql})
    else:
        return render(request, 'home.html', {'referee_results': referee_results,
                                                'venue_results': venue_results,
                                                'team_results': team_results,
                                                'student_results': student_results,
                                                'funder_results': funder_results, 
                                                'competition_results': competition_results,
                                                'manage_results': manage_results,
                                                'belong_results': belong_results,
                                                'fund_results': fund_results})

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
    sql = "delete from referee where rname='裁判J'"
    error_flag = 0

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
    finally:
        connection.close()

    return redirect('home')

def insert_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "insert into referee value('J123456789', '裁判J', 'J')"
    error_flag = 0

    # execute insert action
    try:
        with connection.cursor() as cursor:
        # 執行sql語句，進行插入
            cursor.execute(sql)
            # 沒有設定預設自動提交，需要主動提交，以儲存所執行的語句
            connection.commit()
    except Exception as e:
        error_flag = 1
        return render(request, 'error.html', {'error_flag': error_flag, 'e': e})
    finally:
        connection.close();

    return redirect('home')

def update_demo(request):
    connection = connect_to_DB()

    #selected sql
    sql = "update referee set RLEVEL='S' where RLEVEL='J'"
    error_flag = 0

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
    finally:
        connection.close();

    return redirect('home')

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