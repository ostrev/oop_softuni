from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        # def __init__(username, level, health, damage):
        self.hero = Hero('username', 4, 100, 25)
        self.hero_test_two = Hero('Test', 4, 10, 50)
        self.enemy_test = Hero('Enemy', 4, 100, 25)

    def test_init(self):
        self.assertEqual('username', self.hero.username)
        self.assertEqual(4, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(25, self.hero.damage)

    def test_battle_rais_exception_for_same_name(self):
        hero_test = Hero('username', 4, 100, 50)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(hero_test)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_health_is_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.hero_test_two)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_health_is_negative(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.hero_test_two)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_enemy_health_is_zero(self):
        self.hero_test_two.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.hero_test_two)
        self.assertEqual(f"You cannot fight {self.hero_test_two.username}. He needs to rest", str(ex.exception))

    def test_battle_if_enemy_health_is_negative(self):
        self.hero_test_two.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.hero_test_two)
        self.assertEqual(f"You cannot fight {self.hero_test_two.username}. He needs to rest", str(ex.exception))

    # def test_battle_hero_and_health_is_change(self):
    #     self.hero.battle(self.enemy_test)
    #     self.assertEqual(20, self.hero.health)
    #     self.assertEqual(20, self.enemy_test.health)
    #
    # def test_battle_enemy_health_is_change(self):
    #     pass

    def test_battle_if_hero_and_enemy_health_is_equal_to_zero(self):
        self.assertEqual('Draw', self.hero.battle(self.enemy_test))

    def test_battle_if_hero_and_enemy_health_is_negative(self):
        self.hero.level = 6
        self.enemy_test.level = 6
        self.assertEqual('Draw', self.hero.battle(self.enemy_test))

    def test_battle_if_hero_is_winner(self):
        self.hero.level = 6
        self.enemy_test.level = 3
        self.assertEqual('You win', self.hero.battle(self.enemy_test))
        self.assertEqual(7, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(30, self.hero.damage)

    def test_battle_if_enemy_is_winner(self):
        self.hero.level = 3
        self.enemy_test.level = 6
        self.assertEqual('You lose', self.hero.battle(self.enemy_test))
        self.assertEqual(7, self.enemy_test.level)
        self.assertEqual(30, self.enemy_test.health)
        self.assertEqual(30, self.enemy_test.damage)

    def test_str(self):
        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                 f"Health: {self.hero.health}\n" \
                 f"Damage: {self.hero.damage}\n"
        self.assertEqual(result, self.hero.__str__())

if __name__ == '__main__':
    main()
