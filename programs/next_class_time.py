import urllib2
import datetime

def get_next_class_string_date():
    '''gets the programming class date from the web page'''
    CLASS_URL= "http://services.quorumverita.com/programming_classes"
    page_content= urllib2.urlopen( CLASS_URL ).read()   #get the html page 
    i1= page_content.index("2012")                      #look for "2012"
    i2= page_content.index("Z", i1)                     #and the end of the datetime string ("Z")
    date_str= page_content[i1:i2+1]                     #copy the datetime string from the page
    date= datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%MZ") #convert to a python datetime
    return date

def round_timedelta( d ):
    '''rounds a timedelta to 1 second precision'''
    s= d.total_seconds()    #gets the total seconds the timedelta represents
    s= round( s )             #rounds it (no decimal places)
    return datetime.timedelta( seconds= s ) #create a new timedelta with the rounded amount of seconds

def get_local_utc_offset():
    '''gets the utc offset of the local timezone'''
    utc_offset= datetime.datetime.now() - datetime.datetime.utcnow()
    #we must round the result, since some time has elapsed between now() and utcnow()
    return round_timedelta( utc_offset )
 
utc_date=       get_next_class_string_date()
local_date=     utc_date + get_local_utc_offset()
time_missing=   round_timedelta( local_date - datetime.datetime.now() )

print "class time (utc):",      utc_date
print "class time (local):",    local_date
print "time missing:",          time_missing
