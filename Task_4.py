player_name = input('Введите имя игрока: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy_name = input('Введите имя противника: ')
enemy = {
    'name': enemy_name,
    'health': 50,
    'damage': 30,
    'armor': 1.9
}


def modified_damage(damage, armor):
    return damage / armor


def attack(unit, target):
    damage = modified_damage(unit['damage'], target['armor'])
    target['health'] -= damage


attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)