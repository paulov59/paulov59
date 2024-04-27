import os
datas = ['2024-04-12', '2024-04-16', '2024-04-19']
text = '''<h2>Hi 👋</h2>

<p>My name is Paulo Victor, I'm a backend developer and undergraduate student of Computer Science at Federal University of Alagoas - UFAL.</p>
<hr>
<h2>My Github's statitics</h2>
<div align="center">
  <a href="https://github.com/paulov59">
  <img height="150em" src="https://github-readme-streak-stats.herokuapp.com/?user=paulov59&theme=github-dark-blue&hide_border=true"/>
  <img height="150em" src="https://github-readme-stats-paulov59.vercel.app/api?username=paulov59&show_icons=true&theme=github_dark&rank_icon=github&include_all_commits=true&hide_border=true"/>
  <img height="200em" src="https://github-readme-stats-paulov59.vercel.app/api/top-langs/?username=paulov59&layout=compact&langs_count=7&theme=github_dark&hide_border=true"/>
</div>
<hr>
<h2>Contact with me</h2>
<div align="center">
    <a href = "mailto:pvls2@ic.ufal.br"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="https://www.linkedin.com/in/paulo-severiano/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href = "mailto:paulo.victor@nees.ufal.br"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>
'''

text2 = '''<h2>Hi 👋</h2>

<p>My name is Paulo Victor, I'm a backend developer and undergraduate student of Computer Science at Federal University of Alagoas - UFAL.</p>
<hr>
<h2>My Github's statitics</h2>
<div align="center">
  <a href="https://github.com/paulov59">
  <img height="150em" src="https://github-readme-streak-stats.herokuapp.com/?user=paulov59&theme=github-dark&hide_border=true"/>
  <img height="150em" src="https://github-readme-stats-paulov59.vercel.app/api?username=paulov59&show_icons=true&theme=github_dark&rank_icon=github&include_all_commits=true&hide_border=true"/>
  <img height="200em" src="https://github-readme-stats-paulov59.vercel.app/api/top-langs/?username=paulov59&layout=compact&langs_count=7&theme=github_dark&hide_border=true"/>
</div>
<hr>
<h2>Contact with me</h2>
<div align="center">
    <a href = "mailto:pvls2@ic.ufal.br"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="https://www.linkedin.com/in/paulo-severiano/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href = "mailto:paulo.victor@nees.ufal.br"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>
'''
i=1
for data in datas:
    readme = open("README.md", "w")
    if i % 2:
        readme.write(text)
    else:
        readme.write(text2)
    readme.close()
    add = "git add README.md"
    message =  f"git commit -m 'update readme.md' --date=format:local:{data}"
    push = "git push"
    os.system(add)
    os.system(message)
    os.system(push)
    i+=1