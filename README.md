## Commands to Make Helper Files

     python ./scripts/get_helper.py \
     --src /data/savvas/incels/data/incels_comments_reddit_lower.ndjson \
     --src /data/savvas/incels/data/inceltears_submissions.ndjson \
     --src /data/savvas/incels/data/json/control/reddit/gaming/reddit_gaming_comments.ndjson \
     --src /data/savvas/incels/data/json/control/reddit/random/reddit_random_comments.ndjson \
     --dst /data/savvas/incels/data/
     
and
 
    python ./scripts/get_helper.py \
    --src /data/savvas/incels/data/incels_comments_reddit_lower.ndjson \
    --src /data/savvas/incels/data/inceltears_submissions.ndjson \
    --src /data/savvas/incels/data/json/control/reddit/gaming/reddit_gaming_comments.ndjson \
    --src /data/savvas/incels/data/json/control/reddit/random/reddit_random_comments.ndjson \
    --dst /data/savvas/incels/data/ \
    --author_dict
