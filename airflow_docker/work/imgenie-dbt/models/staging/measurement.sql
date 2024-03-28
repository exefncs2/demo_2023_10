{{ config(materialized='table',
  depends_on=['ref("base_table_observation")']
  ,unique_key='measurement_id') }}
SELECT
'identifier' as "measurement_id", --缺漏
'valueQuantity' as "unit_concept_id", --缺漏
'referenceRange' as "range_low", --缺漏
'referenceRange' as "range_high", --缺漏
substring(performer from '"reference": "([^"]+)"') as "provider_id", 
substring(encounter from '"reference": "([^"]+)"') as "visit_occurrence_id",
substring(code from '"code": "([^"]+)"') as "measurement_source_value", --不知道取哪個 
substring(subject from '"reference": "([^"]+)"') as "person_id",
substring(code from '"code": "([^"]+)"') as "measurement_concept_id",  --不知道取哪個 
"effectiveDateTime" as "measurement_date", 
"effectiveDateTime" as "measurement_datetime", 
'valueInt' as "value_as_number", --缺漏
'valueCodeableConcept' as "value_as_concept_id" --缺漏
,create_time
FROM 
  {{   ref('base_table_observation')  }}
