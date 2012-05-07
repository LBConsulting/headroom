def jsonfileload(config):
    """
    Keeping the kwarg for quick loads
    """
    retpath = os.path.join(CONFIG_ROOT, config)
    with open(retpath, 'r') as retfile:
        retjson = retfile.read()
    ret = json.loads(retjson)
    # Just get the slides, not the _doc
    return ret

def jsonfilewrite(writein, config):
    """
    writes and entire key into one file
    """
    retpath = os.path.join(CONFIG_ROOT, config)
    fh, fp = tempfile.mkstemp(suffix=DBSUFFIX, dir=DBFOLDER)
    try:
        jsontowrite = json.dumps(writein)
    except:
        print "ERROR Dumping JSON"
        return False
    try:
        with os.fdopen(fh, 'w') as jsonfile:
            jsonfile.write(jsontowrite)
        jsonfile.close()
        return True
    except:
        print "ERROR Writing File"
        return False


