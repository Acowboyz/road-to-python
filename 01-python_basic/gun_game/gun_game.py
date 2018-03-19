class Person(object):
    
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun  = None
        self.hp   = 100

    def reload_clip(self, clip_temp, bullet_temp):
        """ reload the bullets to the clip """
        clip_temp.bullet_reload(bullet_temp)

    def reload_gun(self, gun_temp, clip_temp):
        """ reload the clip to the gun """
        gun_temp.clip_reload(clip_temp)

    def take_gun(self, gun_temp):
        """ take the gun """
        self.gun = gun_temp

    def shoot(self, enemy_temp):
        """ shoot the enemy """
        self.gun.fire(enemy_temp)

    def loss_hp(self, damage_power_temp):
        self.hp -= damage_power_temp

    def __str__(self):
        if self.gun:
            return "%s's health point : %d, %s"%(self.name, self.hp, self.gun)
        else:
            if self.hp > 0:
                return "%s's health point : %d, no gun"%(self.name, self.hp)
            else:
                return "%s died..."%(self.name)

class Gun(object):
    
    def __init__(self, name):
        super(Gun, self).__init__()
        # Gun type
        self.name = name
        self.clip = None

    def clip_reload(self, clip_temp):
        self.clip = clip_temp

    def fire(self, enemy_temp):
        """ shoot a bullet to the enemy"""
        bullet_temp = self.clip.shoot_bullet()

        if bullet_temp:
            return bullet_temp.hit_enemy(enemy_temp)
        else:
            return None

    def __str__(self):
        if self.clip:
            return "Gun Info : %s, %s"%(self.name, self.clip)
        else:
            return "Gun Info : %s, this gun has no clip"%(self.name)

class Clip(object):
    
    def __init__(self, max_num):
        super(Clip, self).__init__()
        # maximum capacity of the clip
        self.max_num = max_num 
        self.bullet_list = []

    def bullet_reload(self, bullet_temp):
        """ reload the bullet"""
        self.bullet_list.append(bullet_temp)

    def shoot_bullet(self):
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None

    def __str__(self):
        return "Clip Info : %d/%d"%(len(self.bullet_list), self.max_num)

class Bullet(object):
    
    def __init__(self, damage_power):
        super(Bullet, self).__init__()
        # damage power per bullet
        self.damage_power = damage_power 

    def hit_enemy(self, enemy_temp):
        enemy_temp.loss_hp(self.damage_power)

def main():
    """use to setup all the procedure of the program"""

    # 1. create the object of the gun man
    gun_man = Person("Felix")

    # 2. create the object of the gun
    ak47 = Gun("AK47")

    # 3. create the object of the clip
    clip = Clip(20)

    # 4. create the object of the bullet
    # create some bulletss
    for i in range(15):
        bullet = Bullet(10)


        # 5. the gun man reloads the clip
        # gun_man.reload_clip(clip, bullet)
        gun_man.reload_clip(clip, bullet)
    

    # 6. the gun man installs the clip to the gun
    gun_man.reload_gun(ak47, clip)

    # test : info of the bullet
    print(clip)
    # test : info of the clip
    print(ak47)
    # 7. the gun man takes the gun
    gun_man.take_gun(ak47)

    # test : info of the gun man
    print(gun_man)

    # 8. create the object of the enemy
    enemy = Person("Melissa")

    print(enemy)

    # 9. the gun man shoots the enemy
    # gun_man.shoot(enemy)
    for i in range(16):
        gun_man.shoot(enemy)
        print(enemy)
        print(gun_man)

if __name__ == "__main__":
    main()
