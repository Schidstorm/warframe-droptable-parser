def stringify(arrayOfDict, separator):
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
                resultLine.append(str(line[c]))
            else:
                resultLine.append('')
        resultLines.append(separator.join(resultLine))
    
    return "\n".join(resultLines)


