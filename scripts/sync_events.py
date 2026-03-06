import json
import os

# --------------- 核心配置：可自定义游戏活动数据 ---------------
# 若有真实爬取接口，替换此处的模拟数据即可
def get_game_events():
    """获取游戏活动数据（标准化字段，与前端匹配）"""
    events = [
        {
            "game": "原神",
            "title": "风花的呼吸",  # 标题字段，前端核心读取
            "start": "2026/03/08",  # 开始时间
            "end": "2026/03/22",    # 结束时间
            "remind": 1             # 提前提醒天数（1=1天，3=3天）
        },
        {
            "game": "崩坏：星穹铁道",
            "title": "模拟宇宙·开拓续闻",  # 补充标题，避免undefined
            "start": "2026/03/06",
            "end": "2026/03/20",
            "remind": 1
        },
        {
            "game": "明日方舟",
            "title": "十字路口",
            "start": "2026/03/10",
            "end": "2026/03/20",
            "remind": 3
        }
    ]
    return events

# --------------- 写入events.json（保证路径正确） ---------------
def write_events_to_json(events):
    """将活动数据写入data/events.json"""
    # 拼接文件路径（适配GitHub Actions运行环境）
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "events.json")
    
    # 确保data文件夹存在（防止路径错误）
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    
    # 写入JSON（UTF-8编码，格式化显示）
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

# --------------- 主函数：执行同步 ---------------
if __name__ == "__main__":
    try:
        # 1. 获取活动数据
        events = get_game_events()
        print(f"成功获取 {len(events)} 条活动数据")
        
        # 2. 写入JSON文件
        write_events_to_json(events)
        print("成功写入data/events.json")
        
    except Exception as e:
        print(f"同步失败：{str(e)}")
        # 抛出异常，让Actions标记失败（便于排查）
        raise e
