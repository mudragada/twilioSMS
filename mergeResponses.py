import csv
from utils import cleanupPhoneNum as cleanupPhoneNum
from utils import camelizeWords as camelizeWords

## This takes the assumption of responses.csv has the phonenumber as the first column always
## This also expects the responses.csv file and master_data.csv file

def main():
    responseList = []
    userList = []
    nUserListCols = 0
    nResponseListCols = 0
    try:
        with open('responses.csv', 'r') as responseFile:
            responseFileReader = csv.reader(responseFile)
            nResponseListCols = len(next(responseFileReader))
            responseFile.seek(0)
            for responseFileRow in responseFileReader:
                responseList.append(responseFileRow)
        #print("Number of Response List Cols - " + str(nResponseListCols))

        with open('master_data.csv', 'r') as userFile:
            userFileReader = csv.reader(userFile)
            nUserListCols = len(next(userFileReader))
            userFile.seek(0)
            for userFileRow in userFileReader:
                userList.append(userFileRow)
        #print("Number of User List Cols - " + str(nUserListCols))

        with open('merged_master_data.csv', 'w') as mergeFile:
            mergeFileWriter = csv.writer(mergeFile)
            for userRow in userList:
                combinedRow = []
                for i in range(0,nUserListCols):
                    matchedRow = False
                    if(userRow[i]):
                        if(str(userRow[i]).isnumeric() or (userRow[i][0] == '+' and len(userRow[i]) == 12)):
                            combinedRow.append(cleanupPhoneNum(userRow[i]))
                        else:
                            combinedRow.append(camelizeWords(userRow[i]))
                        for responseRow in responseList:
                            for j in range(0,nResponseListCols):
                                if(responseRow[j]):
                                    if(((str(responseRow[j]).isnumeric() or (responseRow[j][0] == '+' and len(responseRow[j]) == 12)) and (cleanupPhoneNum(userRow[i]) == cleanupPhoneNum(responseRow[j]))) or (camelizeWords(userRow[i]) == camelizeWords(responseRow[j]))):
                                        for k in range(i+1,nUserListCols):
                                            combinedRow.append(userRow[k])
                                        for l in range(j+1,nResponseListCols):
                                            combinedRow.append(responseRow[l])
                                        matchedRow = True
                    else:
                        combinedRow.append('')
                    if(matchedRow == True):
                        break
                #print(combinedRow)
                mergeFileWriter.writerow(combinedRow)
    except OSError as e:
        print('OS/File Missing Error')
    except IOError as ioe:
        print('I/O error')
    except IndexError as ie:
        print('IndexError')

if __name__ == '__main__':
    main()
