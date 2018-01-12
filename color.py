# -*- coding:utf-8 -*-


class Colored(object):  
    # 显示格式: \033[显示方式;前景色;背景色m  
    # 只写一个字段表示前景色,背景色默认  
    RED = '\033[31m'       # 红色  
    GREEN = '\033[32m'     # 绿色  
    YELLOW = '\033[33m'    # 黄色  
    BLUE = '\033[34m'      # 蓝色  
    FUCHSIA = '\033[35m'   # 紫红色  
    CYAN = '\033[36m'      # 青蓝色  
    WHITE = '\033[37m'     # 白色  
  
    #: no color  
    RESET = '\033[0m'      # 终端默认颜色  
  
    def color_str(self, color, s):  
        return '{}{}{}'.format(  
            getattr(self, color),  
            s,  
            self.RESET  
        )  
  
    def red(self, s):  
        return self.color_str('RED', s)  
  
    def green(self, s):  
        return self.color_str('GREEN', s)  
  
    def yellow(self, s):  
        return self.color_str('YELLOW', s)  
  
    def blue(self, s):  
        return self.color_str('BLUE', s)  
  
    def fuchsia(self, s):  
        return self.color_str('FUCHSIA', s)  
  
    def cyan(self, s):  
        return self.color_str('CYAN', s)  
  
    def white(self, s):  
        return self.color_str('WHITE', s)  
  
# ----------使用示例如下:-------------  
color = Colored()  
print color.red('I am red!')  
print color.green('I am gree!')  
print color.yellow('I am yellow!')  
print color.blue('I am blue!')  
print color.fuchsia('I am fuchsia!')  
print color.cyan('I am cyan!')  
print color.white('I am white')  