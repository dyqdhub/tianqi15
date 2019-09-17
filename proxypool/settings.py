# Redis信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'


# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITTAL_SCORE = 10


# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

#测试网站
TEST_URL = 'http://tianqi.moji.com/'

#代理状态ID
VALID_STATUS_CODES = [200, 302]

# 最大批测试量
BATCH_TEST_SIZE = 50

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True