# Pseudocode for ETL/ELT Pipeline

def extract_data(source):
    """
    Extract data from the given source.
    Example sources: EMR_A, Payroll_B.
    """
    if source == "EMR_A":
        data = read_emr_data()  # Placeholder for extraction logic
    elif source == "Payroll_B":
        data = read_payroll_data()  # Placeholder for extraction logic
    return data

def transform_data(raw_data):
    """
    Transform raw data by cleaning and normalizing.
    - Clean dates (format conversion)
    - Normalize text fields (trim, case conversion)
    """
    # Example transformation:
    cleaned_data = []
    for record in raw_data:
        record['date'] = standardize_date(record['date'])
        record['name'] = record['name'].strip().title()
        cleaned_data.append(record)
    return cleaned_data

def load_data(cleaned_data, target_table, mode="append"):
    """
    Load the transformed data into the data repository.
    Supports incremental updates by checking for new or updated records.
    """
    if mode == "incremental":
        # Update only new or modified records
        for record in cleaned_data:
            if record_is_new_or_updated(record, target_table):
                upsert_record(record, target_table)
    else:
        bulk_insert(cleaned_data, target_table)

def run_etl_pipeline():
    # List of sources
    sources = ["EMR_A", "Payroll_B"]
    for source in sources:
        raw_data = extract_data(source)
        transformed_data = transform_data(raw_data)
        # Determine target table based on source
        if source == "EMR_A":
            target_table = "FactPatientVisits"
        else:
            target_table = "FactPayroll"
        # Use incremental mode for updates
        load_data(transformed_data, target_table, mode="incremental")

if __name__ == "__main__":
    run_etl_pipeline()

##Key Points for Incremental Updates:

##Use timestamps or change flags to detect new or updated records.
##Use an “upsert” mechanism to update existing records or insert new ones.
