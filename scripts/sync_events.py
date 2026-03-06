import requests
from bs4 import BeautifulSoup
import re
import json
import os
from datetime import datetime

# 官方数据源配置（全游戏适配）
OFFICIAL_SOURCES = {
    "genshin": {
        "name": "原神",
        "url": "https://genshin.hoyoverse.com/zh-cn/news/event",
        "item_selector": "div.event-item",
        "title_selector": "h3",
        "time_selector": "div.event-time",
        "time_regex": r"(\d{4}/\d{2}/\d{2})"
    },
    "starrail": {
        "name": "星穹铁道",
        "url": "https://hsr.hoyoverse.com/zh-cn/news/event",
        "item_selector": "div.news-item",
        "title_selector": "h4",
        "time_selector": "span.date",
        "time_regex": r"(\d{4}-\d{2}-\d{2})"
    },
    "mingchao": {
        "name": "鸣潮",
        "url": "https://www.wutheringwaves.com/news",
        "item_selector": "li.news-list-item",
        "title_selector": "a",
        "time_selector": "span.time",
        "time_regex": r"(\d{4}-\d{2}-\d{2})"
    },
    "juequ": {
        "name": "绝区零",
        "url": "https://www.zero.game/zh-cn/news",
        "item_selector": "div.news-card",
        "title_selector": "h3",
        "time_selector": "span.time",
        "time_regex": r"(\d{4}-\d{2}-\d{2})"
    },
    "warmth": {
        "name": "无限暖暖",
        "url": "https://nikki.istero.com/zh-cn/news",
        "item_selector": "div.news-item",
        "title_selector": "h3",
        "time_selector": "div.time",
        "time_regex": r"(\d{4}-\d{2}-\d{2})"
    },
    "reverse": {
        "name": "重返未来",
        "url": "https://www.reverse1999.com/zh-cn/news",
        "item_selector": "div.news-item",
        "title_selector": "h3",
        "time_selector": "span.date",
        "time_regex": r"(\d{4}-\d{2}-\d{2})"
    },
    "Arknigs": {
        "name": "明日方舟",
        "url": "https://ak.hypergryph.com/news",
        "item_selector": "div.news-item",
        "title_selector": "h3",
        "time_selector": "span.date",
        "time_regex": r"(\d{4}-\d{2}-\d{2})"
    },
    "Arknigs:Endfield": {
        "name": "明日方舟：终末地",
        "url": "https://endfield.hypergryph.com/news",
        "item_selector": "div.news-item",
        "title_selector": "h3",
        "time_selector": "span.date",
        "time_regex": r"(\d{4}-\d{2}-\d{2})"
    }
}

def crawl_events():
    all_events = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    for game_key, config in OFFICIAL_SOURCES.items():
        try:
            print(f"正在抓取{config['name']}活动...")
            response = requests.get(config["url"], headers=headers, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            
            items = soup.select(config["item_selector"])
            for item in items[:10]:  # 只取最新10条
                try:
                    title = item.select_one(config["title_selector"]).get_text(strip=True)
                    time_text = item.select_one(config["time_selector"]).get_text(strip=True)
                    time_matches = re.findall(config["time_regex"], time_text)
                    
                    if len(time_matches) >= 2:
                        start_date = time_matches[0].replace("/", "-")
                        end_date = time_matches[1].replace("/", "-")
                        all_events.append({
                            "id": int(datetime.now().timestamp() * 1000) + len(all_events),
                            "name": title,
                            "game": game_key,
                            "start": start_date,
                            "end": end_date,
                            "remind": 1
                        })
                except Exception as item_err:
                    continue
            print(f"✅ {config['name']}抓取完成，共{len([e for e in all_events if e['game'] == game_key])}条")
        except Exception as e:
            print(f"❌ {config['name']}抓取失败：{e}")
            continue

    # 去重
    seen = set()
    unique_events = []
    for event in all_events:
        key = f"{event['name']}_{event['game']}"
        if key not in seen:
            seen.add(key)
            unique_events.append(event)
    
    # 保存文件
    os.makedirs("data", exist_ok=True)
    output_path = os.path.join("data", "events.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(unique_events, f, ensure_ascii=False, indent=2)
    print(f"\n✅ 全部抓取完成，共{len(unique_events)}条有效活动，已保存到{output_path}")

if __name__ == "__main__":
    crawl_events()