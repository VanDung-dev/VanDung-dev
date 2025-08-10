import json


def generate_readme(lang):
    try:
        with open('content.json', 'r', encoding='utf-8') as f:
            content = json.load(f)
    except FileNotFoundError:
        print("content.json not found.")
        return
    except json.JSONDecodeError:
        print("content.json is not valid JSON.")
        return

    # Lấy dữ liệu từ content
    profile = content['profile'][lang]
    academic = content['academic'][lang]
    technical_skills = content['technical_skills'][lang]
    projects = content['projects'][lang]
    contact = content['contact']
    stats = content['stats'][lang]
    lang_switch = content['language_switch']
    harvard_cert = content['harvard_cert']
    harvard_cert_title = content['harvard_cert']
    harvard_cert_badge = content['harvard_cert'][lang]

    # Xác định tên file và ngôn ngữ chuyển đổi
    filename = "README.md" if lang == "en" else "README_vi.md"
    lang_link = "README_vi.md" if lang == "en" else "README.md"
    lang_text = lang_switch['en_to_vi'] if lang == "en" else lang_switch['vi_to_en']

    # Câu vui nhộn theo ngôn ngữ
    fun_fact = "☕ Code not running? Don't worry, it's just... The testing feature is not complete!" if lang == "en" else \
        "☕ Code không chạy? Đừng lo, đó chỉ là... tính năng thử nghiệm chưa hoàn thiện!"

    # Tạo nội dung README
    md_content = f"""
# 👋 {profile['hello']}
<div>
  <h2>{profile['name']}</h2>
  <h3>🚀 {profile['title']}</h3>
  <p><em>{profile['description']}</em></p>
</div>

---
> {fun_fact}
---

## 📚 {academic['title']}

🎓 **{academic['institution']}**  
📘 {academic['program']}

---

## 🏅 {harvard_cert_badge['badge']} &nbsp;

<div style="background: #f8f9fa; border-left: 4px solid #A51C30; padding: 10px 15px; margin: 15px 0; border-radius: 4px;">
  <h2 style="color: #333; margin: 0;">
    <strong>{harvard_cert_title['title']}</strong>
  </h2>
  <p style="margin: 8px 0; font-size: 1.1em; color: #333;">
    {harvard_cert['issuer']}
  </p>
  <p style="margin: 5px 0; font-size: 1.1em; color: #333;">
    <strong>Issued:</strong> {harvard_cert['date']} | <strong>ID:</strong> {harvard_cert['id']}
  </p>
  <p style="margin: 5px 0; font-size: 1.1em; color: #333;">
    <strong>Verified by:</strong> {harvard_cert['signature']}
  </p>
  <a href="{harvard_cert['url']}" style="display: inline-block; background: #A51C30; color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; margin-top: 10px; font-weight: bold;">
    View Verified Certificate
  </a>
</div>

---

## 💼 {technical_skills['title']}

### 🛠️ {technical_skills['core']['title']}
"""

    # Thêm các kỹ năng cốt lõi dưới dạng huy hiệu
    md_content += "<p>\n"
    for item in technical_skills['core']['items']:
        md_content += f"  <img src=\"https://img.shields.io/badge/  {item['badge']}\" alt=\"{item['name']}\" />\n"
    md_content += "</p>\n"

    md_content += f"""

### 🧩 {technical_skills['libraries']['title']}
"""
    # Thêm các thư viện dưới dạng huy hiệu
    md_content += "<p>\n"
    for item in technical_skills['libraries']['items']:
        md_content += f"  <img src=\"https://img.shields.io/badge/  {item['badge']}\" alt=\"{item['name']}\" />\n"
    md_content += "</p>\n"

    md_content += f"""

### 🧰 {technical_skills['tools']['title']}
"""
    # Thêm các công cụ dưới dạng huy hiệu
    md_content += "<p>\n"
    for item in technical_skills['tools']['items']:
        md_content += f"  <img src=\"https://img.shields.io/badge/  {item['badge']}\" alt=\"{item['name']}\" />\n"
    md_content += "</p>\n"

    # Thêm các dự án nổi bật
    featured_projects_title = "🌟 Featured Projects" if lang == "en" else "🌟 Dự án nổi bật"
    md_content += f"""

---

## {featured_projects_title} &nbsp;

"""
    for project in projects:
        md_content += f"### 📌 [{project['title']}]({project['url']})\n"
        md_content += f"{project['description']}\n\n"
        technical_highlights_title = "🔧 Technical Highlights:" if lang == "en" else "🔧 Điểm nổi bật kỹ thuật:"
        md_content += f"**{technical_highlights_title}**\n"
        for highlight in project['highlights']:
            md_content += f"  - {highlight}\n"
        md_content += "\n"

    # Thêm thống kê GitHub
    md_content += f"""

---

## 📊 {stats['title']}

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=VanDung-dev&hide_title=false&hide_rank=false&show_icons=true&include_all_commits=false&count_private=false&disable_animations=false&theme=radical&locale={lang}&hide_border=false&order=1" height="150" alt="stats graph"  />
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=VanDung-dev&locale={lang}&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=radical&hide_border=false&order=2" height="150" alt="languages graph"  />
</div>

"""

    # Thêm liên hệ
    md_content += f"""

---

## 📬 {contact[lang]['title']}

<div align="center">
"""

    # Thêm liên kết liên hệ
    for link in contact['links']:
        md_content += f"""  <a href="{link['url']}">
    <img src="https://img.shields.io/badge/{link['name']}-{link['color']}?logo={link['icon']}&logoColor=white&style=for-the-badge&effect=plastic" />
  </a>
  \n"""

    md_content += f"""</div>

<div align="center" style="margin-top: 20px; padding: 12px; background: linear-gradient(145deg, #2e7d32, #1b5e20); border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <a href="{lang_link}" style="color: #fff; font-size: 1.6em; text-decoration: none; font-weight: bold;">
     {lang_text}
  </a>
</div>

<br>

<div align="center">
  <img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake-dark.svg" alt="Snake animation" />
</div>
"""

    # Ghi file README
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"🎉 Generated {filename} successfully! It's alive and kicking! 🚀")


if __name__ == "__main__":
    generate_readme("en")
    generate_readme("vi")