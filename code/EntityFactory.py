# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level01BG':
                return './Level01BG.png'
        return None
