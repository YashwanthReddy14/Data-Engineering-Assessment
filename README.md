# Data-Engineering-Assessment
Overview:

This project designs and implements a consolidated data platform that ingests information from multiple source systems—such as an EMR system (EMR_A) and a payroll provider (Payroll_B)—into a central data repository. The transformed and cleansed data is then surfaced to a BI tool (Tableau) for reporting and analytics.

Assumptions & Approach:

Source Systems:
EMR_A provides clinical and patient visit data.
Payroll_B provides employee payroll information.
Data Repository:
A centralized data warehouse (or lakehouse) stores the cleansed data in a star schema model to support fast aggregation and reporting.
ETL/ELT Pipeline:
A modular pipeline extracts data from each source, transforms (cleans/normalizes) it, and loads it into the data warehouse. Incremental updates are handled via change data capture and timestamp-based filtering.
Security & Governance:
Role-based access control (RBAC), data masking, and encryption (both in transit and at rest) are implemented to safeguard sensitive patient and employee information.
BI Tool Integration:
Tableau connects either via live queries (for smaller, interactive datasets) or through scheduled extracts (for larger volumes).
Real-Time vs. Batch:
While the core pipeline is built for scheduled (batch) loads, the design supports streaming ingestion for near-instant updates where necessary using event-streaming platforms like Kafka or Azure Event Hub.
How to Run/Interpret the Work:

Architecture & Data Model: Review the diagram and data model outline in this documentation for an overview of the data flow and table relationships.
ETL Pipeline: Refer to the pseudocode provided to understand the pipeline’s modular extraction, transformation, and loading stages.
Security & Governance: See the guidelines on RBAC, data masking, and encryption for compliance and data protection.
Queries & Reporting: Example SQL queries are provided for generating key metrics; use these as a starting point in your BI tool.
Real-Time vs. Batch: The optional section explains how the design can be extended to support real-time ingestion.
