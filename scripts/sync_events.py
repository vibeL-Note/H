import json
import os

def get_game_events():
    """获取游戏活动数据（统一game字段为星穹铁道，适配分类）"""
    events = [
        {
            "game": "原神",          # 与顶部分类标签一致
            "name": "风花的呼吸",    # 标题字段（前端读取name）
            "start": "2026/03/08",
            "end": "2026/03/22",
            "remind": 1             # 提前1天提醒
        },
        {
            "game": "星穹铁道",      # 关键：去掉“崩坏：”前缀，匹配分类标签
            "name": "模拟宇宙·开拓续闻",
            "start": "2026/03/06",
            "end": "2026/03/20",
            "remind": 1
        },
        {
            "game": "明日方舟",
            "name": "十字路口",
            "start": "2026/03/10",
            "end": "2026/03/20",
            "remind": 3
        }
    ]
    return events

def write_events_to_json(events):
    """写入data/events.json（路径适配）"""
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "events.json")
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    try:
        events = get_game_events()
        print(f"成功获取 {len(events)} 条活动数据")
        write_events_to_json(events)
        print("成功写入data/events.json（字段已适配分类）")
    except Exception as e:
        print(f"同步失败：{str(e)}")
        raise e
