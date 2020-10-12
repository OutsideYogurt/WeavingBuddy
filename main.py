import lib.wifmanip as wm
import lib.filemanip as fm
import json

mywif = wm.wifmanip("data/notsosimple_exemple.wif")

job = {}
job['wif'] = "data/notsosimple_exemple.wif"
job['currentstep'] = 1
job['steps'] = mywif.returnliftplan()

with open('data.job', 'w') as json_file:
    json.dump(job, json_file, indent=4)