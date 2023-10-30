
input_raw = {"student1":
   {'name': "Rahul",
    'roll': 23455,
    'age': 22
   },
"student2":
   {'name': "Rahul",
    'roll': 23455,
    'age': 22
   },
"student3":
   {'name': "bipul",
    'roll': 12334,
    'age': 22
   },
"student4":
   {'name': "rajiv",
    'roll': 122234,
    'age': 22
   }
}

common = {}

output = {}

for key, value in input_raw.items():
    values = frozenset(value.items())

    if values not in common:
        common[values] = True
        output[key] = value

print(output)
