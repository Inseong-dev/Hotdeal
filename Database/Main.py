import CrawlPage
import Mydata
#import CrawllingPage # type: ignore
#CollectionID는 Name으로 고정
CollectionID = "Name"
Page = CrawlPage.returnList()
Mydata.add_Data(CollectionID, Page)
