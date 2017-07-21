def ctlFormat(**kwargs):
    # must have!!!
    keySet = ['path', 'table', 'type', 'field']
    qry = "LOAD DATA\nINFILE '{path}'\nINTO TABLE {table}\n{type}\nFIELDS TERMINATED BY ','\nTRAILING NULLCOLS(\n{field}\n)"
    chkNext, noHasKey = hasKey(*keySet, **kwargs)
    return printQry(chkNext, qry, *noHasKey, **kwargs)
    '''
    for key in keySet:
        if kwargs.has_key(key):
            pass
        else:
            chkNext = False
            noHasKey.append(key)
    '''
    '''
    if chkNext is False:
        rst = " {}, "
        rst = rst * len(noHasKey)
        return "key is needed this field "+rst.format(*noHasKey).rstrip().rstrip(',')+'\n' + qry
    else:
        return qry.format(**kwargs)
    '''
def sqlloaderCmd(**kwargs):
    #must have!!
    keySet = ['abc','cde']
    qry = 'sqlldr {} '
    chkNext, noHasKey = hasKey(*keySet, **kwargs)
    return printQry(chkNext, qry, *noHasKey, **kwargs)


def printQry(chkNext, qry, *noHasKey, **kwargs):
    if chkNext is False:
        rst = " {}, "
        rst = rst * len(noHasKey)
        return "key is needed this field "+rst.format(*noHasKey).rstrip().rstrip(',')+'\n' + qry
    else:
        return qry.format(**kwargs)

def hasKey(*keys, **kwargs):
    rst = True
    needKeys = []
    for key in keys:
        if kwargs.has_key(key) is False:
            rst = False
            needKeys.append(key)
    return rst, needKeys
