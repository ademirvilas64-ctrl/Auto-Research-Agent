import os
import feedparser
import requests
from datetime import datetime
import json

# --- Configuration ---
# In GitHub Actions, RSSHub is available at localhost:1200
RSSHUB_BASE_URL = "http://localhost:1200"

# --- Skill 1: InfoFetcher (RSS Implementation) ---
def skill_info_fetcher():
    print("--- Starting Skill 1: InfoFetcher ---")
    
    # Target WeChat Official Accounts (Using 'feeddd' bridge)
    # Format: /feeddd/origin/{WeChat_ID}
    # Note: Using 'feeddd' or '2434' as bridge to bypass anti-crawling
    target_routes = [
        "/feeddd/origin/shujubang",    # 佐思汽车研究
        "/feeddd/origin/LatePostAuto", # 晚点Auto
        "/feeddd/origin/cheyunwang",   # 车云
        "/feeddd/origin/Auto-Bit",     # 汽车之心
    ]
    
    collected_articles = []
    
    for route in target_routes:
        url = f"{RSSHUB_BASE_URL}{route}"
        print(f"Fetching: {url}")
        try:
            feed = feedparser.parse(url)
            print(f"  -> Found {len(feed.entries)} entries")
            
            for entry in feed.entries[:5]: # Config: Limit to latest 5 per source
                # Basic normalization
                article = {
                    "title": entry.get("title", "No Title"),
                    "url": entry.get("link", ""),
                    "publish_date": entry.get("published", datetime.now().isoformat()),
                    "content_snippet": entry.get("summary", "")[:200] + "..."
                }
                collected_articles.append(article)
                
        except Exception as e:
            print(f"  -> Error fetching {route}: {e}")
            
    print(f"Total articles collected: {len(collected_articles)}")
    return collected_articles

# --- Skill 2: Evaluator (Mock) ---
def skill_evaluator(articles):
    print("\n--- Starting Skill 2: Evaluator ---")
    print(f"Evaluating {len(articles)} articles locally...")
    # TODO: Implement LLM scoring here
    return articles # Pass through for now

# --- Main Pipeline ---
def main():
    print(f"Job started at {datetime.now().isoformat()}")
    
    # 1. Fetch
    raw_articles = skill_info_fetcher()
    
    # 2. Evaluate
    qualified_articles = skill_evaluator(raw_articles)
    
    # 3. Output (Mock Database Save)
    output_file = "research_output.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(qualified_articles, f, ensure_ascii=False, indent=2)
    
    print(f"\nPipeline finished. Saved to {output_file}")

if __name__ == "__main__":
    main()
