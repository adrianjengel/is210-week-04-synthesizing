#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 WK4 synthesizing - Choosing colors."""


ACIN = 'accent'
HLIG = 'highlight'
QUEST = 'Which {} color, "{}" or "{}"?: '
ANSWER = 'Your selected colors are, {}, {}, and {}.'

BASE = raw_input(QUEST.format('base', 'Seattle Gray', 'Manatee'))

if BASE == 'Seattle Gray':
    ACCENT = raw_input(QUEST.format(ACIN, 'Ceramic Glaze', 'Cumulus Nimbus'))

    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input(QUEST.format(HLIG, 'Basically White', 'White'))
        if HIGHLIGHT == 'Basically White':
            print ANSWER.format(BASE, ACCENT, HIGHLIGHT)
        elif HIGHLIGHT == 'White':
            print ANSWER.format(BASE, ACCENT, HIGHLIGHT)

    elif ACCENT == 'Cumulus Nimbus':
        HIGHLIGHT = raw_input(QUEST.format(HLIG, 'Off-White', 'Paper White'))
        if HIGHLIGHT == 'Off-White':
            print ANSWER.format(BASE, ACCENT, HIGHLIGHT)
        elif HIGHLIGHT == 'Paper White':
            print ANSWER.format(BASE, ACCENT, HIGHLIGHT)

elif BASE == 'Manatee':
    ACCENT = raw_input(QUEST.format(ACIN, 'Platinum Mist', 'Spartan Sage'))

    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input(QUEST.format(HLIG, 'Bone White', 'Just White'))
        if HIGHLIGHT == 'Bone White':
            print ANSWER.format(BASE, ACCENT, HIGHLIGHT)
        elif HIGHLIGHT == 'Just White':
            print ANSWER.format(BASE, ACCENT, HIGHLIGHT)

    elif ACCENT == 'Spartan Sage':
        HIGHLIGHT = raw_input(QUEST.format(HLIG, 'Fractal White', 'Not White'))
        if HIGHLIGHT == 'Fractal White':
            print ANSWER.format(BASE, ACCENT, HIGHLIGHT)
        elif HIGHLIGHT == 'Not White':
            print ANSWER.format(BASE, ACCENT, HIGHLIGHT)
