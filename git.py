import os , random

for i in range(100):
    d = str(i) + 'days ago'
    rand = random.randrange(2,3)
    with open('test.txt','a') as file:
        file.write(d + '\n')
        os.system('git add test.txt')
        os.system('git commit --date=" 2025-' +str(rand)+ '-'+d+'" -m 1')
        os.system('git push -u origin main -f')