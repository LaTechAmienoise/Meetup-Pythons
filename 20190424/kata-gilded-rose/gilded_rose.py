# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == SULFURAS:
                continue
            self.decrease_sell_in(item)
            self.update_item_quality(item)

    def decrease_sell_in(self, item):
        item.sell_in -= 1

    def update_item_quality(self, item):
        if item.name in {AGED_BRIE, BACKSTAGE_PASS}:
            self.increase_quality(item)
            if item.name == BACKSTAGE_PASS:
                if item.sell_in < 10:
                    self.increase_quality(item)
                if item.sell_in < 5:
                    self.increase_quality(item)
        else:
            self.decrease_quality(item)
        if item.sell_in < 0:
            if item.name == AGED_BRIE:
                self.increase_quality(item)
            else:
                if item.name == BACKSTAGE_PASS:
                    item.quality = 0
                else:
                    self.decrease_quality(item)

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)  # pragma: no cover
