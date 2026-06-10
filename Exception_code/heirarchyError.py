class DataSourceError(Exception):
    pass

class FileError(DataSourceError):
    pass

class DatabaseError(DataSourceError):
    pass

class APIError(DataSourceError):
    pass

def read_from_file(file_path):
    if not file_path.endswith('.txt'):
        raise FileError("Only txt files are supported")
    return "data from file"

def fetch_from_api(api_url):
    if "invalid_url" in api_url:
        raise APIError("The url is invalid")
    # Fetch the data
    return "Fetch data from api"

def fetch_from_Database(db_query):
    if "DROP" in db_query:
        raise DatabaseError("unsafe query detected")
    # fetch data from database

    return "data from Database"

def process_data(source_type,source):
    try:
        if source_type == "file":
            return read_from_file(source)
        if source_type == "api":
            return fetch_from_api(source)
        if source_type == "databse":
            return fetch_from_Database
        else:
           raise ValueError("Unknown source type")
    except FileError:
      return "File error occurred!"
    except APIError:
      return "API error occurred!"
    except DatabaseError:
      return "Database error occurred!"
    except DataSourceError:
      return "General data source error!"
    except Exception as e:
      return f"An unexpected error occurred: {e}"
    
print(process_data("file", "data.pdf"))
print(process_data("api", "invalid_url"))
print(process_data("database", "DROP TABLE users;"))
print(process_data("unknown", "data.txt"))
