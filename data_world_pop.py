import pandas as pd
from pathlib import Path

def load_world_pop():
    raw_path = Path("data/data_population_world.csv")
    clean_path = Path("data/world_pop_clean.csv")
    os_path = Path("data/olympics_clean.csv")

    if not os_path.exists():
        #load_data()
        pass
    os = pd.read_csv(os_path)

    if clean_path.exists():
        df = pd.read_csv(clean_path, index_col=0)
    elif not raw_path.exists():
        raise FileNotFoundError(f"Could not find {raw_path}")
    else:
        df = pd.read_csv(raw_path, index_col='country_name')
        df.index = df.index.str.lower().str.capitalize()
        df.index.name = 'Team'

        df = df.drop(columns=[
            i for i in df.columns if i not in os['Year'].unique().astype(str)])
        
        df = df.drop(index=[
            i for i in df.index if i not in os['Team'].unique()])
        
        df.insert(0, 'Mean pop', df.mean(axis=1).round(0))
        
        df.to_csv(clean_path, index=True)

    return df


if __name__ == "__main__":
    print(f"loaded world pop DataFrame:\n{load_world_pop().head()}")