# django_rest_jwt_tutorial

基于[django_rest_swagger_tutorial](https://github.com/zhusheng/django_rest_swagger_tutorial)进行迭代

我们知道rest为我们提供了get、post、put、patch、delete等请求方法，我们使用swagger的样式去显示我们的接口。rest为我们提供了基本的认证，我们必须有账号才能访问所有的接口。但是，这样只要用户登录了，一样可以随意、无限制的操作我们的接口。

于是，我们引入了jwt框架，JSON WEB TOKEN，它有一个access token和refresh token，用户登录账号去获取这2个token，用于其它的接口请求，也就是说其它接口必须要有token才能拿到数据。

## token机制

jwt框架提供了2个token,access token和refresh token, 用户登录后会获得这2个token，access token用于其它的接口请求，refresh token用于更新access token，延长access token的有效期。

access token和refresh token都有失效时间设置，access token失效时间短，refresh token失效时间长，我们可以使用refresh token去更新我们的access token。当用户正在访问网站时，access token失效了，这时我们可以在前端进行操作，使用refresh token去更新access token，在后台延长网站访问时间，使用户不至于退出网站。如果refresh token也失效了， 那么用户会退出登录，需要重新登录去获取这2个token。

## authentication VS authorization

> Django auth
> The Django authentication system handles both authentication and authorization.
authentication verifies a user is who they claim to be,
authorization determines what an authenticated user is allowed to do.

简单说：authentication验证用户是否存在，authorization验证这个用户是否有操作权限。

## jwt简介

[jwt官方文档，介绍](https://jwt.io/introduction/)

jwt，全称 JSON Web Token,是一种公开的标准（RFC 7519），这种标准制定了compact以及self-contained 的方法，用于使用JSON的方式进行安全的数据传递。

jwt接口使由三个部分组成：分別为 Header，Payload，Signature。所以，一般的 JWT 格式看起來如下：xxxxx.yyyyy.zzzzz。

[jwt.io Debugger](http://jwt.io/)

使用示例图如下：
![image](https://raw.githubusercontent.com/zhusheng/blog/master/django/10.png)
它把我们的token的实际内容也显示出来了。

## jwt原理图

![image](https://raw.githubusercontent.com/zhusheng/blog/master/django/11.png)

[图片来源](https://jwt.io/introduction/)

## jwt安装

`pip install djangorestframework-jwt`

## jwt基本配置

[Github博客，jwt配置](http://getblimp.github.io/django-rest-framework-jwt/)

说明：这里我使用的是`simple-jwt`

最终效果如下所示：
![image](https://raw.githubusercontent.com/zhusheng/blog/master/django/09.png)

## 说明

这里的项目setting参考了yingcloud的一些配置进行编写。
