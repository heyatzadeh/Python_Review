import config
from FTPOverSSL import ImplicitFTP_TLS
from datetime import datetime

with ImplicitFTP_TLS() as session:
    session.connect(host=config.url, port=config.port)
    session.login(user=config.user, passwd=config.password)
    session.prot_c()
    while True:
        file = open('./logs.zip', "rb")
        session.storbinary(f'STOR /in_file/79/test/I10001005-{datetime.now().strftime("D%Y%m%d-T%H-%M-%S-%f")}.zip',
                           file)
        print('successfully uploaded')
        file.close()
