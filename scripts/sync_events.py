import json
import os

def get_game_events():
    """获取一个月内（2026年3月）多游戏官方活动数据"""
    events = [
        # 原神（3月官方活动）
        {
            "game": "原神",
            "name": "幽境危战·紊乱地脉挑战",
            "start": "2026/03/04",
            "end": "2026/04/07",
            "remind": 3
        },
        {
            "game": "原神",
            "name": "3月生日会话题活动",
            "start": "2026/03/01",
            "end": "2026/03/31",
            "remind": 7
        },
        # 星穹铁道（3月官方活动）
        {
            "game": "星穹铁道",
            "name": "4.0版本角色活动跃迁（火花/爻光等）",
            "start": "2026/03/03",
            "end": "2026/03/24",
            "remind": 1
        },
        {
            "game": "星穹铁道",
            "name": "《痴人说梦》听歌领星琼",
            "start": "2026/03/03",
            "end": "2026/03/17",
            "remind": 2
        },
        # 明日方舟（3月官方活动）
        {
            "game": "明日方舟",
            "name": "矢量突破#2「巫术之夜」",
            "start": "2026/03/01",
            "end": "2026/03/20",
            "remind": 3
        },
        {
            "game": "明日方舟",
            "name": "故事集「十字路口」限时活动",
            "start": "2026/03/10",
            "end": "2026/03/24",
            "remind": 1
        },
        {
            "game": "明日方舟",
            "name": "卫戍协议：盟约（下半期）",
            "start": "2026/03/15",
            "end": "2026/03/31",
            "remind": 3
        },
        # 鸣潮（3月官方活动）
        {
            "game": "鸣潮",
            "name": "呜呜企划·呜呜之春限时委托",
            "start": "2026/03/05",
            "end": "2026/03/18",
            "remind": 1
        },
        # 绝区零（3月官方活动）
        {
            "game": "绝区零",
            "name": "引力映叙时光观影活动",
            "start": "2026/03/04",
            "end": "2026/03/23",
            "remind": 2
        },
        {
            "game": "绝区零",
            "name": "2.6版本限时频段调频",
            "start": "2026/03/04",
            "end": "2026/03/23",
            "remind": 1
        },
        {
            "game": "绝区零",
            "name": "「嗯呢」应援礼累计登录",
            "start": "2026/03/02",
            "end": "2026/03/16",
            "remind": 3
        },
        # 无限暖暖（3月官方活动）
        {
            "game": "无限暖暖",
            "name": "元宵惊喜礼邮件领取",
            "start": "2026/03/03",
            "end": "2026/03/05",
            "remind": 1
        },
        {
            "game": "无限暖暖",
            "name": "2.3版本创作激励计划",
            "start": "2026/03/02",
            "end": "2026/03/31",
            "remind": 7
        },
        # 重返未来（3月默认活动，无官方新活动补充）
        {
            "game": "重返未来",
            "name": "UTTU聚光专栏",
            "start": "2026/03/07",
            "end": "2026/03/21",
            "remind": 3
        }
    ]
    return events

def write_events_to_json(events):
    """将一个月内活动数据写入data/events.json"""
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "events.json")
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    try:
        events = get_game_events()
        print(f"成功获取 {len(events)} 条3月官方活动数据")
        write_events_to_json(events)
        print("已写入data/events.json，可同步至日历页面")
    except Exception as e:
        print(f"同步失败：{str(e)}")
        raise e
