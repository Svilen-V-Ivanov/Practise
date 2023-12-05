from hero.project.hero import Hero
from unittest import TestCase, main


class HeroTests(TestCase):
    USERNAME = 'John'
    OTHER_USERNAME = 'Maria'
    LEVEL = 5
    HEALTH = 30
    DAMAGE = 10
    LEVEL_RISE = 1
    HEALTH_RISE = 5
    DAMAGE_RISE = 5

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test__when_valid_info__creates_valid_class(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test__when_trying_to_fight_enemy_with_same_name__raise_exception(self):
        enemy = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        expected_result = 'You cannot fight yourself'
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy)
        self.assertEqual(expected_result, str(error.exception))

    def test__when_trying_to_fight_with_less_or_equal_to_zero_health__raise_exception(self):
        enemy = Hero(self.OTHER_USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        low_hp_hero = Hero(self.USERNAME, self.LEVEL, 0, self.DAMAGE)
        expected_result = 'Your health is lower than or equal to 0. You need to rest'
        with self.assertRaises(Exception) as error:
            low_hp_hero.battle(enemy)
        self.assertEqual(expected_result, str(error.exception))

    def test_when_trying_to_fight_enemy_with_less_or_equal_to_zero_health__raise_exception(self):
        enemy = Hero(self.OTHER_USERNAME, self.LEVEL, -2, self.DAMAGE)
        expected_result = f'You cannot fight {enemy.username}. He needs to rest'
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy)
        self.assertEqual(expected_result, str(error.exception))

    def test__when_fighting_and_both_enemy_and_hero_drop_below_zero_hp__returns_correct_result(self):
        enemy = Hero(self.OTHER_USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        result = self.hero.battle(enemy)
        expected_result = 'Draw'

        self.assertEqual(expected_result, result)

    def test__when_fighting_and_hero_wins__expect_correct_stats_increments(self):
        enemy = Hero(self.OTHER_USERNAME, 2, self.HEALTH, self.DAMAGE)
        expected_health = self.hero.health + self.HEALTH_RISE - enemy.level * enemy.damage
        expected_enemy_health = enemy.health - self.hero.level * self.hero.damage
        expected_level = self.hero.level + self.LEVEL_RISE
        expected_damage = self.hero.damage + self.DAMAGE_RISE
        result = self.hero.battle(enemy)
        expected_outcome = 'You win'

        self.assertEqual(expected_outcome, result)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_enemy_health, enemy.health)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_damage, self.hero.damage)

    def test__when_fighting_and_hero_looses__expect_correct_stats_increments(self):
        enemy = Hero(self.OTHER_USERNAME, 10, 100, self.DAMAGE)
        expected_health = self.hero.health  - enemy.level * enemy.damage
        expected_enemy_health = enemy.health - self.hero.level * self.hero.damage + self.HEALTH_RISE
        expected_level = enemy.level + self.LEVEL_RISE
        expected_damage = enemy.damage + self.DAMAGE_RISE
        result = self.hero.battle(enemy)
        expected_outcome = 'You lose'

        self.assertEqual(expected_outcome, result)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_enemy_health, enemy.health)
        self.assertEqual(expected_level, enemy.level)
        self.assertEqual(expected_damage, enemy.damage)

    def test__when_str_is_called__returns_correct_value(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual_result = str(self.hero)

        self.assertEqual(expected_result, actual_result)

    if __name__ == '__main__':
        main()