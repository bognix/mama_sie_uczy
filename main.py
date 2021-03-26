import pandas as pd

def read_excel():
    excel_data_frame = pd.read_excel(r'mama_przyklad.xlsx')
    excel_data_frame['ABS_PERCENTAGE'] = excel_data_frame.apply(calculate_abs_time, axis=1)
    excel_data_frame.to_excel('mama_przyklad_z_kolumna.xlsx')

    # calculate abs daily per program
    # get all rows with desired program
    # divide ABS_TIME_OFF by WH for each row
    # {2018-01-01: 0.7}


def calculate_abs_time(row):
    wh = row.get('WH')
    abs_time_off = row.get('ABS_TIME_OFF')
    abs_percentage = abs_time_off / wh
    return abs_percentage


def calculate_abs_time_old(df, program):
    result = {}
    enter_sales_data_frame = df[df['PROGRAM'] == program]

    for index, row in enter_sales_data_frame.iterrows():
        date = row.get('DATE')
        wh = row.get('WH')
        abs_time_off = row.get('ABS_TIME_OFF')
        abs_percentage = abs_time_off / wh
        result[date] = abs_percentage

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_excel()
