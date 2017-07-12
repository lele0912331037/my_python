#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Race(object):
    """种族类"""
    def __init__(self, race, ps, grade):
        self.race = race
        self.ps = ps
        self.grade = grade

    def get_race(self):
        return '门派：{}\n种族：{}'.format(self.ps, self.race)


class Terran(Race):
    """人族类"""
    def __init__(self, race, ps, grade):
        Race.__init__(self, race, ps, grade)

        # 属性点
        self.point = 0
        self.point_free = 0
        self.physique = 10
        self.mana = 10
        self.power = 10
        self.endurance = 10
        self.agile = 10

        # 属性值
        self.blood = 100
        self.magic = 80
        self.hit = 30
        self.hurt = 34
        self.defense = 0
        self.speed = 0
        self.spiritual = 0

    @property
    def attributes_point(self):
        self.physique += int(self.grade)
        self.mana += int(self.grade)
        self.power += int(self.grade)
        self.endurance += int(self.grade)
        self.agile += int(self.grade)
        return self.physique, self.mana, self.power, self.endurance, self.agile

    @property
    def attributes_value(self):
        self.point_free += int(self.grade * 5 - self.point)
        self.blood += int(self.physique * 5)
        self.magic += int(self.mana * 3)
        self.hit += int(self.mana * 2.01)
        self.hurt += int(self.power * 0.7)
        self.defense += int(self.endurance * 1.5)
        self.speed += int((self.physique + self.endurance + self.power) * 0.1 + self.agile * 0.7)
        self.spiritual += int(self.physique * 0.3 + self.mana * 0.7 + self.power * 0.4 + self.endurance * 0.2)
        return self.blood, self.magic, self.hit, self.hurt, self.defense, self.speed, self.spiritual
    def get_ab(self):
        a = self.attributes_point
        b = self.attributes_value
        return '等级:{}\n气血:{}\n魔法:{}\n命中:{} 体质:{}\n伤害:{} 魔力:{}\n防御:{} 力量:{}\n速度:{} 耐力:{}\n' \
               '灵力:{}敏捷:{}\n潜力：{}'.format(self.grade, b[0], b[1], b[2], a[0], b[3], a[1], b[4], a[2], b[5], \
                a[3], b[6], a[4], self.point_free)

    def add_point(self, virtue, value):
        print(self.power)
        if hasattr(self, virtue):
            points_add = getattr(self, virtue)
            print(self.point)
            if int(value) > self.point_free:
                print('输入点数大于剩余点数')
            else:
                self.point += int(value)
                points_add += input(value)
            return points_add
        else:
            return 'no attribute{}'.format(virtue)

class Datang(Terran):
    """大唐官府类"""
    def __init__(self, race, ps, grade=0):
        Terran.__init__(self, race, ps, grade)

    @property
    def attributes_point(self):
        self.physique = int(10 + self.grade)
        self.mana = int(10 + self.grade)
        self.power = int(10 + self.grade + 2 * self.grade)
        self.endurance = int(10 + self.grade)
        self.agile = int(10 + self.grade)
        return self.physique, self.mana, self.power, self.endurance, self.agile

    def get_attributes(self):
        return self.__dict__

aa = Datang('1', '2',90)

aa.power += 1000
print(aa.power)
print(aa.get_ab())
print(aa.power)