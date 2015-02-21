#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 WK4 synthesizing - alarm clock."""

DAYIN = raw_input('What day is today?: ').title()[:3]
TIMEIN = int(raw_input('What time is it now?: '))
SLEEPIN = 'You can sleep some more!'
LATE = 'Beep! ' * 5
TIME = TIMEIN < 600
DAY = DAYIN == 'Sat' or DAYIN == 'Sun'

SNOOZE = True if (DAY or TIME) else False
if SNOOZE:
    print SLEEPIN
else:
    print LATE
