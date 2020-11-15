class EnemyList:
    __SIZE_OF_SCOPE = 64
    enemies = []

    @classmethod
    def draw_all(cls, display, show_hit_boxes, player, font):
        try:
            for i in range(len(cls.enemies)):
                cls.enemies[i].draw(display, player, font)
                if show_hit_boxes:
                    cls.enemies[i].draw_hitbox(display)
        except IndexError:
            None

    @classmethod
    def hovering_over_enemy(cls, mouse_pos):
        for i in range(len(cls.enemies)):

            p1 = cls.enemies[i].get_hit_point(1)  # top left
            p3 = cls.enemies[i].get_hit_point(3)  # bottom right
            p4 = cls.enemies[i].get_hit_point(4)  # bottom left

            mouse_x, mouse_y = mouse_pos

            mouse_x += cls.__SIZE_OF_SCOPE / 2  # move mouse to correct area
            mouse_y += cls.__SIZE_OF_SCOPE / 2

            if p1[1] <= mouse_y <= p4[1] and p1[0] <= mouse_x <= p3[0]:
                return cls.enemies[i]
        return False

    @classmethod
    def count_enemies(cls):
        return int(len(cls.enemies) / 2)

    @classmethod
    def add(cls, en):
        cls.enemies.append(en)

    @classmethod
    def remove_index(cls, index):
        cls.enemies.pop(index)

    @classmethod
    def remove(cls, en):
        cls.enemies.remove(en)

    @classmethod
    def debug(cls):
        print(cls.enemies)
