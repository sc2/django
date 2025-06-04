import redis


# 创建连接池，池的大小是10
def Pool(max):

    if(max > 0):
        pool = redis.ConnectionPool(max_connections=max)
        print("连接池创建成功，池最大为10")
        return
    else:
        pool.close()


