FROM nginx:latest
RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf \
 && mkdir -p /usr/share/nginx/html/static \
 && mkdir -p /usr/share/nginx/html/media \
 && mkdir -p /usr/share/nginx/ssl


# 添加配置文件
ADD ./nginx.conf /etc/nginx/

# 设置Media文件夹用户和用户组为Linux默认www-data, 并给予可读和可执行权限,
# 否则用户上传的图片无法正确显示。
# RUN chown -R www-data:www-data /usr/share/nginx/html/media \
# && chmod -R 775 /usr/share/nginx/html/media
 
# 关闭守护模式
CMD ["nginx", "-g", "daemon off;"]