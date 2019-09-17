
from scheduler import Scheduler
import sys
import io

#启动文件直接执行这个文件启动
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()

if __name__ == '__main__':
    main()