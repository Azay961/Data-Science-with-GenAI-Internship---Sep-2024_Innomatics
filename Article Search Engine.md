# Hacking the System Design: How Search Engines Understand and Deliver Results
![search engine](https://github.com/user-attachments/assets/d9a1c765-55c0-4188-a893-6e0a7a594d8c)

Search engines have become essential tools in our digital lives, effortlessly turning complex questions into clear answers within seconds. Whether we’re seeking a quick fact, troubleshooting a problem, or exploring a new topic, these platforms are our go-to for instant information. But behind every swift answer lies a complex system designed to analyze and sort through an enormous web of data, surfacing the most relevant results.

In this article, we’ll take a closer look at what goes on behind the scenes in a search engine. From crawling and indexing to ranking results, I’ll break down the core processes that make it possible for these systems to understand our needs and deliver precise answers. Dive in to uncover the mechanics of the digital tools we rely on every day.

## What Powers a Search Engine? Exploring the Core and Types

Search engines are complex systems designed to sift through vast amounts of data and retrieve relevant results in response to user queries. At their core, they rely on fundamental processes like crawling, indexing, query processing, and ranking. Crawling involves systematically browsing web pages to collect data, which is then indexed to create an organized structure of searchable content.

## Cracking the Relevance Code: How Distance Metrics Deliver the Most Accurate Search Results

Relevance is the heart of search engine success. For search engines, distance metrics like Cosine Similarity and Jaccard Index are key in measuring the relevance between a user’s query and potential results. These metrics calculate how “close” or “similar” a query is to documents in terms of content and context. For instance:

- **Cosine Similarity**: Measures the cosine angle between two vectors (query and document). A smaller angle indicates higher similarity, ideal for queries needing content similarity.
- **Jaccard Index**: Measures the intersection over the union of query and document terms, useful when identifying unique content.

Together, distance metrics allow search engines to determine document similarity levels accurately, fine-tuning the search results to match user intent.

## Scaling Search Engine Architecture: The Game-Changing Role of Query Rewriting and Understanding

Query rewriting and understanding play a pivotal role in enhancing search engine accuracy by interpreting and modifying user queries for better matches with indexed documents.

### Overview of Workflow of Search Engine
![Data Flow Diagram Whiteboard in Dark Yellow Light Yellow Black Monochromatic Style](https://github.com/user-attachments/assets/2f468ddf-99a6-4b96-813e-1b78aca34e9f)


1. **Query Rewriting** is primarily focused on correcting spelling errors in the user’s query to ensure accurate matching with relevant documents in the database. Additionally, it may rephrase or adjust the query to align with terminology commonly used in these documents.  
   - *Example*: If a user searches for “wrork-frome-home,” the system would correct it to “work-from-home” and may further rewrite it as “remote work.” This improves the search algorithm’s ability to retrieve contextually relevant documents.

2. **Query Understanding** is the process of interpreting the user’s intent behind a search query. This involves analyzing the query to identify keywords, context, and any implicit meanings to ensure the search engine retrieves the most relevant results.  
   - *Example*: For a query like “best places to visit in winter,” query understanding would identify that the user is likely looking for travel destinations with winter attractions rather than just general information on winter conditions.

3. **Document Selection** is the process of identifying and retrieving documents from a database that are most relevant to a user’s query. After the query is processed (through steps like rewriting and understanding), the system filters and ranks documents based on relevance.  
   - *Example*: For a query like “best practices for remote work,” the document selection process would identify guides, articles, or reports that specifically cover effective remote work strategies.

4. **Ranking** in information retrieval involves ordering search results by relevance. To evaluate ranking effectiveness, metrics like Cumulative Gain (CG), Discounted Cumulative Gain (DCG), and Normalized Discounted Cumulative Gain (NDCG) are used.

#### Key Metrics
- **Cumulative Gain (CG)**:
  - Measures the relevance of results without considering order.
  - Calculated by summing up relevance scores for all items in the result list.
  - Formula: `CG = sum(relevance[1] + relevance[2] + … + relevance[n])`

- **Discounted Cumulative Gain (DCG)**:
  - Adds weight to the position of items, favoring higher placement.
  - Uses a logarithmic scale to discount relevance scores of lower-ranked items.

- **Normalized Discounted Cumulative Gain (NDCG)**:
  - Normalizes DCG by the ideal DCG (IDCG), the DCG of an optimally ranked list.
  - Provides a score between 0 and 1, where 1 represents the best possible ranking.
  - Formula: `NDCG = DCG / IDCG`

   - *Example*: If a user searches for "remote work benefits," and the ideal list (IDCG) has the most relevant documents ranked highest, we calculate NDCG by comparing the actual DCG to the IDCG to assess ranking quality.

These metrics are crucial in evaluating the relevance and effectiveness of search result rankings.

5. **Blendor/Blending** refers to the process of merging ranked lists from multiple sources or algorithms to create a final, unified list of results. This technique is particularly useful in systems that integrate diverse data sources or employ multiple ranking models to improve relevance.

   ### How Blending Works After Ranking
   - **Ranking Phase**: Each source or algorithm produces its own ranked list based on its internal criteria.
   - **Blending Phase**: These ranked lists are combined, often by assigning weights to different sources or applying machine learning techniques to optimize for relevance and diversity.
   - *Example*: If a search system uses separate algorithms for popularity, recency, and content similarity, each generates a ranked list based on its focus. Blending then merges these lists, potentially giving higher priority to popular and recent items.

6. **SERP** stands for Search Engine Results Page. It refers to the page shown by a search engine in response to a user’s query, displaying the most relevant content tailored to the user’s search intent.

## Result & Conclusion

This exploration of search engine mechanics reveals how complex processes deliver relevant information swiftly. Key steps include query rewriting to correct errors, understanding user intent, selecting relevant documents, and ranking results using metrics like Cumulative Gain (CG) and Normalized Discounted Cumulative Gain (NDCG). Blending further refines these results by merging outputs from various algorithms. Ultimately, the SERP showcases the most relevant content tailored to user needs.

Search engines are powerful tools that transform complex queries into quick, relevant answers. By optimizing each stage — from query processing to result presentation — these systems enhance user experience and ensure users receive the precise information they seek in our vast digital landscape.

This article is a part of my internship work, completed with the guidance of Kanav Sir at Innomatics Research Labs. Credits go to the LIVE session discussion and references below.

## References
1. [GeeksforGeeks: Normalized Discounted Cumulative Gain](https://www.geeksforgeeks.org/normalized-discounted-cumulative-gain-multilabel-ranking-metrics-ml/)
2. [Wikipedia: Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)
3. [Aporia: Practical Guide to Normalized Discounted Cumulative Gain (NDCG)](https://www.aporia.com/learn/a-practical-guide-to-normalized-discounted-cumulative-gain-ndcg/)
