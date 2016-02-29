import redis as rs

r = rs.StrictRedis(host='localhost', port=6379, db=0)
dir(r)
r.delete('letters')
nums = range(97, 97 + 25)
for num in nums:
    r.zadd('letters', num, chr(num))


