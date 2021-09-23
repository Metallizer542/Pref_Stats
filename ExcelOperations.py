import pandas as pd

import MathOperations


def load_excel_file(filename, sheet_name):
    excelfile = pd.read_excel(filename, sheet_name=sheet_name)
    return excelfile


def get_data_frame(excelfile):
    df = pd.DataFrame(excelfile)
    return df


def get_users(df):
    users = []
    users_raw = list(df.head().columns)
    for user_index in range(2, len(users_raw)):
        users.append(users_raw[user_index])
    return users


def get_bullets_values(df):
    bullet_values = set(df['Пуля'])
    return bullet_values


def get_game_dates(df):
    game_dates = list(df['Дата игры'])
    return game_dates


def get_rows_by_bullet_range(df, bulletrange):
    result = df.loc[df['Пуля'] == int(bulletrange)]
    return result


def get_all_games_for_user(df, user):
    temp_table_without_Nan = df[~df[user].isnull()]
    temp_dataframe = get_data_frame(pd.DataFrame(temp_table_without_Nan))
    result = temp_dataframe[['Дата игры', 'Пуля', user]]
    return result


def get_all_stats_for_user_by_bulletRange(df, user, bullet):
    all_games = get_all_games_for_user(df, user)
    temp_df = get_data_frame(all_games)
    all_scores = get_rows_by_bullet_range(temp_df, bullet)
    return all_scores


def get_user_scores_by_bulletRange(df, user, bullet):
    all_scores = get_all_stats_for_user_by_bulletRange(df, user, bullet)
    values = list(all_scores[user])
    return values


def get_user_scores_and_dates_by_bulletRange(df, user, bullet):
    all_scores = get_all_stats_for_user_by_bulletRange(df, user, bullet)
    scores_by_date_and_user = all_scores[['Дата игры', user]]
    return scores_by_date_and_user


def get_count_of_games_for_user_by_bulletRange(df, user, bullet):
    counts = []
    all_scores = get_all_stats_for_user_by_bulletRange(df, user, bullet)
    count_of_games = list(all_scores['Дата игры'])
    for x in range(0, len(count_of_games)):
        counts.append(x + 1)
    all_scores['Количество игр'] = counts
    return all_scores


test1 = load_excel_file('Pref.xlsx', sheet_name='Результаты')

df = get_data_frame(test1)
# print(get_rows_by_bullet_range(df, 10))
# print(get_all_games_for_user(df, 'Целый'))
# print(get_bullets_values(df))
# print(get_users(df))
# dates = get_game_dates(df)


score = get_user_scores_by_bulletRange(df, 'Целый', '10')
games_and_scores = get_user_scores_and_dates_by_bulletRange(df, 'Целый', '15')
# MathOperations.print_plot(pd.DataFrame(games_and_scores)))

print(get_count_of_games_for_user_by_bulletRange(df, 'Целый', '10'))

# print(MathOperations.get_standard_deviation(score))
# print(MathOperations.get_expected_value(score))
# print(MathOperations.get_average_median_value(score))
# print(MathOperations.get_average_median_value(score))
# print(get_game_dates(df))
