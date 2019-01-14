#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import time
import feedparser

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, tolerant, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from random import randrange


python_wiki_rss_url = "http://www.poznan.pl/mim/feeds/atom.xml?name=sport"
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial,cascaded=4, block_orientation=-90, rotate=0)
feed = feedparser.parse( python_wiki_rss_url)

for repeats in range(10):
 print(repeats)
 for items in feed["items"]:
     msg = items[ "title"]
#    msg = msg[0:msg.find("")]
     print(msg)
     show_message(device, msg,fill="white", font=proportional(tolerant(LCD_FONT, missing="?")))
     time.sleep(2)
     msg = time.asctime()
     msg= time.strftime("%H:%M:%S")
     print(msg)
     show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
     time.sleep(10)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')

    args = parser.parse_args()

    try:
        demo(args.cascaded, args.block_orientation, args.rotate)
    except KeyboardInterrupt:
        pass
