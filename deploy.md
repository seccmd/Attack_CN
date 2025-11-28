#### 提交仓库代码
```
git add --all && git commit -m test && git push
```

##### GitPage 发布项目

1. 把site/目录，拷贝到 dist/ 目录
2. 把dist/目录，提交到 gh-pages 分支

```
git subtree push --prefix=dist origin gh-pages
```

#### 发布到服务器

```
git clone -b gh-pages https://github.com/seccmd/Attack_CN.git
git -C /data/wwwroot/attack.seccmd.net/  pull
sudo certbot --expand --nginx --nginx-server-root /usr/local/nginx/conf/  -d seccmd.net -d www.seccmd.net -d 123.seccmd.net -d sec123.seccmd.net -d attack.seccmd.net
```
