from ui import reset_level


def test_reset_level_creates_enemy_group_and_resets_state():
    towers_built = []
    enemy_group = []
    money = 0
    lives = 0
    game_over = True

    towers_built, enemy_group, money, lives, game_over = reset_level(
        [(0, 0), (100, 0)],
        towers_built,
        enemy_group,
        money,
        lives,
        game_over,
        max_lives=10,
    )

    assert len(enemy_group) == 3
    assert money == 500
    assert lives == 10
    assert game_over is False
