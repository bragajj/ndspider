# ndspider
## North Dakota Business Search Scraper and Tool


ndspider is a repository containing code for the coding assessment by Sayari Analytics.

## Running the code

All code written for this task can be found in network_tool.py and spiders/nd_spider.py. To run the code, simply go to the top level of the repository and run the following command from the terminal.
```sh
scrapy crawl ndspider && python3 network_tool.py
```
This will start a spider which crawls the North Dakota business search for the data required by the task, saves it to JSON, then creates a network graph and saves it separately. The choice to separate the code for network creation and plotting is due to the nature of its responsibilities. JSON and PNG results can be found in the data folder.
## Notes

- Scrapy has a builtin output function that supports JSON and other formats, I have built in an additional save method for this specific assignment
- I tried to follow the amount of time this task should take from my initial call with the recruiter for Sayari (≈3 hours), as well as assignment's discussion of lines of code (LOC). Both files amount to roughly 100 LOC
- Given more time, there are improvements I would make to this code and visualization process, which I am happy to discuss further


## Network

![nd_network](https://user-images.githubusercontent.com/39658109/207178990-fe56006d-6fba-4af8-b294-ce8df62dc264.png)









