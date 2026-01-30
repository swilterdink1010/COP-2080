hp_damage = lambda h, dmg : h - dmg
damage = 20
hp = 100
print(f'Your character took {damage} points of damge')
print(f'Your character has droped from {hp} hit points to ' \
    f'{hp_damage(hp,damage)} hit points available')

