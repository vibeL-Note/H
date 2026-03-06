import json
import os

def get_game_events():
    """获取游戏活动数据（适配前端name字段，无undefined）"""
    events = [
        {
            "game": "原神",
            "name": "风花的呼吸",  
            "start": "2026/03/08",
            "end": "2026/03/22",
            "remind": 1             
        },
        {
            "game": "星穹铁道",
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
    """将活动数据写入data/events.json（路径适配）"""
    # 拼接正确路径（兼容本地+GitHub Actions环境）
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "events.json")
    
    # 确保data文件夹存在
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    
    # 写入JSON（UTF-8编码，格式化）
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    try:
        # 1. 获取活动数据
        events = get_game_events()
        print(f"成功获取 {len(events)} 条活动数据")
        
        # 2. 写入JSON文件
        write_events_to_json(events)
        print("成功写入data/events.json（name字段已适配）")
        
    except Exception as e:
        print(f"同步失败：{str(e)}")
        raise e  # 抛出异常，便于Actions排查

