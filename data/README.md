# Data

We make available data related to subreddit and standalone forums from the manosphere.
We also make available Perspective API annotations for all posts.

You can find the data in [Zenodo](https://zenodo.org/record/4007913).

You can find the code in [GitHub](https://github.com/manoelhortaribeiro/manosphere_analysis).

Please cite this paper if you use this data:

~~~bibtex
@article{ribeiroevolution2021,
    title={The Evolution of the Manosphere Across the Web},
    author={Ribeiro, Manoel Horta and Blackburn, Jeremy and Bradlyn, Barry and De Cristofaro, Emiliano and Stringhini, Gianluca and Long, Summer and Greenberg, Stephanie and Zannettou, Savvas},
    booktitle = {{Proceedings of the 15th International AAAI Conference on Weblogs and Social Media (ICWSM'21)}},
    year={2021}
}
~~~
 

# Reddit

We make available data for forums and for relevant subreddits (56 of them, as described in `subreddit_descriptions.csv`).
These are available, 1 line per post in each subreddit Reddit in `/ndjson/reddit.ndjson`.
A sample for example is:
 
    {
      "author": "Handheld_Gaming",
      "date_post": 1546300852,
      "id_post": "abcusl",
      "number_post": 9.0,
      "subreddit": "Braincels",
      "text_post": "Its been 2019 for almost 1 hour And I am at a party with 120 people, half of them being foids. 
      The last year had been the best in my life. I actually was happy living hope because I was redpilled to the death.
      \n\nNow that I am blackpilled I see that I am the shortest of all men and that I am the only one with a recessed 
      jaw. \n\nIts over. Its only thanks to my age old friendship with chads and my social skills I had developed in the
       past year that a lot of men like me a lot as a friend.\n\nNo leg lengthening syrgery is gonna save me. Ignorance 
       was a bliss. Its just horror now seeing that everyone can make out wirth some slin hoe at the party. \n\n
       I actually feel so unbelivably bad for turbomanlets. Life as an unattractive manlet is a pain, I cant imagine 
       the hell being an ugly turbomanlet is like. I would have roped instsntly if I were one. Its so unfair. 
       \n\nTallcels are fakecels and they all can (and should) suck my cock. \n\nIf I were 17cm taller my life would be
        a heaven and I would be the happiest man alive. \n\nJust cope and wait for affordable body tranpslants.",
      "thread": "t3_abcusl"
    }
     

# Forums

We here describe the `.sqlite` and `.ndjson` files that contain the data from the following forums.

    (avfm)           --- https://d2ec906f9aea-003845.vbulletin.net 
    (incels)         --- https://incels.co/
    (love_shy)       --- http://love-shy.com/lsbb/
    (redpilltalk)    --- https://redpilltalk.com/
    (mgtow)          --- https://www.mgtow.com/forums/
    (rooshv)         --- https://www.rooshvforum.com/
    (pua_forum)      --- https://www.pick-up-artist-forum.com/
    (the_attraction) --- http://www.theattractionforums.com/
    
The files are in folders `/sqlite/` and `/ndjson`.

## `.sqlite`

All the tables in the `sqlite.` datasets follow a very simple `{key:value}` format. 
Each `key` is a thread name (for example `/threads/housewife-is-like-a-job.123835/`) and each value is a python dictionary or a list.
This file contains three tables:

- `idx`  each key is the relative address to a thread and maps to a post. Each post is represented by a dict:

      "type":           (list) in some forums you can add a descriptor such as
                        [RageFuel] to each topic, and you may also have special
                        types of posts, like sticked/pool/locked posts.                       
      "title":          (str) title of the thread;
      "link":           (str) link to the thread;
      "author_topic":   (str) username that created the thread;
      "replies":        (int) number of replies, may differ from number of
                        posts due to difference in crawling date;
      "views":          (int) number of views;
      "subforum":       (str) name of the subforum;
      "collected":      (bool) indicates if raw posts have been collected;
      "crawled_idx_at": (str) datetime of the collection.

- `processed_posts` each key is the relative address to a thread and maps to a list with posts (in order). Each post is represented by a dict:

      "author":              (str) author's username;
      "resume_author":       (str) author's little description;
      "joined_author":       (str) date author joined;
      "messages_author":     (int) number of messages the author has;
      "text_post":           (str) text of the main post;
      "number_post":         (int) number of the post in the thread;
      "id_post":             (str) unique post identifier (depends), 
                                   for sure unique within thread;
      "id_post_interaction": (list) list with other posts ids this 
                                    post quoted;
      "date_post":           (str) datetime of the post,
      "links":               (tuple) nice tuple with the url parsed, e.g. 
                                     ('https', 'www.youtube.com', '/S5t6K9iwcdw');
      "thread":              (str) same as key;
      "crawled_at":          (str) datetime of the collection.
      

- `raw_posts` each key is the relative address to a thread and maps to a list with unprocessed posts (in order). Each post is represented by a dict:

      "post_raw":   (binary) raw html binary;
      "crawled_at": (str) datetime of the collection.
      
## `.ndjson`

Each line consists of a json object representing a different comment with the following fields:

      "author":              (str) author's username;
      "resume_author":       (str) author's little description;
      "joined_author":       (str) date author joined;
      "messages_author":     (int) number of messages the author has;
      "text_post":           (str) text of the main post;
      "number_post":         (int) number of the post in the thread;
      "id_post":             (str) unique post identifier (depends), 
                                   for sure unique within thread;
      "id_post_interaction": (list) list with other posts ids this 
                                    post quoted;
      "date_post":           (str) datetime of the post,
      "links":               (tuple) nice tuple with the url parsed, e.g. 
                                     ('https', 'www.youtube.com', '/S5t6K9iwcdw');
      "thread":              (str) same as key;
      "crawled_at":          (str) datetime of the collection.
                       

# Perspective

We also run each post and reddit post through perspective, the files are located in the `/perspective/` folder.
They are compressed with gzip.
 One example output

    {
    "id_post": 5200,
    "hate_output": {
    "text": "I still can\u2019t wrap my mind around both of those articles about these c\~\~\~s sleeping with poor 
        Haitian Men. Where\u2019s the uproar?, where the hell is the outcry?, the \u201cpig\u201d comments or the 
        \u201ccreeper comments\u201d. F\~\~\~ing hell, if roles were reversed and it was an article about Men going to 
        Europe where under 18 sex in legal, you better believe they would crucify the writer of that article and DEMAND 
        an apology by the paper that wrote it.. This is exactly what I try and explain to people about the double 
        standards within our modern society. A bunch of older women, wanna get their kicks off by sleeping with poor 
        Men, just before they either hit or are at menopause age. F~~~ing unreal, I\u2019ll never forget going to Sweden
        and Norway a few years ago with one of my buddies and his girlfriend who was from there, the legal age of 
        consent in Norway is 16  and in Sweden it\u2019s 15. I couldn\u2019t believe it, but my friend told me \u201c 
        hey, it\u2019s normal  here\u201d . Not only that but the age wasn\u2019t a big different in other European 
        countries as well.  One thing i learned very quickly was how very Misandric Sweden as well as Denmark were.",
    "TOXICITY": 0.6079781,
    "SEVERE_TOXICITY": 0.53744453,
    "INFLAMMATORY": 0.7279288,
    "PROFANITY": 0.58842486,
    "INSULT": 0.5511079,
    "OBSCENE": 0.9830818,
    "SPAM": 0.17009115
    }
    }
    
# Working with sqlite

A nice way to read some of the files of the dataset is using `SqliteDict`, for example:

```
from sqlitedict import SqliteDict
processed_posts = SqliteDict("./data/forums/incels.sqlite", 
                             tablename="processed_posts")

for key, posts in processed_posts.items():
    for post in posts:
        # here you could do something with each post in the dataset
        pass
```

# Helpers

Additionally, we provide two `.sqlite` files that are helpers used in the analyses. 
These are related to reddit, and not to the forums!
They are:

- `channel_dict.sqlite` a sqlite where each key corresponds to a subreddit and values are lists of dictionaries users who posted on it, along with timestamps.

- `author_dict.sqlite` a sqlite where each key corresponds to an author and values are lists of dictionaries of the subreddits they posted on, along with timestamps.

These are used in the paper for the migration analyses.

# Examples and particularities for forums

Although we did our best to clean the data and be consistent across forums, this is not always possible. In the following subsections we talk about the particularities of each forum, directions to improve the parsing which were not pursued as well as give some examples on how things work in each forum.

## incels

Check out an archived version of the [front page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/incels_front_page.png), the [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/incels_thread_page.png) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/incels_post_page.png), as well as a dump of the data stored for a [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/incels_thread_page_example.txt) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/incels_post_page_example.txt).

- *types*: for the incel forums the special types associated with each thread in the `idx` table are "Sticky", "Pool", "Closed", and the custom types added by users, such as `[LifeFuel]`. These last ones are all in brackets. You can see some examples of these in the on the example thread page.

- *quotes*: quotes in this forum were quite nice and thus, all quotations are deterministic.

## LoveShy

Check out an archived version of the [front page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/love_shy_front_page.png), the [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/love_shy_thread_page.png) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/love_shy_thread_page.png), as well as a dump of the data stored for a [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/love_shy_thread_page_example.txt) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/love_shy_post_page_example.txt).

- *types*: no types were parsed. There are some rules in the forum, but not significant.

- *quotes*: quotes were obtained from exact text+author match, or author match + a jaccard similarity of more than 0.9 in the tokens of the text split on spaces.

- *other*: this forum apparently deleted a bunch of posts (or hid them from new users). 

## MGTOW

Check out an archived version of the [front page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/mgtow_front_page.png), the [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/mgtow_thread_page.png) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/mgtow_thread_page.png), as well as a dump of the data stored for a [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/mgtow_thread_page_example.txt) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/mgtow_post_page_example.txt).

- *types*: no types were parsed. There are some rules in the forum, but not significant.

- *quotes*: quotes in this forum were quite nice and thus, all quotations are deterministic.

- *other*: collecting users for this forum was hard because info like number of threads and join date do not show on the threads. Thus there was a 2-step collection. Some users may be missing because of this.

## A Voice for Men

Check out an archived version of the [front page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/avfm_front_page.png), the [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/avfm_thread_page.png) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/avfm_thread_page.png), as well as a dump of the data stored for a [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/avfm_thread_page_example.txt) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/avfm_post_page_example.txt).

- *types*: "sticky" is the only existing type.

- *quotes*: quotes in this forum were quite nice and thus, all quotations are deterministic.

## Red Pill Talk (formerly sluthate.com)

Check out an archived version of the [front page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/avfm_front_page.png), the [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/avfm_thread_page.png) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/avfm_thread_page.png), as well as a dump of the data stored for a [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/avfm_thread_page_example.txt) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/avfm_post_page_example.txt).


- *types*: no types were parsed.

- *quotes*: quotes were obtained from exact text+author match, or author match + a jaccard similarity of more than 0.9 in the tokens of the text split on spaces.

## The Attraction

Check out an archived version of the [front page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/the_attraction_front_page.png), the [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/the_attraction_thread_page.png) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/the_attraction_thread_page.png), as well as a dump of the data stored for a [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/the_attraction_thread_page_example.txt) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/the_attraction_post_page_example.txt).

- *types*: "sticky" is the only existing type.

- *quotes*: quotes in this forum were quite nice and thus, all quotations are deterministic.

- *other*: there is the possibility to parse stuff like age and location, but this was not done.

## PUA Forum

Check out an archived version of the [front page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/pua_forum_front_page.png), the [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/pua_forum_thread_page.png) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/pua_forum_thread_page.png), as well as a dump of the data stored for a [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/pua_forum_thread_page_example.txt) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/pua_forum_post_page_example.txt).

- *types*: There are several types parsed: Sticky, Announcement, General Announcement, Locked, to name a few.

- *quotes*: quotes were obtained from exact text match, or a jaccard similarity of more than 0.9 in the tokens of the text split on spaces. There are actually some problems with quotes with other quotes inside (check example .txt).

## Rooshv

Check out an archived version of the [front page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/rooshv_front_page.png), the [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/rooshv_thread_page.png) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/screenshots/pua_forum_thread_page.png), as well as a dump of the data stored for a [thread page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/rooshv_thread_page_example.txt) and a [post page](https://github.com/manoelhortaribeiro/manosphere_analysis/blob/master/data/forums/examples/rooshv_post_page_example.txt).

- *types*: Two types parsed: `sticky`, `announcement`.

- *quotes*: quotes in this forum were quite nice and thus, all quotations are deterministic.

- *other*: lots of posts have some problem with dates, which is quite annoying (~5%). Some threads could not be captured also, website behaves a bit weird. Some don't exist.

