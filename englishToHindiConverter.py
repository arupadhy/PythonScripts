__author__ = 'arvind'
import urllib.request;
import json;
import xlrd;
import xlwt;


def copyXl():
    workbook = xlrd.open_workbook('hindiWords.xls')
    sheet = workbook.sheet_by_index(0)
    workbook = xlwt.Workbook()
    newSheet = workbook.add_sheet('test')
    for row in range(0,sheet.nrows):
        data = [sheet.cell_value(row, col) for col in range(sheet.ncols)]
        for index, value in enumerate(data):
            if index == 1 and row>0 and value:
                try:
                    if value == '&':
                        value = 'and'
                    value = convertLine(value);
                except:
                    value = "could not convert";
            newSheet.write(row, index, value)

    workbook.save('tamil_version.xls')


def convertLine(englishLine):
        line = " ";
        for word in englishLine.split(' '):
            line += " ";
            if "&" in word:
                word = "and";
            line += convertToHindi(word)
        print(line)
        return line

def convertToHindi(eng):
    url = "http://www.google.com/transliterate/indic?tlqt=1&langpair=en|ta&text="+eng+"%2Cindia&tl_app=3";
    web_host_api = urllib.request.urlopen(url);
    web_host_res = web_host_api.read();
    result = json.loads(web_host_res.decode('utf8'))
    return (result[0]['hws'][0]) +" ";



if __name__ == '__main__':
    #convertToHindi("podi");
    #readFromXl();
    copyXl();
