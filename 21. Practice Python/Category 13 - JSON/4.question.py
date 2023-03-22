# Access the nested key ‘salary’ from the following JSON


import json

sample_json = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

print(json.loads(sample_json)["company"]["employee"]["payable"]["salary"])
