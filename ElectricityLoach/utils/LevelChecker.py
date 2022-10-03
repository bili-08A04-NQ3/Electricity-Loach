import json


def CanResponse(s, level: int) -> bool:
    # Input must be session
    # s.event.group_id
    with open("ElectricityLoach/GroupManager.json", "r+", encoding="utf-8") as f:
        GroupManager = json.load(f)
        try:
            return GroupManager[str(s.event.group_id)]["level"] >= level
        except:
            f.seek(0)
            f.truncate()
            GroupManager[str(s.event.group_id)] = {
                "level": 1
            }
            json.dump(GroupManager, f)
