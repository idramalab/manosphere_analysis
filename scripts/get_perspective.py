from sqlitedict import SqliteDict
import datetime
import argparse
import json


parser = argparse.ArgumentParser(description="""This script generates an sqlite files that help throughout the analysis
                                                of the comments!""")

parser.add_argument("--src", dest="src", action="append",
                    help=".ndjson file with comments and perspective score.")

parser.add_argument("--dst", dest="dst", default="/data/savvas/incels/data/perspective_dict_final2.sqlite",
                    help="If present, runs author_dict, otherwise, runs for channel_dict.")

args = parser.parse_args()

dst = args.dst
dict_db = SqliteDict(dst, tablename="perspective", journal_mode="OFF")
tmp_dict = dict()

fs = [open(f, "r") for f in args.src]

count = 0
now = datetime.datetime.now()

print("start")
for f in fs:
    for line in f:
        count += 1
        line = json.loads(line)

        tmp_dict[line["id_post"]] = line["hate_output"]["SEVERE_TOXICITY"]

        if count % 1000000 == 0:
            for key, item in tmp_dict.items():
                dict_db[key] = item

            dict_db.commit()
            tmp_dict = {}
            print(datetime.datetime.now() - now)
            now = datetime.datetime.now()

    for key, item in tmp_dict.items():
        dict_db[key] = item

    dict_db.commit()
    dict_db.close()
    print(datetime.datetime.now() - now)