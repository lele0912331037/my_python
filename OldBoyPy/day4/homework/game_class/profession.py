#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Race(object):
    """种族类"""
    def __init__(self, race, ps):
        self.race = race
        self.ps = ps

    def get_race(self):
        return '门派：{}\n种族：{}'.format(self.ps, self.race)


class Terran(Race):
    """人族类"""
    def __init__(self, race, ps):
        Race.__init__(self, race, ps)

        # 属性点
        self.physique = 10
        self.mana = 10
        self.power = 10
        self.endurance = 10
        self.agile = 10
        self.grade = 0
        self.point = 0
        # 属性值
        self.blood = 150
        self.magic = 110
        self.hurt = 41
        self.defense = 15
        self.speed = 8


    @property
    def growing_physique(self):
        self.physique = int(10 + 5 * self.grade + 0.1 * self.grade)
        return self.physique

    @property
    def growing_mana(self):
        self.mana = int(10 + 5 * self.grade)
        return self.mana

    @property
    def growing_power(self):
        self.power = int(10 + 5 * self.grade)
        return self.power

    @property
    def growing_endurance(self):
        self.endurance = int(10 + 5 * self.grade + 0.08 * self.grade)
        return self.endurance

    @property
    def growing_agile(self):
        self.agile = int(10 + 5 * self.grade + 0.11 * self.grade)
        return self.agile

    @property
    def growing_point(self):
        self.point = int(self.grade * 5)
        return self.point

    @property
    def growing_blood(self):
        self.blood = int(self.growing_physique * 5 + 100)
        return self.blood

    @property
    def growing_magic(self):
        self.magic = int(self.growing_mana * 3 + 80)
        return self.magic

    @property
    def growing_hurt(self):
        self.hurt = int(self.growing_power * 0.7 + 34)
        return self.hurt

    @property
    def growing_defense(self):
        self.defense = int(self.growing_endurance * 1.5)
        return self.defense

    @property
    def growing_speed(self):
        self.speed = int((self.growing_physique + self.growing_endurance + self.growing_power) * 0.1 \
                         + self.growing_agile * 0.7)
        return self.speed

    @property
    def growing_spiritual(self):
        self.spiritual = int(self.growing_physique * 0.3 + self.growing_mana * 0.7 + self.growing_power * 0.4 \
                             + self.growing_endurance * 0.2)
        return self.spiritual

    def get_ab(self):
        return '等级：{}\n气血{} 体质：{}\n魔法：{} 法力：{}\n伤害：{} 力量：{}\n防御：{} 耐力：{}\n速度：{} 敏捷：{} ' \
               '\n灵力：{} 可用属性点：{}'.format(self.grade, self.growing_blood, self.growing_physique,
                self.growing_magic, self.growing_mana, self.growing_hurt, self.growing_power, self.growing_defense, \
                self.growing_endurance, self.growing_speed, self.growing_agile, self.growing_spiritual, \
                self.growing_point)

    def add_point(self, virtue, value):
        self.virtue += value
        return self.virtue


class Datang(Terran):
    """大唐官府类"""
    def __init__(self, race, ps):
        Terran.__init__(self, race, ps)

    @property
    def growing_power(self):
        self.power = 10 + 5 * self.grade + 2 * self.grade
        return self.power

    def get_attributes(self):
        return self.__dict__

