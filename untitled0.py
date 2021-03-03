# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:00:32 2021

@author: joysi
"""

import json

                                       
json_data='{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }'
                                                                         
python_obj=json.loads(json_data)

print(python_obj['HeightCm'])


                                                                         