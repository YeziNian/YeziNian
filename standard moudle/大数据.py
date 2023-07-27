import os
import os.path
import time

def FileSplit(sourcefile, targetFolder):
    if not os.path.isfile(sourcefile):
        print(sourcefile, "does not exist!")
        return
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)
    tempDate = []
    number = 1000
    fileNum = 1
    with open(sourcefile, "r", encoding="utf-8") as fp:
        dataLine = fp.readline().strip()
        while dataLine:
            for i in range(number):
                tempDate.append(dataLine)
                dataLine = fp.readline()
                if not dataLine:
                    break
            desFile = os.path.join(targetFolder, sourcefile[0:-4]+str(fileNum)+'.txt')
            with open(desFile, "a+") as fp:
                fp.writelines(tempDate)
            tempDate = []
            fileNum = fileNum+1
if __name__ == '__main__':
    souceFile = r"C:\Users\40437\Desktop\《遮天》1.txt"
    target = "test"
    #FileSplit(souceFile, target)