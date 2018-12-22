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

### api调用方法

```
1.创建用户
请求路径：114.116.64.103:8000/create_user
请求方法：POST
所需参数：username,password,role,phone_number
返回参数：{"error":0,"errmsg":"create user success"}

2.通过traceid获取trace内容
请求路径：114.116.64.103:8000/get_trace_by_traceid
请求方法：POST
所需参数：trace_id
返回参数：
返回失败结果：{"error":0,"errmsg":"create user success"} 

3.通过用户id,起止时间来获取该时间段该用户的轨迹信息
请求路径：114.116.64.103:8000/get_trace_by_uid
请求方法：POST
所需参数：user_id,start_time,end_time
返回参数：


4.通过用户id来获取用户信息
请求路径：114.116.64.103:8000/get_user_by_uid
请求方法：POST
所需参数：user_id
返回参数：{"error":1,"errmsg":"the user that you request doesn`t exist"}


5.获取用户列表
请求路径：114.116.64.103:8000/get_user_list
请求方法：GET
所需参数：null
返回参数：{
    "user_list": [
        {
            "username": "lvaid",
            "phone_number": "15333333",
            "uid": "1543848336",
            "password": "lvaid",
            "user_role": "1",
            "id": 1
        },
        {
            "username": "lvaid1",
            "phone_number": "153333333",
            "uid": "1545077231",
            "password": "lvaid1",
            "user_role": "1",
            "id": 2
        }
    ]
}	


6.上传用户轨迹信息
请求路径：114.116.64.103:8000/upload_trace
请求方法：POST
所需参数：uid,lng,lat
返回参数：{
            "error": 0,
            "errmsg": "upload trace success"
           }

```

### api调用方法如下


  |    URL   |       方法      |  所需参数  |      返回结构     |     描述     |
  |:--------:|:------------------: |:-----------: |:----------------:|:----------------:|
  |   114.116.64.103:8000/user_login |  POST   ||   0   |用户登录接口|
  |   114.116.64.103:8000/upload_trace  | POST    |uid,<br>lng,<br>lat|   {"error":0,<br>"errmsg":"upload trace success"} |上传用户位置接口|
  |   114.116.64.103:8000/get_user_list  | GET    ||   [{"username": "lv",<br>"phone_number": "15",<br>"uid": "15",<br>"password": "lv",<br>"user_role": "1","id": 1}]   |管理员获取用户信息接口|
  |   114.116.64.103:8000/get_trace_list  | GET     || [ {"uid": "1",<br> "lat": "100.10001", <br>"timestamp": "60000000",<br>"lng": "103.0001",<br>"id": 1}]  |管理员获取某个用户全部位置信息接口|
  |   114.116.64.103:8000/get_trace_by_uid  | GET    ||   0   |管理员获取某个用户某个位置信息接口|
  |   114.116.64.103:8000/create_user  |POST     |username,<br>password,<br>user_role,<br>phone_number|   {"error":0,<br>"errmsg":"create user success"}   |管理员创建用户|
