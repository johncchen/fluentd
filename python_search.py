from elasticsearch import Elasticsearch

import datetime

d1 = datetime.datetime.now()
d3 = d1 + datetime.timedelta(days=-5)

#print (d1.strftime("%Y-%m-%dT%H:%M:%S"))
#print (d3.strftime("%Y-%m-%dT%H:%M:%S"))

nowtime = d1.strftime("%Y-%m-%dT%H:%M:%S")
before5 = d3.strftime("%Y-%m-%dT%H:%M:%S")

es = Elasticsearch([{'host': '52.68.214.54', 'port': '9200'}])

qdoc = {
  "query": {
    "bool": {
      "must": [
        {"match": {"response_code": "404"}},
        {"range": {
          "@timestamp": {
            "gte": before5+"+08:00",
            "lte": nowtime+"+08:00"}
          }
        }
      ]
    }
  }
}


fdoc = {
  "query": {
    "bool": {
      "filter":{
        "bool":{
          "must": [
            {"match": {"response_code": "404"}},
            {"range": {
              "@timestamp": {
                "gte": "2017-11-06T00:00:00+08:00",
                "lte": "2017-11-07T23:59:59+08:00"}
              }
            }
          ]
        }
      }
    }
  }
}


getdata = es.search(index="uat-nginx-access*", body=qdoc)

#print (getdata['hits']['total'])
times = getdata['hits']['total']


print ("404 times in 5 minutes | 404 time=".times)


#print (nowtime)
#print (before5)
