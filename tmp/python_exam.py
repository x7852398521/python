# -*- coding: utf-8 -*-

input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}


L=[]
while input_value.keys():
    L.append(list(input_value.keys())[0])  
    input_value = input_value[list(input_value.keys())[0]]
    if type(input_value) != dict:
        L.append(input_value)
        break
k,v = L[1:],L[0]
for i in k:
    D = dict()
    D[i] = v
    v = D

print(v)

"""輸出結果
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}
"""




