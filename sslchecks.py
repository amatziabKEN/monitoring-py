import ssllabsscanner
import random
import MySQLdb as mdb
import redis
import time
import json
from credentials import dbCreds

services = ["https://east-vip.xg4ken.com", "https://socialorigin.kenshoo.com", "https://impsbal.xg4ken.com"]


def getServerList():
    servers = []
    creds = dbCreds()
    con = mdb.connect(creds['database'], creds['user'], creds['password'], creds['dbname'])
    with con:
        cur = con.cursor()
        cur.execute("SELECT h.name FROM hosts h WHERE h.name LIKE 'ks%%'")

        rows = cur.fetchall()
        for row in rows:
            servers.append(row[0])
    servers.extend(services)
    return servers


def getCheck():
    checks = []
    items = random.sample(getServerList(), 10)
    items = list(map(lambda x: "https://" + x + ".kenshoo.com", items))
    items.extend(services)

    for check in items:
        data = ssllabsscanner.newScan(check)
        try:
            data['endpoints'][0]['grade']
        except KeyError:
            checks.append({'check': check, 'result': 'no grade'})
            redisSetSsl(check, 'no grade')
        else:
            checks.append({'check': check, 'result': data['endpoints'][0]['grade']})
            redisSetSsl(check, data['endpoints'][0]['grade'])

    return print(checks)


def redisSetSsl(hostname, grade):
    r = redis.StrictRedis(host='10.53.220.47', port=6379, db=0)
    redisName = 'ssl.certificate|hostname=' + hostname + '|grade=' + grade
    redisData = json.dumps({'hostname': hostname, 'grade': grade, 'date': int(time.time())})
    return r.set(redisName, redisData)


getCheck()
