import json
import os

class ScenarioConfigRecord:
    def __init__(self):
        self.ego = {}
        self.config = {}
        self.config_path = "/home/lhy/projects/scenario_runner/config/"
        self.index = 1

    def ego_info_w(self, ego_info):
        self.ego = {
            "name": ego_info["name"],
            "behavior_type": ego_info["behavior_type"],
            "model_name": ego_info["model_name"],
            "hyperparameters": {
                "max_speed": ego_info["max_speed"],
                "max_acc": ego_info["max_acc"]
            },
            "start_position": {
                "lane_id": ego_info["start_lane_id"],
            },
            "end_position": {
                "lane_id": ego_info["end_lane_id"],
            },
            "distance_to_go": ego_info["distance_to_go"]
        }
        self.config['ego_vehicle'] = self.ego


    def npc_info_w(self, npc_info):
        npc = {
            "name": npc_info["name"],
            "behavior_type": npc_info["behavior_type"],
            "model_name": npc_info["model_name"],
            "hyperparameters": {
                "max_speed": npc_info["max_speed"],
                "max_acc": npc_info["max_acc"]
            },
            "start_position": {
                "lane_id": npc_info["start_lane_id"],
                "position": npc_info["start_position"]
            },
            "end_position": {
                "lane_id": npc_info["end_lane_id"],
                "position": npc_info["end_position"]
            }
        }
        self.config['npc'+str(self.index)] = npc
        self.index += 1

    def write_to_json(self):
        fileidx = 0
        while os.path.exists(self.config_path + '{}.json'.format(fileidx)):
            fileidx += 1

        with open(self.config_path +'{}.json'.format(fileidx), 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4)

