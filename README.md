# Machine Learning and Data Mining
This project for purpose analyzing music trending video of users in the world.

### Install requirements

```bash
pip3 install -r requirements.txt
```
### Install environment
Install firefox

### Crawl data

```bash
python youtube_scraping.py
# for crawl url from youtube and located them to scraping_data.txt
# then 
python scraping_info_data_youtube.py 
# from list url at file scraping_data.txt we extract ID and call API to youtube to get the information of each video and store in file list_infor.csv and id are stored in file list_id.txt
```

### Data Analysis
run step by step file: youtube_music_analysis.ipynb
