import pandas as pd
import faiss
from src import query_search
from src import config

# load index
index = faiss.read_index(f'{config.DIR_OUTPUT}/search.index')

def validate_data_change(added:list, removed:list, df:pd.DataFrame) -> float:
    """
    This function checks whether added/removed rows in the project mappings
    can be found/not-found through the search bar.
    :param added: list, added rows
    :param removed: list, removed rows
    :param df: project mappings dataframe
    :return: float, ratio of found/not-found rows
    """
    # select 5 random rows
    # search through the search bar and write results in a vector
    # return the ratio of found/not-found rows
    
    validations = []
    if len(added)>0:
        added = pd.DataFrame(added, columns=['title'])
        for item in added.sample(min(5, len(added)))['title'].values.tolist():
            results = query_search.search(item, index, config.NUM_OF_SEARCH_RESULTS, df).title.values.tolist()
            results = list(map(lambda x: x.lower().strip(), results))
            if item.lower() in results:
                validations.append(1)
            else:
                validations.append(0)
                print(f"[warning] added item not found in search results : {item}")
    if len(removed)>0:
        removed = pd.DataFrame(removed, columns=['title'])
        for item in removed.sample(min(5, len(removed)))['title'].values.tolist():
            results = query_search.search(item, index, config.NUM_OF_SEARCH_RESULTS, df).title.values.tolist()
            results = list(map(lambda x: x.lower().strip(), results))
            if item.lower() in results:
                validations.append(0)
                print(f"[warning] removed item found in search results : {item}")
            else:
                validations.append(1)
    return sum(validations)/len(validations)
        

def validate(df:pd.DataFrame, df_old:pd.DataFrame) -> int:
    """
    This function executes the data validation process.
    :param df: project mappings dataframe
    :param df_old: project mappings dataframe
    :return: int, 0 if data has not changed, 1 if data has changed
    """
    # check if data has changed
    # if data has changed, run the validation process
    # if data has not changed, check if the search index is still ok (There might be a bug due to code changes)
    assert 'title' in df.columns, 'title column not found in project mappings'
    added = list(set(df.title.values.tolist()).difference(set(df_old.title.values.tolist())))
    removed = list(set(df_old.title.values.tolist()).difference(set(df.title.values.tolist())))
    if added==[] and removed==[]:
        # note that we check the search index if it is not hard-coded to always return the entered query
        print("[info] data has not changed, checking if code changes have not broken the search index")
        sample = list(set(df.sample(1).title.values.tolist()))
        validation = validate_data_change(added=sample, removed=["The search index is not hard-coded to always return the entered query"], df=df)
    else:
        validation = validate_data_change(added, removed, df=df)
    return int(validation>0.5)
    
    
if __name__=="__main__":
    print("[info] validating data change")
    try:
        df = pd.read_csv("data/project_mappings.csv")
        df_old = pd.read_csv("temp_ml/project_mappings.csv")
    except:
        df = pd.read_csv("data/project_mappings.csv")
        df_old = pd.read_csv("data/project_mappings.csv.bak")
    if validate(df, df_old)==1:
        print("CHANGE VALIDATION: SUCCESS")
    else:
        print("CHANGE VALIDATION: FAILURE")