#!/usr/bin/env python3
"""
快速部署脚本 - Realtime Earth
支持多种部署方式
"""

import os
import sys
import subprocess
import json
import http.server
import socketserver
import threading
import time

def print_header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def deploy_github_pages():
    """部署到 GitHub Pages"""
    print_header("部署到 GitHub Pages")
    
    repo_url = input("请输入 GitHub 仓库地址 (例如: https://github.com/username/repo): ").strip()
    if not repo_url:
        print("❌ 错误: 需要提供仓库地址")
        return False
    
    try:
        # 初始化 git
        subprocess.run(["git", "init"], check=True, cwd="/root/clawd/projects/realtime-earth")
        subprocess.run(["git", "add", "."], check=True, cwd="/root/clawd/projects/realtime-earth")
        subprocess.run(["git", "commit", "-m", "Initial commit - Realtime Earth"], 
                      check=True, cwd="/root/clawd/projects/realtime-earth")
        subprocess.run(["git", "branch", "-M", "main"], check=True, cwd="/root/clawd/projects/realtime-earth")
        subprocess.run(["git", "remote", "add", "origin", repo_url], 
                      check=True, cwd="/root/clawd/projects/realtime-earth")
        subprocess.run(["git", "push", "-u", "origin", "main"], 
                      check=True, cwd="/root/clawd/projects/realtime-earth")
        
        print(f"\n✅ 代码已推送到 {repo_url}")
        print(f"\n📋 接下来请在 GitHub 上完成以下操作:")
        print(f"   1. 访问仓库页面: {repo_url}")
        print(f"   2. 点击 Settings → Pages")
        print(f"   3. Source 选择 'Deploy from a branch'")
        print(f"   4. Branch 选择 'main'，文件夹选 '/ (root)'")
        print(f"   5. 点击 Save，等待几分钟即可访问")
        print(f"\n🌐 网站地址将是: https://yourusername.github.io/reponame/")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 错误: {e}")
        return False

def deploy_netlify_drop():
    """通过 Netlify Drop 部署"""
    print_header("Netlify Drop 部署")
    print("\n🚀 Netlify Drop 是最简单的部署方式:")
    print("\n1. 压缩项目文件夹:")
    print("   cd /root/clawd/projects/realtime-earth")
    print("   zip -r realtime-earth.zip .")
    print("\n2. 访问 https://app.netlify.com/drop")
    print("\n3. 将 zip 文件拖放到网页上")
    print("\n4. 几秒钟后你的网站就会上线！")
    print("\n✨ 优势: 免费、快速、支持自定义域名、自动HTTPS")

def deploy_vercel():
    """Vercel 部署指南"""
    print_header("Vercel 部署")
    print("\n🚀 Vercel 是前端开发者的首选平台:")
    print("\n方式1 - 通过 GitHub:")
    print("   1. 将代码推送到 GitHub")
    print("   2. 访问 https://vercel.com")
    print("   3. 导入 GitHub 仓库")
    print("   4. 点击 Deploy")
    print("\n方式2 - Vercel CLI:")
    print("   npm i -g vercel")
    print("   cd /root/clawd/projects/realtime-earth")
    print("   vercel --prod")
    print("\n✨ 优势: 全球CDN、零配置、预览部署、分析功能")

def start_local_server():
    """启动本地服务器"""
    print_header("启动本地服务器")
    
    PORT = 8080
    DIRECTORY = "/root/clawd/projects/realtime-earth"
    
    class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)
        
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"\n🌐 服务器已启动!")
            print(f"\n📍 本地访问: http://localhost:{PORT}")
            print(f"📍 网络访问: http://{get_ip()}:{PORT}")
            print(f"\n📂 服务目录: {DIRECTORY}")
            print(f"\n⚠️  按 Ctrl+C 停止服务器\n")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n👋 服务器已停止")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"\n❌ 端口 {PORT} 已被占用")
            print(f"请尝试: lsof -ti:{PORT} | xargs kill -9")
        else:
            raise

def get_ip():
    """获取本机IP地址"""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def show_menu():
    """显示主菜单"""
    print_header("Realtime Earth 部署工具")
    print("\n请选择部署方式:\n")
    print("  1) 🚀 本地服务器 (立即预览)")
    print("  2) 📦 GitHub Pages (免费静态托管)")
    print("  3) 🌐 Netlify Drop (拖拽部署)")
    print("  4) ▲ Vercel (开发者首选)")
    print("  5) 📖 查看部署说明")
    print("  0) ❌ 退出")
    print()

def main():
    """主函数"""
    import sys
    
    # 如果直接运行，显示菜单
    if len(sys.argv) == 1:
        while True:
            show_menu()
            choice = input("请输入选项编号: ").strip()
            
            if choice == "1":
                start_local_server()
            elif choice == "2":
                deploy_github_pages()
            elif choice == "3":
                deploy_netlify_drop()
            elif choice == "4":
                deploy_vercel()
            elif choice == "5":
                print_header("部署说明")
                print("""
部署选项对比:

┌──────────────┬──────────┬──────────┬──────────┬─────────┐
│    平台      │  难度    │  速度    │  费用    │ 自定义  │
├──────────────┼──────────┼──────────┼──────────┼─────────┤
│ 本地服务器   │   ⭐     │  立即    │  免费    │   ✅    │
│ GitHub Pages │   ⭐⭐   │  2分钟   │  免费    │   ✅    │
│ Netlify Drop │   ⭐     │  30秒    │  免费    │   ✅    │
│ Vercel       │   ⭐⭐   │  1分钟   │  免费    │   ✅    │
└──────────────┴──────────┴──────────┴──────────┴─────────┘

推荐:
• 快速预览 → 本地服务器
• 快速上线 → Netlify Drop
• 长期维护 → GitHub Pages 或 Vercel
                """)
            elif choice == "0":
                print("\n👋 再见!")
                break
            else:
                print("\n❌ 无效选项，请重新选择\n")
    
    # 命令行参数模式
    elif sys.argv[1] == "local":
        start_local_server()
    elif sys.argv[1] == "github":
        deploy_github_pages()
    elif sys.argv[1] == "netlify":
        deploy_netlify_drop()
    elif sys.argv[1] == "vercel":
        deploy_vercel()

if __name__ == "__main__":
    main()
