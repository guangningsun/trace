# tracetest
# 简易定位跟踪系统demo 


* This project is used for sending message easily

* Chemira Co.,Ltd


* Connect

  >  月池 sun-guangning@126.com
  >
  >  薇薇
  >
  >  墨斗

### 项目简介
* python语言处理简单业务逻辑
* django框架
* sqlite3数据库，可随时切换mysql等主流数据库

### api调用方法如下


  |    URL   |       方法      |  所需方法  |      返回结构     |     描述     |
  |:--------:|:------------------: |:-----------: |:----------------:|:------------:|
  |   114.116.64.103:8000/user_login |  POST   ||   0   |用户登录接口|
  |   114.116.64.103:8000/upload_trace  | POST    |uid,lng,lat,timestamp|   {"error":0,"errmsg":"upload trace success"} |上传用户位置接口|
  |   114.116.64.103:8000/get_user_list  | GET    ||   0   |管理员获取用户信息接口|
  |   114.116.64.103:8000/get_trace_list  | GET     ||   |管理员获取某个用户全部位置信息接口|
  [ 
   {
        "uid": "1",
        "lat": "100.10001",
        "timestamp": "60000000",
        "lng": "103.0001",
        "id": 1
    },
    {
        "uid": "2",
        "lat": "100.10001",
        "timestamp": "60000001",
        "lng": "103.0001",
        "id": 2
    }
   ] 
   |:--------:|:------------------: |:-----------: |:----------------:|:------------:| 
  |   114.116.64.103:8000/get_trace_by_uid  | GET    ||   0   |管理员获取某个用户某个位置信息接口|
