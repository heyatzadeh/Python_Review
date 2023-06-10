from datetime import datetime
import ftplib
import FTPOverSSL
import CSVReader
import config

time = datetime.now()

with FTPOverSSL.ImplicitFTP_TLS() as ftps:
    ftps.connect(host=config.url, port=config.port)
    ftps.login(user=config.user, passwd=config.password)
    ftps.prot_c()
    ftps.cwd(f'/in_file/00/logs/rahsam/{time.strftime("%Y/%m/%Y%m09")}')

    for terminal in CSVReader.get_terminals():
        try:
            ftps.cwd(terminal)
            if len(ftps.nlst()) == 0:
                print(terminal + ' is empty')
            elif len(ftps.nlst()) > 1:
                print(terminal + ' more than one file')
            else:
                print(terminal + ' is OK')
        except ftplib.error_perm:
            print(terminal + ' not found')
        else:
            ftps.cwd('..')
