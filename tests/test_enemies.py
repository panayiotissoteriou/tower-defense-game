from enemies import Enemy


def test_set_path_preserves_spawn_offset():
    enemy = Enemy()
    enemy.spawn_offset = 18

    enemy.set_path([(0, 0), (100, 0)])

    assert enemy.spawn_offset == 18
