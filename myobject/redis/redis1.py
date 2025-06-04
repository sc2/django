# redis模块
import redis
from Pool import Pool

# redis普通连接
# conn = redis.Redis()
# conn.set('name1', 'axl')
# conn.close()

# 调用Pool文件中的Pool方法
# pool = Pool(max=10)
# conn = redis.Redis(connection_pool=pool)

# 从连接池中取连接，连接redis
pool = redis.ConnectionPool(max_connections=10)
conn = redis.Redis(connection_pool=pool)
# set(name, value, ex, px, nx, xx)

conn.set("age", "20")
print("redis写入age=20")
conn.close()
print("关闭连接池连接")
pool.close()
print("关闭连接池")