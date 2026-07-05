import pandas as pd


def dataframe(data):

    columns = [

        "ID",
        "Quote",
        "Author",
        "Tags",
        "Scraped At"

    ]

    return pd.DataFrame(
        data,
        columns=columns
    )


def search(df, keyword):

    keyword = keyword.lower()

    return df[

        df["Quote"].str.lower().str.contains(keyword)

        |

        df["Author"].str.lower().str.contains(keyword)

        |

        df["Tags"].str.lower().str.contains(keyword)

    ]


def author_statistics(df):

    return (

        df.groupby("Author")

        .size()

        .reset_index(name="Quotes")

        .sort_values(

            by="Quotes",

            ascending=False

        )

    )


def tag_statistics(df):

    tags = []

    for row in df["Tags"]:

        for tag in row.split(","):

            tag = tag.strip()

            if tag:

                tags.append(tag)

    stats = (

        pd.Series(tags)

        .value_counts()

        .reset_index()

    )

    stats.columns = [

        "Tag",

        "Count"

    ]

    return stats