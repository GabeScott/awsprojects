import os


os.system('crontab -l > tempfile')
os.system('echo "0 * * * * ls" >> tempfile')
os.system('crontab tempfile')
os.system('rm tempfile')

