class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (40, 40, 40)

        self.ship_speed = 1.5
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (71, 176, 255)
        self.bullet_speed = 1
        self.bullets_allowed = 5

        self.alien_speed = 0.3
        self.alien_points = 50

        self.fleet_direction = 1
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5


    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

