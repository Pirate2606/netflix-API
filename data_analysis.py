import pandas as pd

df = pd.read_csv("netflix_titles.csv")
pd.set_option('display.max_colwidth', None)


def get_all_titles():
    result_dict = dict()
    for count, item in enumerate(df.iterrows()):
        result_dict[count] = item[1].title
    return result_dict


def get_info_title(title):
    result_row = df[df["title"] == title]
    result_dict = dict()
    discard = ["show_id", "date_added"]
    for item in result_row.iteritems():
        if item[0] in discard:
            continue
        else:
            result_dict[item[0]] = item[1].to_string(index=False)
    return result_dict


def get_type(type_):
    result = df[df["type"] == type_]
    result_dict = dict()
    for item in result.iterrows():
        result_dict[item[1].title] = get_info_title(item[1].title)
    return result_dict


def get_directors(director):
    result = df[df["director"] == director]
    result_dict = dict()
    temp_list = list()
    for item in result.iterrows():
        temp_list.append(get_info_title(item[1].title))
    result_dict[director] = temp_list
    return result_dict


def get_particular_year(year):
    result = df[df["release_year"] == year]
    result_dict = dict()
    temp_list = list()
    for item in result.iterrows():
        temp_list.append(item[1].title)
    result_dict[str(year)] = temp_list
    return result_dict


def get_year():
    data = df.sort_values("release_year")
    all_years = data.release_year.unique()
    result_dict = dict()
    for count, year in enumerate(all_years):
        result_dict[count] = get_particular_year(year)
    return result_dict
