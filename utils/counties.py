result=[]
with open('counties.txt','r') as file:
    counties=file.readlines()
    for i in counties:
        code=int(i.strip('\n').split('.')[0])
        county=i.strip('\n').split('.')[-1]
        f=f"('{code:02d}','{county}')"
        result.append(f)

with open('counties_updated.txt','w') as file:
    for i in result:
        file.write(i)
        file.write('\n')