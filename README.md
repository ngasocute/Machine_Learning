# Machine Learning and Data Mining

This project for purpose analyzing music trending video of users in the world.

## Install environment and packages

- Python(recommend 3.8)
- Pip
- Firefox
- Jupyter notebook

## Install requirements

```bash
pip3 install -r requirements.txt
```

## Crawl data

For crawl url from youtube and located them to scraping_data.txt. Depending on internet banwidth the number of data could change (usually decreasing), so we don't recommend you running the script again and use our default data file

```bash
python youtube_scraping.py
```

## Preprocess data

From list url at file scraping_data.txt we extract ID and call API to youtube to get the information of each video and store in file list_infor.csv and id are stored in file list_id.txt

```
python scraping_info_data_youtube.py
```

## Data Analysis

Run vscode file: youtube_music_analysis.ipynb <br>
or <br>
run notebook: youtube_music_analysis.ipynb
