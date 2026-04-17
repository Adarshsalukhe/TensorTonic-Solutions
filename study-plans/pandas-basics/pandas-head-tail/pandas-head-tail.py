import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    df = pd.DataFrame(data)
    df_first= df.head(n)
    df_last = df.tail(n)

    return {
        "head": df_first.to_dict(orient="list"),
        "tail": df_last.to_dict(orient="list")
    }
    
