import os
from faker import Faker
import pathlib
import pandas as pd
import logging

# configuring a logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# initializing the fake data generator
fake = Faker()


def profile_factory(n_rows: int) -> pd.DataFrame:
    """Creates fake profile data given the number of rows requested"""
    # generating and returning n_rows of the new data using Faker
    logger.info(f"Generating the fake profile data with {n_rows} rows.")
    data = pd.DataFrame([fake.profile() for _ in range(n_rows)])
    return data


def company_factory(profile_data: pd.DataFrame) -> pd.DataFrame:
    """Takes in profile data and returns a relational table of companies"""
    # creating the new dataFrame from the profile data
    logger.info("Creating the unique company data from the profile data.")
    data = pd.DataFrame()
    data["company"] = pd.Series(profile_data["company"].unique())

    # indexing the data in the profile_data
    logger.info("Indexing company id within the profile_data.")
    profile_data["company_id"] = profile_data["company"].apply(
        lambda company: data.index[data["company"] == company][0]
    )

    # deleting the company column from the profile data
    logger.info("Deleting company column within the profile_data.")
    del profile_data["company"]

    # returning out the company data
    return data


def job_factory(profile_data: pd.DataFrame) -> pd.DataFrame:
    """Takes in profile data and returns a relational table of job titles"""
    # creating the new dataFrame from the profile data
    logger.info("Creating the unique job data from the profile data.")
    data = pd.DataFrame()
    data["job"] = pd.Series(profile_data["job"].unique())

    # indexing the data in the profile_data
    logger.info("Indexing job id within the profile_data.")
    profile_data["job_id"] = profile_data["job"].apply(
        lambda job: data.index[data["job"] == job][0]
    )

    # deleting the company column from the profile data
    logger.info("Deleting job column within the profile_data.")
    del profile_data["job"]

    # returning out the company data
    return data


def main():
    """Main function used to created and save out the data"""
    # generating the fake dataFrames
    logger.info("****** STARTING DATA GENERATION ******")
    profile_data = profile_factory(10_000)
    company_data = company_factory(profile_data)
    job_data = job_factory(profile_data)

    # configuring the locations that we want to save the data
    logger.info("")
    logger.info("****** WRITING SAVE DATA ******")
    data_folder = "fake_data"
    file_names = {
        "profile_data.parquet": profile_data,
        "company_data.parquet": company_data,
        "job_data.parquet": job_data,
    }

    # checking to see if the files have already been created
    # if the files already exist then we delete them and write the new data
    # if the files do not exist then we just write the new data
    for file_name, data in file_names.items():
        # creating the filepath
        file_path = pathlib.Path(data_folder, file_name)

        # checking if the file exists within the file system
        if os.path.exists(file_path):
            logger.info(f"{file_path} exists ... removing from file path.")
            os.remove(file_path)

        # writing the data out to a parquet
        try:
            logger.info(f"Trying to write {file_path}.")
            profile_data.to_parquet(file_path, engine="pyarrow")
            logger.info(f"Successfully saved {file_path}!")
        except Exception as err:
            logger.error(f"{file_path} failed to save with error {err}")

    logger.info("")
    logger.info("All done!")


if __name__ == "__main__":
    main()
