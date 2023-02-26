# -*- coding = UTF-8 -*-
# Autohr   : 黄朝岗
# @公众号   : iTest岗
# File     : SendReportEmail.py
# Describe : 发送邮件


from bs4 import BeautifulSoup
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText  # 构建邮件正文，可以是text，也可以是HTML
from email.mime.application import MIMEApplication  # 构建邮件附件，理论上，只要是文件即可，一般是图片，Excel表格，word文件等
import time


class SendReportToEmail:
    def send_report(self,title,mail_host,mail_user,mail_pass,receiver):
        with open(r'./report/'+title+'.html', 'r', encoding='utf-8') as f:
            Soup = BeautifulSoup(f.read(), 'html.parser')
            Pass_rate= Soup.select('#btn-group > div > a.btn.btn-primary')
            print(Pass_rate)
            ss = re.findall('通过率{(.+?)}</a>', str(Pass_rate))[0]
            print(ss)
            test_result=Soup.select('#div_base > div:nth-child(2) > div.header-left > p:nth-child(3)')
            print(test_result)
            result_text=re.findall('结果概况:</strong> (.+?)</p>]', str(test_result))[0]
            print(result_text)
            if ss == '100.00%':
                print('测试通过')
            else:
                mail_host = mail_host  # 设置服务器
                mail_user = mail_user  # 用户名
                mail_pass = mail_pass  # 密码
                # 邮件发送和接收人
                sender = mail_user
                receiver = receiver
                # 邮件头信息
                # 格式化成2016-03-20 11:45:39形式
                t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                message = MIMEMultipart('related')
                message['From'] = sender
                message['To'] = ','.join(receiver)
                message['Subject'] = Header(title+t)
                # ①普通文本内容添加到邮件
                content_text = MIMEText('测试结果: \n通过率：'+ss+'  '+'\n概况：'+result_text, 'plain', 'utf-8')
                message.attach(content_text)

                # 构建附件1
                excel_file_path_1 = r'./report/'+title+'.html'
                attach_table = MIMEApplication(open(excel_file_path_1, 'rb').read())
                attach_table.add_header('Content-Disposition', 'attachment', filename=title+'.html')
                #  这样的话，附件名称就可以是中文的了，不会出现乱码
                attach_table.set_charset('utf-8')
                message.attach(attach_table)

                excel_file_path_2 = r'./report/'+title+'.json'
                attach_table = MIMEApplication(open(excel_file_path_2, 'rb').read())
                attach_table.add_header('Content-Disposition', 'attachment', filename=title+'.json')
                #  这样的话，附件名称就可以是中文的了，不会出现乱码
                attach_table.set_charset('utf-8')
                message.attach(attach_table)

                # 发送邮件，测试成功，流程都是固定的：创建客户端，登陆，发送，关闭
                try:
                    # smtpObj = smtplib.SMTP()  # 实例化
                    smtpObj = smtplib.SMTP_SSL(mail_host)
                    # smtpObj.connect(mail_host, 25)  # 25为 SMTP 端口号
                    smtpObj.login(mail_user, mail_pass)  # 邮箱登录
                    print('登录成功！')
                    smtpObj.sendmail(mail_user, receiver, message.as_string())  # 发送邮件
                    smtpObj.quit()  # 邮件退出
                    print("恭喜：邮件发送成功!")
                except smtplib.SMTPException as e:
                    print("错误：无法发送邮件",e)

if __name__ == '__main__':
    title = ''
    mail_host = ""  # 设置服务器
    mail_user = ""  # 用户名
    mail_pass = ""  # 密码
    # 邮件发送和接收人
    receiver = ['211986576@qq.com', '1205409349@qq.com', ]
    SendReportToEmail().send_report(title,mail_host,mail_user,mail_pass,receiver)


