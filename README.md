## Commands to Make Helper Files

     python ./scripts/get_helper.py --src /data/savvas/incels/data/incels_comments_reddit_lower.ndjson --src /data/savvas/incels/data/inceltears_comments.ndjson --src /data/savvas/incels/data/json/control/reddit/gaming/reddit_gaming_comments.ndjson --src /data/savvas/incels/data/json/control/reddit/random/reddit_random_comments.ndjson --kind all --kind all --kind gaming --kind random --dst /data/savvas/incels/data/
     
and
 
    python ./scripts/get_helper.py --src /data/savvas/incels/data/incels_comments_reddit_lower.ndjson --src /data/savvas/incels/data/inceltears_comments.ndjson --src /data/savvas/incels/data/json/control/reddit/gaming/reddit_gaming_comments.ndjson --src /data/savvas/incels/data/json/control/reddit/random/reddit_random_comments.ndjson --kind all --kind all --kind gaming --kind random --dst /data/savvas/incels/data/ --author_dict

and (for perspective)

     python ./scripts/get_perspective.py --src /data/savvas/incels/data/json/perspective/perspective_redditall_results.txt --dst /data/savvas/incels/data/perspective_dict.sqlite

##

