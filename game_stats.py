class GameStats:
    """跟踪游戏统计信息"""

    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings=ai_game.settings
        self.rest_stats()
        
        # 让游戏一开始处于非活动状态。
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def rest_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left=self.settings.ship_limit
        self.score=0
        self.level=1