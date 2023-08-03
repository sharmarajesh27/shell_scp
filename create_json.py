import json
import pandas as pd

my_emp=[{"emp":1,"name":"rajesh","age":32,"skills":["Python","PowerBI"],"city":"Mohali"},
        {"emp":2,"name":"Munish","age":30,"skills":["Linux","Devops"],"city":"Delhi"}
        ]
print(type(my_emp))

with open("json1.txt","w") as fw:
    json.dump(my_emp,fw,indent=4)

print("Json file created")


print(df)


