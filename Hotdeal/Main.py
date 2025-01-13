import Crawlling.Returnpage as Crawl
import Database.Mydata as DB
CollectionID = "Name"
Page = Crawl.returnList()
DB.add_Data(CollectionID, Page)
DB.delete_Data(CollectionID, Page)
