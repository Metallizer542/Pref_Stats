import pandas as pd


def load_excel_file(filename, sheet_name):
    excelfile = pd.read_excel(filename, sheet_name=sheet_name)
    return excelfile


def get_data_frame(excelfile):
    df = pd.DataFrame(excelfile)
    return df


def get_users(excelfile):
    return


def get_bullets(excelfile):
    return


def get_game_date(df):
    return


def get_rows_by_bullet_range(df, bulletrange):
    result = df.loc[df['Пуля'] == int(bulletrange)]
    return result


def get_all_games_for_user(df, user):
    temp_table_without_Nan = df[~df[user].isnull()]
    temp_dataframe = get_data_frame(pd.DataFrame(temp_table_without_Nan))
    result = temp_dataframe[['Дата игры', 'Пуля', user]]
    return result


test1 = load_excel_file('Pref.xlsx', sheet_name='Результаты')

df = get_data_frame(test1)
# print(get_rows_by_bullet_range(df, 10))
print(get_all_games_for_user(df, 'Целый'))
