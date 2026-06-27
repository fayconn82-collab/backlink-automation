#!/usr/bin/env python3
"""
verify-backlink.py
验证外链页面的链接性质（dofollow/nofollow/mention）

用法:
    python3 verify-backlink.py <url> <domain>
    
示例:
    python3 verify-backlink.py https://check-host.net/check-report/43085d8dkee3 photoeditingprompts.io
"""

import sys
import re
import json
import subprocess

def fetch_page(url):
    """用 curl 获取页面 HTML"""
    cmd = [
        "curl", "-s", "-L", "-o", "-",
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "--max-time", "15",
        url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.returncode

def analyze_links(html, target_domain):
    """分析页面上的链接"""
    # 查找所有 <a> 标签
    link_pattern = r'<a[^>]*href="([^"]*' + re.escape(target_domain) + r'[^"]*)"[^>]*>'
    links = re.findall(link_pattern, html, re.IGNORECASE)
    
    # 查找所有带 rel 的 <a> 标签（更精确匹配）
    full_link_pattern = r'<a([^>]*)href="([^"]*' + re.escape(target_domain) + r'[^"]*)"([^>]*)>'
    full_links = re.findall(full_link_pattern, html, re.IGNORECASE)
    
    results = []
    for prefix, href, suffix in full_links:
        full_tag = prefix + 'href="' + href + '"' + suffix
        
        # 提取 rel 属性
        rel_match = re.search(r'rel="([^"]*)"', full_tag, re.IGNORECASE)
        rel = rel_match.group(1) if rel_match else ""
        
        # 判断是否 nofollow
        is_nofollow = "nofollow" in rel.lower() if rel else False
        
        # 判断链接类型
        if is_nofollow:
            link_type = "nofollow"
        elif rel:
            link_type = "dofollow_with_rel"
        else:
            link_type = "dofollow"
        
        results.append({
            "href": href,
            "rel": rel or "no rel attribute",
            "link_type": link_type,
            "pass_weight": not is_nofollow
        })
    
    return results

def check_noindex(html):
    """检查页面是否有 noindex"""
    noindex_pattern = r'<meta[^>]*name="robots"[^>]*content="[^"]*noindex[^"]*"'
    return bool(re.search(noindex_pattern, html, re.IGNORECASE))

def extract_title(html):
    """提取页面标题"""
    title_match = re.search(r'<title[^>]*>([^<]*)</title>', html, re.IGNORECASE)
    return title_match.group(1).strip() if title_match else ""

def verify_backlink(url, target_domain):
    """验证外链页面"""
    html, status = fetch_page(url)
    
    if status != 0 or not html:
        return {
            "url": url,
            "domain": target_domain,
            "status": "error",
            "error": "Failed to fetch page",
            "http_status": status
        }
    
    # 基础信息
    title = extract_title(html)
    has_domain_in_title = target_domain.lower() in title.lower()
    has_domain_in_url = target_domain.lower() in url.lower()
    is_noindex = check_noindex(html)
    
    # 链接分析
    links = analyze_links(html, target_domain)
    has_actual_links = len(links) > 0
    
    # 判断外链类型
    if has_actual_links:
        # 有实际链接
        dofollow_links = [l for l in links if l["pass_weight"]]
        if dofollow_links:
            backlink_type = "dofollow"
            pass_weight = True
        else:
            backlink_type = "nofollow"
            pass_weight = False
    else:
        # 无实际链接，只是提及
        backlink_type = "mention"
        pass_weight = False
    
    return {
        "url": url,
        "domain": target_domain,
        "status": "success",
        "title": title,
        "has_domain_in_title": has_domain_in_title,
        "has_domain_in_url": has_domain_in_url,
        "has_actual_links": has_actual_links,
        "link_count": len(links),
        "links": links[:5],  # 最多返回 5 个
        "is_noindex": is_noindex,
        "backlink_type": backlink_type,
        "pass_weight": pass_weight,
        "summary": generate_summary(backlink_type, pass_weight, has_actual_links, links)
    }

def generate_summary(backlink_type, pass_weight, has_actual_links, links):
    """生成大白话总结"""
    if backlink_type == "dofollow":
        dofollow_count = len([l for l in links if l["pass_weight"]])
        return f"有{dofollow_count}个dofollow链接，能传递权重"
    elif backlink_type == "nofollow":
        return f"有{len(links)}个链接，但都是nofollow，不传递权重"
    else:
        return "页面上没有实际链接，只是标题/URL提及域名，不传递权重"

def main():
    if len(sys.argv) < 3:
        print("用法: python3 verify-backlink.py <url> <domain>")
        print("示例: python3 verify-backlink.py https://check-host.net/check-report/43085d8dkee3 photoeditingprompts.io")
        sys.exit(1)
    
    url = sys.argv[1]
    target_domain = sys.argv[2]
    
    result = verify_backlink(url, target_domain)
    
    # 输出 JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # 同时输出一行摘要，方便复制到备注
    print("\n--- 备注摘要 ---")
    print(f"backlink_type: {result['backlink_type']} | pass_weight: {result['pass_weight']} | {result['summary']}")

if __name__ == "__main__":
    main()
