## 采用PO模式设计的Web UI自动化测试框架
## 通过Selenium＋Pytest实现

### 结构如下：
- Base:封装Selenium
- Common:存放公共函数或方法，如解析yaml文件
- Config:存放配置信息
- Data:存放测试用例的数据，本框架采用yaml数据驱动
- Test
  - PageObject:存放页面对象，包括元素定位类、元素操作类和业务场景类
  - TestCase:存放测试用例
