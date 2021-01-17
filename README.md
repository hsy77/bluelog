# Bluelog 安装

**使用镜像直接看第4步**

**云数据库以删除，需要新建**（防止花费过高）



## 1，安装过程

clone:
```
$ git clone https://github.com/hsy77/bluelog.git
$ cd bluelog
```
## 2，使用已有数据库

## （使用新建数据库先跳转至3，再做2）

在云主机中安装依赖：

```
(这两步可不做，即不用创建虚拟环境)
$ python3 -m venv env  
$ source env/bin/activate  
(需要在云主机上或者虚拟环境中运行，两个环境都可以，为了保证psycopg2的安装不报错)
$ sudo yum install postgresql-libs -y
$ sudo yum install postgresql-devel -y
$ sudo yum install gcc -y
(安装需要的包)
$ pip3 install -r requirements.txt
```
生成数据并且运行:
```
$ flask forge #将数据导入数据表中
$ flask run -h 0.0.0.0 -p 80  #在0.0.0.0 80端口运行，为了使得使用外网ip可以访问
* Running on http://0.0.0.0:80/
```

接下来就可以在网页上输入云主机外网ip访问

Test account:

* username: `admin`
* password: `helloflask`



## 3， 使用新建云数据库

- 将`bluelog\bluelog\settings.py` 中的以下四个参数改为自己数据库的设置

![数据库设置.jpg](http://ww1.sinaimg.cn/large/005ZSk16gy1gmqk9kv2iwj30cw03rwei.jpg)



# 4,从镜像中导入：

### - 先做步骤3，新建数据库

### - 然后

生成数据并且运行:

```
$ flask forge #将数据导入数据表中
$ flask run -h 0.0.0.0 -p 80  #在0.0.0.0 80端口运行，为了使得使用外网ip可以访问
* Running on http://0.0.0.0:80/
```

接下来就可以在网页上输入云主机外网ip访问

Test account:

* username: `admin`

* password: `helloflask`

  

## 安装成果

![安装成果.jpg](http://ww1.sinaimg.cn/large/005ZSk16gy1gmqk9ujm8xj30y30q0wi2.jpg)