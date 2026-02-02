# 🚀 部署指南 | Deployment Guide

## 快速部署选项

### 选项1: GitHub Pages (推荐 ⭐)

**步骤：**

1. **创建 GitHub 仓库**
   ```bash
   # 访问 https://github.com/new
   # 仓库名: realtime-earth
   # 公开或私有都可以
   ```

2. **推送代码**
   ```bash
   cd /root/clawd/projects/realtime-earth
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/realtime-earth.git
   git push -u origin main
   ```

3. **开启 GitHub Pages**
   - 访问仓库 → Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / (root)
   - 点击 Save
   - 等待 1-2 分钟即可访问

4. **访问网站**
   ```
   https://yourusername.github.io/realtime-earth/
   ```

---

### 选项2: Netlify Drop (最简单 🚀)

**步骤：**

1. **打包项目**
   ```bash
   cd /root/clawd/projects/realtime-earth
   zip -r realtime-earth.zip . -x "*.git*" -x "*.zip"
   ```

2. **部署**
   - 访问 https://app.netlify.com/drop
   - 将 `realtime-earth.zip` 拖放到网页上
   - 等待几秒钟即可上线！

3. **访问**
   - 网站地址类似: `https://vibrant-mclean-abc123.netlify.app`
   - 可以在 Netlify 后台设置自定义域名

---

### 选项3: Vercel (开发者首选 ▲)

**步骤：**

1. **安装 Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **登录并部署**
   ```bash
   cd /root/clawd/projects/realtime-earth
   vercel --prod
   ```
   - 按提示登录 GitHub 账号
   - 选择项目配置
   - 等待部署完成

3. **访问**
   - 地址类似: `https://realtime-earth.vercel.app`

---

### 选项4: Cloudflare Pages

**步骤：**

1. 访问 https://dash.cloudflare.com
2. 进入 Pages → Create a project
3. 上传文件夹或连接 Git
4. 点击 Deploy

---

## 🎯 推荐选择

| 场景 | 推荐平台 | 原因 |
|------|---------|------|
| 快速上线 | Netlify Drop | 无需账号，拖拽即部署 |
| 长期维护 | GitHub Pages | 与代码仓库集成，自动更新 |
| 专业项目 | Vercel | 预览部署、分析、团队协作 |
| 国内访问 | Cloudflare | 全球CDN加速 |

---

## 🔧 本地开发

```bash
# 进入项目目录
cd /root/clawd/projects/realtime-earth

# 启动本地服务器
python3 -m http.server 8080

# 或使用 Node.js
npx serve

# 访问 http://localhost:8080
```

---

## 📞 需要帮助？

遇到问题可以查看：
- Three.js 文档: https://threejs.org/docs/
- 各平台官方文档
- 在 GitHub 上提交 issue
