from url_downloader import save_file

for i in range({VALUE}):
    
    save_file(url="https://api.masteringnuxt.com/lessons/"+str(i)+"/download/hd?api_token={TOKEN}", file_path='C:/Users/user/Desktop/{PATH}', file_name=str(i)+'.mp4')
