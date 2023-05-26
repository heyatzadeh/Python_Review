import FTPOverSSL
import config
import datetime

file = open('./logs.zip', "rb")
with FTPOverSSL.ImplicitFTP_TLS() as ftps:
    for i in range(1000):
        time = datetime.datetime.now()
        ftps.connect(host=config.url, port=config.port)
        ftps.login(user=config.user, passwd=config.password)
        ftps.prot_p()
        ftps.storbinary(f'STOR /in_file/79/test/I94430003-D20230423-T{time.strftime("%H-%M-%S-%f")}Test.zip', file)
        print(f'Number: {i} successful I94430003-D20230423-T{time.strftime("%H-%M-%S-%f")}Test.zip')

file.close()
