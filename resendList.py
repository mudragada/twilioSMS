from time import sleep
import re, csv
from utils import camelizeWords as camelizeWords
from utils import cleanupPhoneNum as cleanupPhoneNum

## This takes the assumption of responses.csv has the phonenumber as the first column always
## This also expects the errors.csv file and master_data.csv file

def main():
    try:
        with open('errors.csv', 'r') as error_data:
            error_data_lines = error_data.readlines()
        masterDataDict = {}
        errorDataDict = {}
        with open('master_data.csv', 'r') as master_data:
            master_data_lines = master_data.readlines()

        error_data_lines_cleanedup = []
        for error_data_line in error_data_lines:
            error_phone_number = cleanupPhoneNum(error_data_line)
            error_data_lines_cleanedup.append(error_phone_number)
        for master_data_line in master_data_lines:
            master_data_line_list = master_data_line.split(',')
            if(master_data_line_list[2] and master_data_line_list[2] != '\n'):
                master_data_phone_number = cleanupPhoneNum(master_data_line_list[2])
                #master_data_lastname = camelizeWords(master_data_line_list[1])
                master_data_lastname = ''
                master_data_firstname = camelizeWords(master_data_line_list[0])
                if(master_data_lastname != ''):
                    fullname = (master_data_firstname + " " + master_data_lastname)
                else:
                    fullname = master_data_firstname
                if (master_data_phone_number in error_data_lines_cleanedup):
                    errorDataDict[master_data_phone_number] = fullname

#### write error data to resendlist.csv
        csv_columns = ['PhoneNumber', 'FullName']
        csv_file = "resendlist.csv"
        with open(csv_file, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in errorDataDict.items():
                writer.writerow([value, key])

    except OSError as e:
        print('OS/File Missing Error')
    except IOError as ioe:
        print('I/O error')
    except IndexError as ie:
        print('IndexError')

if __name__ == '__main__':
    main()
