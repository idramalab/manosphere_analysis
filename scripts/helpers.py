from heapq import heappop, heappush
import numpy as np
import pandas as pd
import scipy.stats


def human_format(num, pos=None):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'B', 'T', 'P'][magnitude])


colors = {
    "Alt-right": "#f93e49",
    "Alt-lite": "#019441",
    "Intellectual Dark Web": "#35598a"
}

bins = [
    (0, 1146398400000),  # - Apr 30,06
    (1146398400000, 1177934400000),  # Apr 30,06 - Apr 30,07
    (1177934400000, 1209556800000),  # Apr 30,07 - Apr 30,08
    (1209556800000, 1241092800000),  # Apr 30,08 - Apr 30,09
    (1241092800000, 1272628800000),  # Apr 30,09 - Apr 30,10
    (1272628800000, 1304164800000),  # Apr 30,10 - Apr 30,11
    (1304164800000, 1335787200000),  # Apr 30,11 - Apr 30,12
    (1335787200000, 1367323200000),  # Apr 30,12 - Apr 30,13
    (1367323200000, 1398859200000),  # Apr 30,13 - Apr 30,14
    (1398859200000, 1430395200000),  # Apr 30,14 - Apr 30,15
    (1430395200000, 1462017600000),  # Apr 30,15 - Apr 30,16
    (1462017600000, 1493553600000),  # Apr 30,16 - Apr 30,17
    (1493553600000, 1525089600000),  # Apr 30,17 - Apr 30,18
    (1525089600000, 1527768000000),  # Apr 30,18 - May 31,18
    (1527768000000, 1530360000000),  # May 31,18 - Jun 30,18
    (1530360000000, 1533038400000),  # Jun 30,18 - Jul 31,18
    (1533038400000, 1535716800000),  # Jul 31,18 - Aug 31,18
    (1535716800000, 1538308800000),  # Aug 31,18 - Sep 30,18
    (1538308800000, 1540987200000),  # Sep 30,18 - Oct 31,18
    (1540987200000, 1543579200000),  # Oct 31,18 - Nov 30,18
    (1543579200000, 1546257600000),  # Nov 30,18 - Dec 31,18
    (1546257600000, 1548936000000),  # Dec 31,18 - Jan 31,19
    (1548936000000, 1551355200000),  # Jan 31,19 - Feb 28,19
    (1551355200000, 1554033600000),  # Feb 28,19 - Mar 31,19
    (1554033600000, 1556625600000)  # Mar 31,19 - Apr 30,19
]

bins_y_o = [
    (1209556800000, 1241092800000),  # Apr 30,08 - Apr 30,09
    (1241092800000, 1272628800000),  # Apr 30,09 - Apr 30,10
    (1272628800000, 1304164800000),  # Apr 30,10 - Apr 30,11
    (1304164800000, 1335787200000),  # Apr 30,11 - Apr 30,12
    (1335787200000, 1367323200000),  # Apr 30,12 - Apr 30,13
    (1367323200000, 1398859200000),  # Apr 30,13 - Apr 30,14
    (1398859200000, 1430395200000),  # Apr 30,14 - Apr 30,15
    (1430395200000, 1462017600000),  # Apr 30,15 - Apr 30,16
    (1462017600000, 1493553600000),  # Apr 30,16 - Apr 30,17
    (1493553600000, 1525089600000),  # Apr 30,17 - Apr 30,18
    (1525089600000, 1556625600000)  # Apr 30,18 - Apr 30,19
]

bins_t = ["", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "Apr",
          "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]

bins_t_o = ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]

bins_t_s = ["2006-2012", "2013-2015", "2016", "2017", "2018"]

bins_y_s = [
    (1146398400000, 1367323200000),  # Apr 30,06 - Apr 30,13
    (1367323200000, 1462017600000),  # Apr 30,13 - Apr 30,16
    (1462017600000, 1493553600000),  # Apr 30,16 - Apr 30,17
    (1493553600000, 1525089600000),  # Apr 30,17 - Apr 30,18
    (1525089600000, 1556625600000)  # Apr 30,18 - Apr 30,19
]


def triple_bin_to_df(keys, bin1, bin2, bin3, fun):
    vals = []
    for k in keys:
        val = fun(bin1[k], bin2[k], bin3[k])
        val["idx"] = k
        vals.append(val)
    return pd.DataFrame(vals)


def bin_to_df(keys, bin1, bin2, fun):
    vals = []
    for k in keys:
        val = fun(bin1[k], bin2[k])
        val["idx"] = k
        vals.append(val)
    return pd.DataFrame(vals)


def intersec_3(x, y, z):
    s_x, s_y, s_z = set([it_x for it_x in x]), \
                    set([it_y for it_y in y]), \
                    set([it_z for it_z in z])

    s_xy = s_x.intersection(s_y)
    s_xyz = s_xy.intersection(s_z)
    s_xuyuz = s_x.union(s_y).union(s_z)

    tmp = {"xyz": len(s_xyz),
           "xyz_p": len(s_xyz) / len(s_xuyuz) if len(s_xuyuz) != 0 else 0}
    return tmp


def _jaccard(s1, s2):
    intersection_cardinality = len(set.intersection(*[s1, s2]))
    union_cardinality = len(s1) + len(s2) - intersection_cardinality
    return intersection_cardinality / float(union_cardinality)


def jaccard(x, y):
    s_x, s_y = set([it_x for it_x in x]), set([it_y for it_y in y])

    tmp = {"x": len(s_x),
           "x-y": len(s_x - s_y),
           "y-x": len(s_y - s_x),
           "y": len(s_y),
           "intersection": len(s_x.intersection(s_y)),
           "jaccard": 0}

    n_x, n_y = len(s_x), len(s_y)

    if n_x == 0 or n_y == 0:
        tmp["jaccard"] = 0
        return tmp

    tmp["jaccard"] = _jaccard(s_x, s_y)
    return tmp


def sliding_heaps(h1, h2, f, time_f, window_size=2.628e+9, window_step=2.628e+9):
    get_p = lambda x: x[0][0]
    q1, q2, vals = [], [], []
    p_global = min(get_p(h1), get_p(h2))

    while len(h1) != 0 and len(h2) != 0:

        try:
            while get_p(h1) - p_global < window_size:
                heappush(q1, heappop(h1))
        except IndexError:
            pass

        try:
            while get_p(h2) - p_global < window_size:
                heappush(q2, heappop(h2))
        except IndexError:
            pass

        tmp = f(q1, q2)
        tmp["time"] = time_f(p_global)
        vals.append(tmp)

        p_global += window_step

        try:
            while get_p(q1) < p_global:
                heappop(q1)
        except IndexError:
            pass

        try:
            while get_p(q2) < p_global:
                heappop(q2)
        except IndexError:
            pass

    return vals


def add_user_to_bin(b, user, timestamp_v):
    for lower, upper in b.keys():
        if upper > timestamp_v >= lower:
            b[(lower, upper)].add(user)
            break


def populate_bin_with_channel(channel, channel_dict, bin_dict):
    if channel in channel_dict:
        for user in channel_dict[channel]:
            add_user_to_bin(bin_dict, user["author"], user["timestamp"])


def add_user_categories_to_bin(b, user, category, timestamp_v):
    for lower, upper in b.keys():
        if upper > timestamp_v >= lower:
            user_at_b = b[(lower, upper)].get(user, {"pua": 0, "incels": 0, "trp": 0,
                                                     "health": 0, "mgtow": 0, "mra": 0})
            cat_at_b = user_at_b.get(category, 0)
            cat_at_b += 1
            user_at_b[category] = cat_at_b
            b[(lower, upper)][user] = user_at_b
            break


# calculate mean with confidence intervals
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    return {"mean": m, "lower": m - h, "upper": m + h}


# normalize_user_bins
def normalize_user_bins(b):
    for lower, upper in b.keys():
        for user, cats in b[(lower, upper)].items():
            count = sum([v for k, v in cats.items()])
            new_cats = {k: v / count for k, v in cats.items()}
            new_cats["count"] = count
            b[(lower, upper)][user] = new_cats


# find users in the bin with a given constraint
def find_users_constraint(b, key, constraint):
    return [user for user, cats in b[key].items() if constraint(cats)]


# track users in other bins
def find_users_other_bin(b, key, users_to_track, constraint=lambda x: True):
    users_tracked = list(set([user for user, cats in b[key].items()]).intersection(set(users_to_track)))
    users_tracked = [user for user in users_tracked if constraint(b[key][user])]
    return users_tracked


# estimate a number in the bins
def estimate_for_users(b, key, users_to_track, estimate):
    return estimate([b[key][user] for user in users_to_track])
