from sqlitedict import SqliteDict
import datetime
import argparse
import json
import glob

dst_fldr = "/data/savvas/incels/data/"
dst = "channels_dict.sqlite"
tmp_sqlite = glob.glob(dst_fldr + "tmp/channels_dict*")
dict_db = SqliteDict(dst_fldr + dst, tablename="channels", journal_mode="OFF", flag="w")
for tmp in tmp_sqlite:
    print(tmp)
    tmp_dict = SqliteDict(tmp, tablename="channels", journal_mode="OFF",  flag="r")
    # print("start")
    for key, item in tmp_dict.items():
        # print(key)
        val = dict_db.get(key, [])
        val += item
        # print("1")
        dict_db[key] = val
        # print("2")
    # print("end")
    dict_db.commit()
    tmp_dict.close()
