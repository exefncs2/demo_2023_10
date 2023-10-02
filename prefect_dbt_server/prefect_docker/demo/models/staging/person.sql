{{ config(materialized='table',
  depends_on=['ref("base_table_patient")']) }}
SELECT
  id as person_id,
  CASE
    WHEN gender = 'male' THEN 8507
    WHEN gender = 'female' THEN 8532
    ELSE 8551
  END as gender_concept_id,
  EXTRACT(YEAR FROM to_date("birthDate", 'YYYY-MM-DD'))::int4 as year_of_birth,
  EXTRACT(MONTH FROM to_date("birthDate", 'YYYY-MM-DD'))::int4 as month_of_birth,
  EXTRACT(DAY FROM to_date("birthDate", 'YYYY-MM-DD'))::int4 as day_of_birth,
  "birthDate" as birth_datetime,
  identifier as person_source_value,
  gender as gender_source_value
FROM 
  {{   ref('base_table_patient')  }}

