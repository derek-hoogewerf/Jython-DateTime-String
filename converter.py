from java.util import Calendar, GregorianCalendar, Date

def convert_datetime_bst_to_javaSQLTimestamp( datetime_val ):
    if datetime_val is None: return None
    assert type( datetime_val ) is datetime.datetime
    tz_local = tz.tzlocal()
    gmt_datetime = datetime_val - tz_local.dst( datetime_val )
    delta = gmt_datetime - datetime.datetime( 1970, 1, 1 )
    seconds = int( delta.total_seconds() ) 
    ms_fraction = int( delta.microseconds / 1000 )
    ms = seconds * 1000 + ms_fraction
    return java.sql.Timestamp( ms )

def conv_ms_to_datetime_bst( ms ):
    assert type( ms ) is long, '# ms type %s' % ( type( ms ), )
    # NB potentially a problem with pre-1970 and post-2038 dates: datetime.datetime.fromtimestamp(ms/1000.0)
    gmt_datetime = datetime.datetime( 1970, 1, 1 ) + datetime.timedelta( 0, 0, 0, ms )
    tz_local = tz.tzlocal()
    return gmt_datetime + tz_local.dst( gmt_datetime )
#OR
SimpleDateFormat myDate = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");
myDate.setTimeZone(TimeZone.getTimeZone("BST"));
Date newDate = myDate.parse("2010-05-23T09:01:02");
