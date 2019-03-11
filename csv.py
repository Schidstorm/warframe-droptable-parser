import numbers

def stringify(arrayOfDict, locale):
    separator = ';' if locale == 'de' else ','
    if len(arrayOfDict) == 0:
        return ''
    
    columnMapSet = {}
    for line in arrayOfDict:
        for key, value in line.items():
            columnMapSet[key] = 1
    columnMap = [key for key in columnMapSet.keys()]
    
    resultLines = []
    resultLines.append(separator.join(columnMap))

    for line in arrayOfDict:
        resultLine = []
        for c in columnMap:
            if c in line:
                if isinstance(line[c], (int, float)):
                    if locale == 'de':
                        resultLine.append(str(line[c]).replace('.', ',').encode('utf-8').decode('utf-8'))
                    else:
                        resultLine.append(str(line[c]).encode('utf-8').decode('utf-8'))    
                else:
                    resultLine.append("\"" + line[c].encode('utf-8').decode('utf-8') + "\"")
                
            else:
                resultLine.append('')
        resultLines.append(separator.join(resultLine))
    
    return "\n".join(resultLines)


