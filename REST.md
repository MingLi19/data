## Rest

1. [Get] /api/v1/todo -> Get all todos
2. [Post] /api/v1/todo -> Create a todo
3. [Put] /api/v1/todo/:id -> Update a todo
4. [Delete] /api/v1/todo/:id -> Delete a todo

MVC pattern: Model View Controller 
Modal: Schema
View: Frontend
Controller: Backend Controller (Rest API)

## 状态码

- 200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。cachable
- 201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
- 400 BAD REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
- 401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
- 403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
- 404 Not Found - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
- 500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。