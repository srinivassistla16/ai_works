from typing import TypedDict, Annotated

class Review (TypedDict):
    summary : Annotated[str , "Summary Of Review" ]
    sentiment: Annotated[str , "Sentiment Based on review" ]