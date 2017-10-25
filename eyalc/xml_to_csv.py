#import numpy
#import os
#import matplotlib
import sys
from lxml import etree, objectify


def extractEventTimes(fileName):
    with open(fileName) as fd:
        xml=fd.read()

    root = objectify.fromstring(xml)

    events = root.events

    print('idx, class_id, class_name, start_second, end_second')
    for item in events.item:
        print("%d, %d, %s, %f, %f" % (int(item.attrib['idx']), int(item.CLASS_ID), item.CLASS_NAME, float(item.STARTSECOND), float(item.ENDSECOND)) )


extractEventTimes(sys.argv[1])