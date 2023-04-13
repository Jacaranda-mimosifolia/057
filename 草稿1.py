#Myclass家族，但是这个家族只有一个人f
class MyClass:
  """一个简单的类实例"""
  i = 12345
  def f(self):
    return 'hello world'
# 实例化类
x = MyClass()
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i) #家族x + 物品名i
print("MyClass 类的方法 f 输出为：", x.f()) #家族x + 人名f