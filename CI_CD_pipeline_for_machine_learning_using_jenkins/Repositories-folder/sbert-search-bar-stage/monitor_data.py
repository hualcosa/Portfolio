from src import dataset, utils, config
import pandas as pd

def monitor_data(prod_data:pd.DataFrame) -> bool:
    """
    use this to keep checking if the production data should be updated
    :param prod_data: pd.DataFrame, data in the prod currently
    """
    project_description_df = dataset.get_project_description()
    project_topics_df = dataset.get_video_titles()
    db_data = utils.generate_data(project_description_df, project_topics_df)[['title']]
    diff1 = set(db_data.title.values.tolist()).difference(set(prod_data.title.values.tolist()))
    diff2 = set(prod_data.title.values.tolist()).difference(set(db_data.title.values.tolist()))
    print("[info] db_data size:", db_data.shape)
    print("[info] prod_data size:", prod_data.shape)
    print("[info] diff1 size:", len(diff1))
    print("[info] diff2 size:", len(diff2))
    if diff1==set() and diff2==set():
        print("DATA UPDATE NOT REQUIRED")
    else:
        print("DATA UPDATE REQUIRED")

if __name__ == "__main__":
    prod_df = pd.read_csv("data/project_mappings.csv")
    monitor_data(prod_df)