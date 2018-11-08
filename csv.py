def stringify(arrayOfDict, separator):
    if len(arrayOfDict) == 0:
        return ''.encode('utf-8')
    
    columnMapSet = {}
    for line in arrayOfDict:
        for key, value in line.items():
            columnMapSet[key] = 1
    columnMap = [key.encode('utf-8') for key in columnMapSet.keys()]
    
    resultLines = []
    resultLines.append(separator.encode('utf-8').join(columnMap))

    for line in arrayOfDict:
        resultLine = []
        for c in columnMap:
            if c in line:
                if isinstance(line[c], (int, float)):
                    resultLine.append(str(line[c]).encode('utf-8'))
                else:
                    resultLine.append(line[c].encode('utf-8'))
                
            else:
                resultLine.append(''.encode('utf-8'))
        resultLines.append(separator.encode('utf-8').join(resultLine))
    
    return "\n".encode('utf-8').join(resultLines)


