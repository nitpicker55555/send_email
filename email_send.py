import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
def send_email(message,image_path=None,address='1303385763@qq.com'):
    # SMTP设置
    smtp_server = "smtp.163.com"
    smtp_port = 465
    email = "weatherforu@163.com"
    password = ""
    recipient = address

    # 创建一个MIMEMultipart对象来代表电子邮件本身
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = recipient
    msg["Subject"] = message

    # 添加电子邮件文本
    text = MIMEText("Here is your image.")
    msg.attach(text)

    # 打开图像并添加到电子邮件
    if image_path!=None:
        with open(image_path, "rb") as img_file:
            img_data = img_file.read()
            image = MIMEImage(img_data, name="my_image.jpg")
            msg.attach(image)

        # 使用SMTP服务器发送电子邮件
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(email, password)
        server.sendmail(email, recipient, msg.as_string())
    return True