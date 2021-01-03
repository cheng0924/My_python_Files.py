import sys
from you_get import common as you_get

d = r'F:\\Edge'
url = 'https://www.bilibili.com/video/BV1oW411q7Un?from=search&seid=12660778709814580198'
sys.argv = ['you_get', '-o', d, url]
you_get.main()
